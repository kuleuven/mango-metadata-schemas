from unittest import result
from flask import (
    Blueprint,
    render_template,
    current_app,
    url_for,
    redirect,
    g,
    send_file,
    abort,
    stream_with_context,
    Response,
    request,
    flash,
)

import os
import json
import base64

from werkzeug.datastructures import MultiDict

# from irods.meta import iRODSMeta, AVUOperation

# from irods.models import Column, Collection, DataObject, DataObjectMeta, CollectionMeta
# from irods.column import Criterion

# from irods.query import Query


from slugify import slugify

# from csrf import csrf

from pprint import pprint


from .editor import get_metadata_schema_dir

from . import (
    get_schema_manager,
    FileSystemSchemaManager,
)  # ??? HOW TO IMPORT IT
import logging

from .demo_classes import (
    DemoAVU,
    demo_collection,
    demo_data_object,
)


metadata_schema_form_bp = Blueprint(
    "metadata_schema_form_bp",
    __name__,
    template_folder="templates/metadata_schema",
)


def flatten_schema(object_tuple, level=0, prefix="", result_dict={}, **kwargs):
    (_key, _dict) = object_tuple
    for p_key, _property in _dict["properties"].items():
        result_dict[f"{prefix}.{p_key}"] = {
            "label": _property["title"],
            "type": _property["type"],
            "level": level,
        }

        if _property["type"] == "object":
            result_dict[f"{prefix}.{p_key}"]["properties"] = [
                f"{prefix}.{p_key}.{x}" for x in _property["properties"].keys()
            ]
            result_dict = flatten_schema(
                (p_key, _property),
                level=(level + 1),
                prefix=f"{prefix}.{p_key}",
                result_dict=result_dict,
            )

    return result_dict


def get_schema_prefix_from_filename(filename):
    """
    filename must end with '.json'
    """
    if filename.endswith(".json"):
        filename = filename[:-5]
        return slugify(filename)
    else:
        return False


def get_schema_prefix(schema_identifier=False, schema_filename=False):
    if schema_identifier:
        return f"{current_app.config['MANGO_SCHEMA_PREFIX']}.{schema_identifier}"
    if schema_filename:
        return f"{current_app.config['MANGO_SCHEMA_PREFIX']}.{get_schema_prefix_from_filename(schema_filename)}"


def add_to_dict(metadata_items, multidict, unit_level=1):
    name_length = 2 + unit_level
    simple_fields = [
        meta_data_item
        for meta_data_item in metadata_items
        if len(meta_data_item.name.split(".")) == name_length
    ]
    composite_fields = set(
        (
            ".".join(meta_data_item.name.split(".")[:name_length]),
            ".".join(meta_data_item.units.split(".")[:unit_level])
            if meta_data_item.units
            else None,
        )
        for meta_data_item in metadata_items
        if len(meta_data_item.name.split(".")) > name_length
    )
    if len(composite_fields) > 1:
        composite_fields = sorted(
            list(composite_fields), key=lambda x: int(x[1].split(".")[unit_level - 1])
        )
    for meta_data_item in simple_fields:
        multidict.add(meta_data_item.name, meta_data_item.value)
    for composite_name, composite_unit in composite_fields:
        subdict = MultiDict()
        composite_items = [
            meta_data_item
            for meta_data_item in metadata_items
            if meta_data_item.name.startswith(composite_name)
        ]
        if composite_unit:
            subdict.add("__unit__", composite_unit)
            composite_items = [
                meta_data_item
                for meta_data_item in composite_items
                if meta_data_item.units.startswith(composite_unit)
            ]
        add_to_dict(composite_items, subdict, unit_level + 1)
        multidict.add(composite_name, subdict.to_dict(flat=False))


@metadata_schema_form_bp.route("/metadata-schema/edit", methods=["POST", "GET"])
def edit_schema_metadata_for_item():
    """ """
    _parameters = request.values.to_dict()

    item_type = _parameters["item_type"]
    object_path = _parameters["object_path"]
    if not object_path.startswith("/"):
        object_path = "/" + object_path
    schema = _parameters["schema"]
    realm = _parameters["realm"]
    prefix = get_schema_prefix(schema_identifier=schema)

    schema_manager: FileSystemSchemaManager = get_schema_manager(
        # zone=g.irods_session.zone,
        zone=current_app.config["ZONE_NAME"],
        realm=realm,
    )
    logging.info(f"Using metadata schema {schema}")

    schema_as_json = schema_manager.load_schema(schema_name=schema, status="published")
    logging.info(schema_as_json)
    form_dict = {}
    flat_form_dict = {}
    if schema_as_json:
        form_dict = json.loads(schema_as_json)
        flat_form_dict = flatten_schema(
            ("", form_dict), level=0, prefix=prefix, result_dict={}
        )

    catalog_item = (
        # g.irods_session.data_objects.get(object_path)
        demo_data_object
        if item_type == "data_object"
        # else g.irods_session.collections.get(object_path)
        else demo_collection
    )
    setattr(catalog_item, "item_type", item_type)

    form_values = MultiDict()

    form_values.add("redirect_route", request.referrer + "#metadata")
    # add_to_dict(catalog_item.metadata.items(), form_values)
    add_to_dict(catalog_item.metadata, form_values)

    values_json = json.dumps(form_values.to_dict(flat=False))

    if request.method == "GET":
        return render_template(
            "schema_form_edit.html.j2",
            schema=schema,
            realm=realm,
            schema_values=base64.b64encode(bytes(values_json, "utf-8")).decode("utf-8"),
            prefix=prefix,
            item=catalog_item,
        )

    if request.method == "POST":
        """ """

        # remove all relevant attributes for this schema
        # remove operations:
        avu_operation_list = []
        # for meta_data_item in catalog_item.metadata.items():
        for meta_data_item in catalog_item.metadata:
            if meta_data_item.name.startswith(prefix):
                avu_operation_list.append(
                    # AVUOperation(operation="remove", avu=meta_data_item)
                    ("remove", meta_data_item)
                )
        for _key, _value in request.values.items(multi=True):
            if _key.startswith(prefix) and _value:
                if (
                    _key in flat_form_dict
                    and flat_form_dict[_key]["type"] == "textarea"
                ):
                    # the value is transformed to replace newlines as iRODS cannot handle this.
                    # Most likely this is only for schemas which can have textarea boxes
                    _value = "<br/>".join(_value.splitlines())

                if isinstance(_value, str):
                    _value = _value.strip()

                if "__" in _key and not _key.endswith("__"):
                    pprint(_key)
                    pprint(_key.split("__"))
                    _key, _unit = _key.split("__")
                    avu_operation_list.append(
                        # AVUOperation(operation="add", avu=iRODSMeta(_key, _value, _unit))
                        ("add", DemoAVU(_key, _value, _unit))
                    )
                else:
                    avu_operation_list.append(
                        # AVUOperation(operation="add", avu=iRODSMeta(_key, _value))
                        ("add", DemoAVU(_key, _value))
                    )

        # catalog_item.metadata.apply_atomic_operations(*avu_operation_list)
        catalog_item.apply_operations(avu_operation_list)
        # workaround for a bug in 4.2.11: only 'own' can execute atomic operations
        # lib.util.execute_atomic_operations(
        #     g.irods_session, catalog_item, avu_operation_list
        # )

        # if item_type == "collection":
        #     signals.collection_changed.send(
        #         current_app._get_current_object(),
        #         irods_session=g.irods_session,
        #         collection_path=object_path,
        #     )
        # if item_type == "data_object":
        #     signals.data_object_changed.send(
        #         current_app._get_current_object(),
        #         irods_session=g.irods_session,
        #         data_object_path=object_path,
        #     )

        # signals.data_object_changed(current_app._get_current_object(), data_object_path=data_object_path)

        # if item_type == "collection":
        #     referral = url_for(
        #         "browse_bp.collection_browse", collection=catalog_item.path
        #     )
        # else:
        #     referral = url_for(
        #         "browse_bp.view_object", data_object_path=catalog_item.path
        #     )
        referral = url_for("metadata_schema_view_bp.view_schema_metadata_for_item")

        if "redirect_route" in request.values:
            return redirect(request.values["redirect_route"])
        if "redirect_hash" in request.values:
            return redirect(referral.split("#")[0] + request.values["redirect_hash"])
        return redirect(request.referrer)


@metadata_schema_form_bp.route("/metadata-schema/delete-metadata", methods=["POST"])
def delete_schema_metadata_for_item():
    """ """
    form_parameters = request.values.to_dict()
    schema_identifier = form_parameters["schema_identifier"]
    item_path = form_parameters["item_path"]
    if not item_path.startswith("/"):
        item_path = "/" + item_path
    item_type = form_parameters["item_type"]

    catalog_item = (
        # g.irods_session.data_objects.get(item_path)
        demo_data_object
        if item_type == "data_object"
        # else g.irods_session.collections.get(item_path)
        else demo_collection
    )
    prefix = get_schema_prefix(schema_identifier=schema_identifier)

    avu_operation_list = []
    # for meta_data_item in catalog_item.metadata.items():
    for meta_data_item in catalog_item.metadata:
        if meta_data_item.name.startswith(prefix):
            avu_operation_list.append(
                # AVUOperation(operation="remove", avu=meta_data_item)
                ("remove", meta_data_item)
            )

    # catalog_item.metadata.apply_atomic_operations(*avu_operation_list)
    catalog_item.apply_operations(avu_operation_list)
    # workaround for a bug in 4.2.11
    # lib.util.execute_atomic_operations(
    #     g.irods_session, catalog_item, avu_operation_list
    # )

    # if item_type == "collection":
    #     signals.collection_changed.send(
    #         current_app._get_current_object(), collection_path=item_path
    #     )
    # if item_type == "data_object":
    #     signals.data_object_changed.send(
    #         current_app._get_current_object(), data_object_path=item_path
    #     )

    # if item_type == "collection":
    #     referral = url_for(
    #         "browse_bp.collection_browse",
    #         irods_session=g.irods_session,
    #         collection=catalog_item.path,
    #     )
    # else:
    #     referral = url_for(
    #         "browse_bp.view_object",
    #         irods_session=g.irods_session,
    #         data_object_path=catalog_item.path,
    #     )

    if "redirect_route" in request.values:
        return redirect(request.values["redirect_route"])
    # if "redirect_hash" in request.values:
    #     return redirect(referral.split("#")[0] + request.values["redirect_hash"])
    return redirect(request.referrer)

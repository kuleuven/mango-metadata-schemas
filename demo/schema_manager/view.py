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

from multidict import MultiDict

from slugify import slugify

from .editor import get_metadata_schema_dir
from .form import flatten_schema
from .demo_classes import demo_collection, demo_data_object

from . import (
    get_schema_manager,
    FileSystemSchemaManager,
)  # ??? HOW TO IMPORT IT
import logging


metadata_schema_view_bp = Blueprint(
    "metadata_schema_view_bp",
    __name__,
    template_folder="templates/metadata_schema",
)


def group_prefix_metadata_items(
    metadata_items,
    mango_prefix,
    no_schema_label="other",
    group_analysis_unit=False,
):
    """ """
    # grouped_metadata = {no_schema_label: MultiDict()}
    grouped_metadata = {}

    # if group_analysis_unit:
    #     grouped_metadata["analysis"] = MultiDict()
    def add_composite(parent, avu, i=3):
        name_sections = avu.name.split(".")
        unit_section = avu.units.split(".")
        composite_name = ".".join(name_sections[:i])
        composite_units = ".".join(unit_section[: (i - 2)])
        print("ADDING COMPOSITE: ", avu.name, i, composite_name, composite_units)
        if i < len(name_sections):
            if composite_name not in parent:
                parent[composite_name] = {composite_units: MultiDict()}
            if composite_units not in parent[composite_name]:
                parent[composite_name][composite_units] = MultiDict()
            add_composite(parent[composite_name][composite_units], avu, i + 1)
        else:
            parent.add(avu.name, avu)

    for avu in metadata_items:
        if avu.name.startswith(mango_prefix) and avu.name.count(".") >= 2:
            (mango_schema_prefix, schema, avu_name) = avu.name.split(".", 2)
            # item.name = meta_name
            if schema not in grouped_metadata:
                grouped_metadata[schema] = MultiDict()
            if not avu.units:
                grouped_metadata[schema].add(avu.name, avu)
            else:
                # creating a dict with the ordinal string from avu.unit as key
                # chop off the last part to get the composite identifier
                add_composite(grouped_metadata[schema], avu)

        # elif group_analysis_unit and avu.units and avu.units.startswith("analysis"):
        #     grouped_metadata["analysis"].add(avu.name, avu)
        # else:
        #     grouped_metadata[no_schema_label].add(avu.name, avu)
    # sort the non schema lists by key
    # grouped_metadata[no_schema_label] = MultiDict(
    #     sorted(grouped_metadata[no_schema_label].items(), key=itemgetter(0))
    # )
    # if "analysis" in grouped_metadata:
    #     grouped_metadata["analysis"] = MultiDict(
    #         sorted(grouped_metadata["analysis"].items(), key=itemgetter(0))
    #     )
    # if there are no consolidated metadata in the analysis group, delete the (empty) group
    # if group_analysis_unit and len(grouped_metadata["analysis"]) == 0:
    #     del grouped_metadata["analysis"]
    return grouped_metadata


@metadata_schema_view_bp.route("/metadata-schema/view")
def view_schema_metadata_for_item():
    data_object = demo_data_object
    schema_manager = get_schema_manager(
        current_app.config["ZONE_NAME"], current_app.config["REALM_NAME"]
    )
    schemas = schema_manager.list_schemas(filters=["published"])
    logging.info(f"Schema manager found schemas: {'|'.join(schemas.keys())}")
    grouped_metadata = group_prefix_metadata_items(
        # meta_data_items := data_object.metadata(timestamps=True).items(),
        data_object.metadata,
        current_app.config["MANGO_SCHEMA_PREFIX"],
    )  # find function
    schema_labels = {}

    for schema in grouped_metadata:  # schema_labels[schema][item.name]:
        try:
            if version := grouped_metadata[schema].get(
                f"{current_app.config['MANGO_SCHEMA_PREFIX']}.{schema}.__version__",
                "",
            ):
                schema_dict = json.loads(
                    schema_manager.load_schema(schema, status="", version=version.value)
                )
            else:
                schema_dict = json.loads(
                    schema_manager.load_schema(schema, status="published")
                )

            if schema_dict:
                schema_labels[schema] = flatten_schema(
                    ("", schema_dict),
                    level=0,
                    prefix=f"{current_app.config['MANGO_SCHEMA_PREFIX']}.{schema}",
                    result_dict={},
                )  # find function
            logging.info(f"Flattened schema {schema}: {schema_labels[schema]}")
        except:
            pass

    return render_template(
        "viewer.html.j2",
        data_object=data_object,
        grouped_metadata=grouped_metadata,
        schemas=schemas,
        schema_labels=schema_labels,
        realm=current_app.config["REALM_NAME"],
    )

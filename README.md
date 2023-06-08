Metadata schema manager
================

This repository contains Javascript code and a CSS file to render the
metadata schema manager for the ManGO portal, a web-based client for
iRODS. In this context, a metadata schema is a template aimed towards
the systematic application of metadata to iRODS data objects and
collections. The scope of this code is twofold: to support the design
and lifecycle management of metadata schemas and to generate a form
through which an user can assign metadata based on said schema.

On the one hand, the metadata schema manager allows to design a form,
choosing among different kinds of fields (simple input fields,
multiple-choice and even nested schemas, *aka* composite fields). The
templates for these forms, here called **schemas**, can go through
different stages, from drafts to published to archived versions. The
different fields, the lifecycle and the specifications of the JSON
format in which schemas are stored are described in [the documentation
files](docs/). On the other hand, some of the code meant for the manager
can also be used for the rendering of the form itself.

# Demo

If you want to run the demo, clone the repository, (create and activate
a virtual environment with **at least Python 3.10**), install the
required Python modules and run the Flask App:

``` sh
git clone git@github.com:kuleuven/mango-metadata-schemas.git
cd mdschema-editor
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cd demo
flask run
```

The demo will be available in <http://127.0.0.1:5000>.

Once you have done this once, the following times you only need to
activate the virtual environment and run flask:

``` sh
# from mdschema-editor
. venv/bin/activate
cd demo
flask run
```

# Other resources

- A [Python package](https://github.com/kuleuven/mango-schema-validator)
  to validate metadata based on a ManGO metadata schema.

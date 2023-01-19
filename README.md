# Metadata schema editor

This repository contains Javascript code and a CSS file to render a metadata schema editor. The editor was designed for the ManGO portal.

The goal of this editor is to be able to design forms for metadata schema implementation.
If you want a web-interface that offers forms to assign metadata to data objects, you may want to organize the desired metadata based on pre-defined schemas, which contain desired fields, their possible formats and sometimes even their possible values. This can be implemented by designing a form with text/numeric input fields, radio buttons, checkboxes, dropdowns and even meaningful combinations of the above. The metadata schema editor allows to design the form, choosing the kinds of fields that suit your needs, assigning them IDs and labels and setting different properties, such as the kind of input for the text input fields (free text, e-mails, integers, floats...) and the selection of values for radios, checkboxes and dropdowns. Fields can be marked as required and both input fields and objects (i.e. combinations of fields) can be marked as repeatable.
The output is then stored as a json file with the format of the "basic.json" example.

For information on the output format, check the documents in the "doc" folder of this repository.

## How to use

The Javascript code in this repository needs to be hooked to a DOM element (typically a `<div>`) with the id "metadata_template_list_container". This is defined in "src/init.js".
It also assumes that there is a custom tag "url-list" with a few custom fields that contain the urls to retrieve lists of existing metadata schemas and to save/update schemas.

The code in "src/init.js" reads the contents of this tag and stores the values of the urls in a `urls` object, which should have at least a `list` and a `new` item containing, respectively, the url to retrieve the list of existing metadata schema and the url to save new schemas or update existing ones. These urls are then used by the `Schema()` and `TemplatesRequest()` calls in the same file.

In other words, you could also provide the urls as an object by editing the code in "init.js" and providing your custom `urls` object to these calls.

All the Javascript files should be included in your HTML:

```html
<script src="doms.js"></script>
<script src="fields.js"></script>
<script src="schema.js"></script>
<script src="httprequests.js"></script>
<script src="init.js"></script>
```

Or, for example, given a Jinja2 template:

```jinja2
{% for file in ['doms', 'fields', 'schema', 'httprequests', 'init'] %}
    <script src="{{'dist/{}.js'.format(file)}}"></script>
{% endfor %}
```

# Structure of the Javascript files

The only file that actually runs code is "src/init.js", which hooks to the DOM elements and creates everything you will see. It also creates a `Schema()` instance for the new schema you may want to design and a `TemplatesRequest()` class, which retrieves the list of existing schemas and then renders them.

The rest of the files define different classes then instantiated through the workflow.

## doms.js

The DOMs file contains a number of classes that programmatically generate and manipulate DOM elements.

- The `Field` class only contains static elements that can be reused.

- The `MovingField` class defines a box with an input field and buttons to move it up and down; it has the `MovingViewer` and `MovingChoice` subclasses which are used, respectively, for viewing created fields (and reordering them) and for defining the options in a multiple-choice field.

- The `BasicForm` class sets up the common aspects to the forms that design the different fields, such as inputs and labels, switches and buttons.

- The `Modal` and `AccordionItem` classes help create modals (to create forms) and accordion items (to create, view and edit schemas).

## fields.js

The Fields file contains a parent class called `InputField` that sets up the common ground for all kinds of fields that can be designed. It includes important attributes and methods to select them, design them, view them, edit them and retrieve information from their forms.

Its three main children are `TypedInput`, `MultipleInput` and `ObjectInput`, which are used to create scalar inputs (text, numbers...), multiple-choice inputs (radio and checkbox, dropdowns...) and objects (combinations of other kinds of inputs). The `MultipleInput` subclass has two further children: `SelectInput` for when only one of the possible answers can be selected, and `CheckboxInput` for when many of the possible answers can be selected. Both can be eventually rendered as dropdowns, but their alternative shapes are different: radio buttons for the former and checkbox for the latter.

## schema.js

The Schema file contains a parent class `ComplexField` with two children: `ObjectEditor` and `Schema`. Since Object fields are basically mini schemas, their creation, edition and rendering should be very similar. `ComplexField` gathers their commonalities, whereas the subclasses specify what is particular for objects and schemas respectively.

## httprequests.js

The HttpRequests file contains a class that extends `XMLHttpRequest`, `MangoRequest`, with two children: `TemplatesRequest` and `TemplateReader`. These classes are used to retrieve information from the server: the list of existing templates and individual templates, respectively.

For the moment, no such class is used for posting information to the server side.


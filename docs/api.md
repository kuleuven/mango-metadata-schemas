## Classes

<dl>
<dt><a href="#Field">Field</a></dt>
<dd><p>Class for HTML DOM utilities. Only static methods.</p>
</dd>
<dt><a href="#MovingField">MovingField</a></dt>
<dd><p>Class representing a form element or field that can move up and down among others of its kind.</p>
</dd>
<dt><a href="#MovingViewer">MovingViewer</a> ⇐ <code><a href="#MovingField">MovingField</a></code></dt>
<dd><p>Class representing box to view and edit an input field when editing a schema.</p>
</dd>
<dt><a href="#MovingChoice">MovingChoice</a> ⇐ <code><a href="#MovingField">MovingField</a></code></dt>
<dd><p>Class representing a moving input field to design options in a dropdown, checkbox or radio field.</p>
</dd>
<dt><a href="#BasicForm">BasicForm</a></dt>
<dd><p>Class for forms used when editing a schema or field.</p>
</dd>
<dt><a href="#SchemaDraftForm">SchemaDraftForm</a> ⇐ <code><a href="#BasicForm">BasicForm</a></code></dt>
<dd><p>Class for forms used when editing a schema (draft).
It includes hidden inputs that are not included in its parent class.</p>
</dd>
<dt><a href="#Modal">Modal</a></dt>
<dd><p>Class to create a standard BS5 Modal, typically containing a form to edit a Schema or InputField.</p>
</dd>
<dt><a href="#AccordionItem">AccordionItem</a></dt>
<dd><p>Class to create a standard BS5 Accordion Item, in which the information of a given schema
and all its versions will be displayed.</p>
</dd>
<dt><a href="#NavBar">NavBar</a></dt>
<dd><p>Class to create a navigation bar with pills or tabs.
This is used to display the different versions of a schema, with tabs that have badges,
and to switch between views and editors within a version of a schema.</p>
</dd>
<dt><a href="#InputField">InputField</a></dt>
<dd><p>Master class to represent input fields. Only the child classes are actually instantiated.</p>
</dd>
<dt><a href="#TypedInput">TypedInput</a> ⇐ <code><a href="#InputField">InputField</a></code></dt>
<dd><p>Class representing a simple field.
Its <code>form_type</code> is always &quot;text&quot;, whereas its <code>type</code> refers to one of many possible input options.
Its <code>button_title</code> is &quot;Simple field&quot; and its <code>description</code> includes the many input options.</p>
</dd>
<dt><a href="#ObjectInput">ObjectInput</a> ⇐ <code><a href="#InputField">InputField</a></code></dt>
<dd><p>Class representing a composite field
Its <code>form_type</code> is always &quot;object&quot;, like its <code>type</code>.
Its <code>button_title</code> is &quot;Composite field&quot; and its description is a brief summary.</p>
</dd>
<dt><a href="#MultipleInput">MultipleInput</a> ⇐ <code><a href="#InputField">InputField</a></code></dt>
<dd><p>Class representing a multiple-choice field.
Its <code>form_type</code> depends on the subclass; its <code>type</code> is always &quot;select&quot;.
Its <code>button_title</code> depends on the subclass.</p>
</dd>
<dt><a href="#SelectInput">SelectInput</a> ⇐ <code><a href="#MultipleInput">MultipleInput</a></code></dt>
<dd><p>Class representing a single-value multiple-choice field.
Its <code>form_type</code> is always &quot;selection&quot;; its <code>type</code> remains &quot;select&quot;.
Its <code>button_type</code> is always &quot;Single-value multiple choice&quot;.
Its <code>values.multiple</code> property is always &quot;false&quot;; its <code>values.ui</code> property can only be &quot;dropdown&quot; or &quot;radio&quot;.</p>
</dd>
<dt><a href="#CheckboxInput">CheckboxInput</a> ⇐ <code><a href="#MultipleInput">MultipleInput</a></code></dt>
<dd><p>Class representing a multiple-value multiple-choice field.
Its <code>form_type</code> is always &quot;checkbox&quot;; its <code>type</code> remains &quot;select&quot;.
Its <code>button_type</code> is always &quot;Multiple-value multiple choice&quot;.
Its <code>values.multiple</code> property is always &quot;true&quot;; its <code>values.ui</code> property can only be &quot;dropdown&quot; or &quot;checkbox&quot;.</p>
</dd>
<dt><a href="#MangoRequest">MangoRequest</a> ⇐ <code>XMLHttpRequest</code></dt>
<dd><p>Abstract class to handle GET requests</p>
</dd>
<dt><a href="#TemplatesRequest">TemplatesRequest</a> ⇐ <code><a href="#MangoRequest">MangoRequest</a></code></dt>
<dd><p>Class representing a request for a list of schemas.</p>
</dd>
<dt><a href="#TemplateReader">TemplateReader</a></dt>
<dd><p>Class representing a request for a schema (to manage).</p>
</dd>
<dt><a href="#AnnotationRequest">AnnotationRequest</a> ⇐ <code><a href="#MangoRequest">MangoRequest</a></code></dt>
<dd><p>Class representing a request for a schema for annotation.</p>
</dd>
<dt><a href="#ComplexField">ComplexField</a></dt>
<dd><p>Master class to represent schemas and mini-schemas. Only the child classes are actually instantiated.</p>
</dd>
<dt><a href="#DummyObject">DummyObject</a> ⇐ <code><a href="#ComplexField">ComplexField</a></code></dt>
<dd><p>Class for illustration of an ObjectEditor.
It has three fixed IDs to illustrate: a simple text input, a simple date input and a radio.</p>
</dd>
<dt><a href="#ObjectEditor">ObjectEditor</a> ⇐ <code><a href="#ComplexField">ComplexField</a></code></dt>
<dd><p>Class for mini-schemas connected to a composite field.
<code>data_status</code> always starts with &#39;object&#39;, followed by the <code>data_status</code>
of the schema that the composite field belongs to.</p>
</dd>
<dt><a href="#Schema">Schema</a> ⇐ <code><a href="#ComplexField">ComplexField</a></code></dt>
<dd><p>Class for a version of a schema.</p>
</dd>
<dt><a href="#SchemaGroup">SchemaGroup</a></dt>
<dd><p>Class for a schema with all its versions, to render on the page.</p>
</dd>
<dt><a href="#SchemaForm">SchemaForm</a></dt>
<dd><p>Class for a published version of a schema to be used when applying metadata.</p>
</dd>
</dl>

## Members

<dl>
<dt><a href="#url_tag">url_tag</a> : <code>HTMLElement</code></dt>
<dd><p>DOM element containing the information for the list ofr URLs.</p>
</dd>
<dt><a href="#urls">urls</a> : <code><a href="#UrlsList">UrlsList</a></code></dt>
<dd></dd>
<dt><a href="#schema_pattern">schema_pattern</a> : <code>String</code></dt>
<dd><p>REGEX Pattern to control possible schema names. This pattern is then filled with existing names.</p>
</dd>
<dt><a href="#starting_schema">starting_schema</a> : <code><a href="#Schema">Schema</a></code></dt>
<dd><p>Empty schema to start with.</p>
</dd>
</dl>

## Constants

<dl>
<dt><a href="#container_id">container_id</a> : <code>String</code></dt>
<dd><p>ID of the DOM element to hook the form to.</p>
</dd>
<dt><a href="#container">container</a> : <code>HTMLElement</code></dt>
<dd><p>DOM element to hook the form to. It should also have several attributes with necessary info.</p>
</dd>
<dt><a href="#container_id">container_id</a> : <code>String</code></dt>
<dd><p>ID of the DOM element to which all the code will be hooked.</p>
</dd>
<dt><a href="#container">container</a> : <code>HTMLDivElement</code></dt>
<dd><p>DOM element to which all the code will be hooked. The BS5 class &#39;accordion&#39; is enforced.</p>
</dd>
<dt><a href="#schemas">schemas</a> : <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code></dt>
<dd><p>Register of existing schemas</p>
</dd>
</dl>

## Typedefs

<dl>
<dt><a href="#FieldInfo">FieldInfo</a> : <code>Object</code></dt>
<dd><p>Representation of a field to be saved as JSON.</p>
</dd>
<dt><a href="#SchemaInfo">SchemaInfo</a> : <code>Object</code></dt>
<dd><p>Information about a schema from the backend.</p>
</dd>
<dt><a href="#SchemaContents">SchemaContents</a> : <code>Object</code></dt>
<dd><p>JSON representation of a schema.</p>
</dd>
<dt><a href="#UrlsList">UrlsList</a> : <code>Object</code></dt>
<dd><p>Collection of URLS to communicate with the backend.</p>
</dd>
</dl>

<a name="Field"></a>

## Field
Class for HTML DOM utilities. Only static methods.

**Kind**: global class  

* [Field](#Field)
    * _instance_
        * [.example_values](#Field+example_values) : <code>Array.&lt;String&gt;</code>
    * _static_
        * [.quick(tag, class_name, [inner])](#Field.quick) ⇒ <code>HTMLElement</code>
        * [.dropdown(field, [active])](#Field.dropdown) ⇒ <code>HTMLElement</code>
        * [.checkbox_radio(field, [active])](#Field.checkbox_radio) ⇒ <code>HTMLElement</code>
        * [.labeller(label_text, input_id)](#Field.labeller) ⇒ <code>HTMLElement</code>
        * [.include_value(field)](#Field.include_value) ⇒

<a name="Field+example_values"></a>

### field.example\_values : <code>Array.&lt;String&gt;</code>
Example values for example dropdowns/checkboxes/radios

**Kind**: instance property of [<code>Field</code>](#Field)  
<a name="Field.quick"></a>

### Field.quick(tag, class_name, [inner]) ⇒ <code>HTMLElement</code>
Create an HTML element with a certain class and maybe text.

**Kind**: static method of [<code>Field</code>](#Field)  
**Returns**: <code>HTMLElement</code> - An HTML element with the provided tag name, class and (optionally) internal text.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| tag | <code>String</code> |  | Tag Name for the HTML element. |
| class_name | <code>String</code> |  | Class name for the HTML element. |
| [inner] | <code>String</code> | <code></code> | Text to be added inside the HTML element. |

<a name="Field.dropdown"></a>

### Field.dropdown(field, [active]) ⇒ <code>HTMLElement</code>
Create a BS5 Select input.

**Kind**: static method of [<code>Field</code>](#Field)  
**Returns**: <code>HTMLElement</code> - A dropdown (select input).  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| field | [<code>MultipleInput</code>](#MultipleInput) |  | Input field to build a dropdown upon. |
| [active] | <code>Boolean</code> | <code>false</code> | Whether it will be used for annotation. |

<a name="Field.checkbox_radio"></a>

### Field.checkbox\_radio(field, [active]) ⇒ <code>HTMLElement</code>
Create a BS5 checkbox or radio input.

**Kind**: static method of [<code>Field</code>](#Field)  
**Returns**: <code>HTMLElement</code> - A checkbox or radio input.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| field | [<code>MultipleInput</code>](#MultipleInput) |  | Input field to build a dropdown upon. |
| [active] | <code>Boolean</code> | <code>false</code> | Whether it will be used for annotation. |

<a name="Field.labeller"></a>

### Field.labeller(label_text, input_id) ⇒ <code>HTMLElement</code>
Quickly create a label for an input field.

**Kind**: static method of [<code>Field</code>](#Field)  
**Returns**: <code>HTMLElement</code> - A label for an input field.  

| Param | Type | Description |
| --- | --- | --- |
| label_text | <code>String</code> | Text for the input label. |
| input_id | <code>String</code> | ID of the input this label describes. |

<a name="Field.include_value"></a>

### Field.include\_value(field) ⇒
Check if a value has been provided for a field, or otherwise a default, and retrieve it.

**Kind**: static method of [<code>Field</code>](#Field)  
**Returns**: An existing value, or a default value, or nothing.  

| Param | Type | Description |
| --- | --- | --- |
| field | [<code>InputField</code>](#InputField) | Field from which the value will be extracted |

<a name="MovingField"></a>

## MovingField
Class representing a form element or field that can move up and down among others of its kind.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| idx | <code>String</code> \| <code>Number</code> | Index or identifier of this field in relation to its siblings. |
| up | <code>HTMLButtonElement</code> | Button used to move the field one slot up. |
| down | <code>HTMLButtonElement</code> | Button used to move the field one slot down. |


* [MovingField](#MovingField)
    * [new MovingField(idx)](#new_MovingField_new)
    * *[.move_up()](#MovingField+move_up)*
    * *[.move_down()](#MovingField+move_down)*
    * [.add_btn(className, symbol, [action])](#MovingField+add_btn) ⇒ <code>HTMLButtonElement</code>

<a name="new_MovingField_new"></a>

### new MovingField(idx)
Initiate a moving field.


| Param | Type | Description |
| --- | --- | --- |
| idx | <code>String</code> \| <code>Number</code> | Index or identifier of this field in relation to its siblings. |

<a name="MovingField+move_up"></a>

### *movingField.move\_up()*
Move the field one slot up.

**Kind**: instance abstract method of [<code>MovingField</code>](#MovingField)  
<a name="MovingField+move_down"></a>

### *movingField.move\_down()*
Move the field one slot down.

**Kind**: instance abstract method of [<code>MovingField</code>](#MovingField)  
<a name="MovingField+add_btn"></a>

### movingField.add\_btn(className, symbol, [action]) ⇒ <code>HTMLButtonElement</code>
Create a button for the Moving Field.

**Kind**: instance method of [<code>MovingField</code>](#MovingField)  
**Returns**: <code>HTMLButtonElement</code> - The button to be added.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| className | <code>String</code> |  | Class name for the button indicating its function ('up', 'down', 'edit'...). |
| symbol | <code>String</code> |  | Name of the Bootstrap Icon symbol to use in the button ('arrow-up-circle', 'arrow-down-circle'...). |
| [action] | <code>function</code> | <code>false</code> | What the button must do on click. If 'false', nothing happens. |

<a name="MovingViewer"></a>

## MovingViewer ⇐ [<code>MovingField</code>](#MovingField)
Class representing box to view and edit an input field when editing a schema.

**Kind**: global class  
**Extends**: [<code>MovingField</code>](#MovingField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| title | <code>String</code> | Title of the box (title of the field, with asterisk if required). |
| repeatable | <code>Boolean</code> | Whether the field is repeatable. |
| div | <code>HTMLElement</code> | Box containing the title, example and buttons. |
| body | <code>HTMLElement</code> | Example input field, showing what the field looks like. |
| parent_modal | <code>bootstrap.Modal</code> | If the field is inside a composite field, the composite field's editor modal. |
| rem | <code>HTMLButtonElement</code> | Button used to remove the field. |
| copy | <code>HTMLButtonElement</code> | Button to duplicate the field. |
| edit | <code>HTMLButtonElement</code> | Button to edit the field. |
| schema | [<code>ComplexField</code>](#ComplexField) | The schema (or mini-schema of composite field) to which the field belongs. |
| below | <code>HTMLButtonElement</code> | Button under the field used to add a new field under it. It moves along with the field. |


* [MovingViewer](#MovingViewer) ⇐ [<code>MovingField</code>](#MovingField)
    * [new MovingViewer(form, schema)](#new_MovingViewer_new)
    * [.duplicate(form)](#MovingViewer+duplicate)
    * [.assemble()](#MovingViewer+assemble)
    * [.move_down()](#MovingViewer+move_down)
    * [.move_up()](#MovingViewer+move_up)
    * [.remove()](#MovingViewer+remove)
    * [.add_btn(className, symbol, [action])](#MovingField+add_btn) ⇒ <code>HTMLButtonElement</code>

<a name="new_MovingViewer_new"></a>

### new MovingViewer(form, schema)
Create a box to show and allow editing / placement / removal / duplication of a field.


| Param | Type | Description |
| --- | --- | --- |
| form | [<code>InputField</code>](#InputField) | Field to be edited. |
| schema | [<code>ComplexField</code>](#ComplexField) | Schema or mini-schema of a composite field to which the field belongs. |

<a name="MovingViewer+duplicate"></a>

### movingViewer.duplicate(form)
Create a duplicate of a field with empty ID.
Until the duplicate has a new ID, the (mini-)schema cannot be saved or published.
The duplicate itself cannot be copied (the button is disabled) and the "edit" button is highlighted.

**Kind**: instance method of [<code>MovingViewer</code>](#MovingViewer)  

| Param | Type | Description |
| --- | --- | --- |
| form | [<code>InputField</code>](#InputField) | Field to duplicate / copy / clone. |

<a name="MovingViewer+assemble"></a>

### movingViewer.assemble()
Construct and fill the HTML Element.

**Kind**: instance method of [<code>MovingViewer</code>](#MovingViewer)  
<a name="MovingViewer+move_down"></a>

### movingViewer.move\_down()
Move the viewer down one slot.
This method is called when the 'down' button is clicked on,
which is disabled if this is the last viewer in the sequence of viewers.

**Kind**: instance method of [<code>MovingViewer</code>](#MovingViewer)  
**Overrides**: [<code>move\_down</code>](#MovingField+move_down)  
<a name="MovingViewer+move_up"></a>

### movingViewer.move\_up()
Move the viewer up one slot.
This method is called when the 'up' button is clicked on,
which is disabled if this is the first viewer in the sequence of viewers.

**Kind**: instance method of [<code>MovingViewer</code>](#MovingViewer)  
**Overrides**: [<code>move\_up</code>](#MovingField+move_up)  
<a name="MovingViewer+remove"></a>

### movingViewer.remove()
Remove the viewer (and the field linked to it).
This method is called when the 'rem' button is clicked on, but nothing really happens unless the
confirmation modal triggered by it is accepted.

**Kind**: instance method of [<code>MovingViewer</code>](#MovingViewer)  
<a name="MovingField+add_btn"></a>

### movingViewer.add\_btn(className, symbol, [action]) ⇒ <code>HTMLButtonElement</code>
Create a button for the Moving Field.

**Kind**: instance method of [<code>MovingViewer</code>](#MovingViewer)  
**Overrides**: [<code>add\_btn</code>](#MovingField+add_btn)  
**Returns**: <code>HTMLButtonElement</code> - The button to be added.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| className | <code>String</code> |  | Class name for the button indicating its function ('up', 'down', 'edit'...). |
| symbol | <code>String</code> |  | Name of the Bootstrap Icon symbol to use in the button ('arrow-up-circle', 'arrow-down-circle'...). |
| [action] | <code>function</code> | <code>false</code> | What the button must do on click. If 'false', nothing happens. |

<a name="MovingChoice"></a>

## MovingChoice ⇐ [<code>MovingField</code>](#MovingField)
Class representing a moving input field to design options in a dropdown, checkbox or radio field.

**Kind**: global class  
**Extends**: [<code>MovingField</code>](#MovingField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| div | <code>HTMLElement</code> | Div containing the input field and the buttons. |
| sub_div | <code>HTMLElement</code> | Div that contains the input field only. |
| label | <code>HTMLElement</code> | Label for the input ("Select option"). |
| input_tag | <code>HTMLElement</code> | Input field |
| [value] | <code>String</code> | The value of the input field, or 'false' if it doesn't exist. |
| rem | <code>HTMLButtonElement</code> | Button used to remove the field. |


* [MovingChoice](#MovingChoice) ⇐ [<code>MovingField</code>](#MovingField)
    * [new MovingChoice(label_text, idx, [value])](#new_MovingChoice_new)
    * _instance_
        * [.assemble()](#MovingChoice+assemble)
        * [.add_input()](#MovingChoice+add_input) ⇒ <code>HTMLElement</code>
        * [.move_down()](#MovingChoice+move_down)
        * [.move_up()](#MovingChoice+move_up)
        * [.remove()](#MovingChoice+remove)
        * [.add_btn(className, symbol, [action])](#MovingField+add_btn) ⇒ <code>HTMLButtonElement</code>
    * _static_
        * [.remove_div(div)](#MovingChoice.remove_div)

<a name="new_MovingChoice_new"></a>

### new MovingChoice(label_text, idx, [value])
Initiate a moving field in which to define an option for a dropdown, checkbox or radio.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the input (e.g. "Select option"). |
| idx | <code>Number</code> |  | Index of this field as it gets created. |
| [value] | <code>String</code> | <code>false</code> | Value of the input field, or 'false' if it doesn't exist. |

<a name="MovingChoice+assemble"></a>

### movingChoice.assemble()
Bring everything together (append the sub elements to the main HTML Element) in the right order.

**Kind**: instance method of [<code>MovingChoice</code>](#MovingChoice)  
<a name="MovingChoice+add_input"></a>

### movingChoice.add\_input() ⇒ <code>HTMLElement</code>
Create an input field for a new option.

**Kind**: instance method of [<code>MovingChoice</code>](#MovingChoice)  
**Returns**: <code>HTMLElement</code> - Input field to define the value of the option.  
<a name="MovingChoice+move_down"></a>

### movingChoice.move\_down()
Move the option down one slot.
This method is called when the 'down' button is clicked on,
which is disabled if this is the last option in the sequence.

**Kind**: instance method of [<code>MovingChoice</code>](#MovingChoice)  
**Overrides**: [<code>move\_down</code>](#MovingField+move_down)  
<a name="MovingChoice+move_up"></a>

### movingChoice.move\_up()
Move the option up one slot.
This method is called when the 'up' button is clicked on,
which is disabled if this is the first option in the sequence.

**Kind**: instance method of [<code>MovingChoice</code>](#MovingChoice)  
**Overrides**: [<code>move\_up</code>](#MovingField+move_up)  
<a name="MovingChoice+remove"></a>

### movingChoice.remove()
Remove this option.
This method is called when the 'rem' button is clicked on,
which is disabled if there are only two options.

**Kind**: instance method of [<code>MovingChoice</code>](#MovingChoice)  
<a name="MovingField+add_btn"></a>

### movingChoice.add\_btn(className, symbol, [action]) ⇒ <code>HTMLButtonElement</code>
Create a button for the Moving Field.

**Kind**: instance method of [<code>MovingChoice</code>](#MovingChoice)  
**Overrides**: [<code>add\_btn</code>](#MovingField+add_btn)  
**Returns**: <code>HTMLButtonElement</code> - The button to be added.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| className | <code>String</code> |  | Class name for the button indicating its function ('up', 'down', 'edit'...). |
| symbol | <code>String</code> |  | Name of the Bootstrap Icon symbol to use in the button ('arrow-up-circle', 'arrow-down-circle'...). |
| [action] | <code>function</code> | <code>false</code> | What the button must do on click. If 'false', nothing happens. |

<a name="MovingChoice.remove_div"></a>

### MovingChoice.remove\_div(div)
Remove a Moving Choice. This is a static method because it is also called from outside
when resetting the form it belongs to.

**Kind**: static method of [<code>MovingChoice</code>](#MovingChoice)  

| Param | Type | Description |
| --- | --- | --- |
| div | <code>HTMLDivElement</code> | A DIV element from a MovingChoice to be removed from the form. |

<a name="BasicForm"></a>

## BasicForm
Class for forms used when editing a schema or field.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| form | <code>HTMLFormElement</code> | The 'form' element itself, with BS5 validation. |
| option_indices | <code>Array.&lt;Number&gt;</code> | List of indices of moving fields (if relevant). |
| divider | <code>HTMLHRElement</code> | An 'hr' element to split the form content from the submission buttons. |
| rowsub | <code>HTMLDivElement</code> | A 'div' element with class 'row' that contains the submission buttons. |
| switches | <code>HTMLDivElement</code> | A 'div' element with switches (e.g. 'required', 'repeatable'). |


* [BasicForm](#BasicForm)
    * [new BasicForm(id)](#new_BasicForm_new)
    * [.add_input(label_text, input_id, [description], [placeholder], [value], [validation_message], [pattenr], [required])](#BasicForm+add_input)
    * [.add_select(label_text, select_id, options, [selected])](#BasicForm+add_select)
    * [.add_mover(label_text, idx, value)](#BasicForm+add_mover) ⇒ [<code>MovingChoice</code>](#MovingChoice)
    * [.add_moving_options(label_text, [starting_values])](#BasicForm+add_moving_options)
    * [.add_switches(id, switchnames, [required], [repeatable], [dropdown])](#BasicForm+add_switches)
    * [.add_action_button(text, id, color)](#BasicForm+add_action_button)
    * [.add_submit_action(id, action)](#BasicForm+add_submit_action)
    * [.reset()](#BasicForm+reset)

<a name="new_BasicForm_new"></a>

### new BasicForm(id)
Initialize a standard form.


| Param | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | ID of the field or schema this form is used to edit. |

<a name="BasicForm+add_input"></a>

### basicForm.add\_input(label_text, input_id, [description], [placeholder], [value], [validation_message], [pattenr], [required])
Create a text input element for the form and insert it before the divider or, if they exist, the switches.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the input field. |
| input_id | <code>String</code> |  | ID of the input field. |
| [description] | <code>String</code> \| <code>Boolean</code> | <code>false</code> | A description for the input field. |
| [placeholder] | <code>String</code> | <code>&quot;Some text&quot;</code> | A placeholder for the input field. |
| [value] | <code>String</code> \| <code>Boolean</code> | <code>false</code> | Value to fill into the input field, if it exists. |
| [validation_message] | <code>String</code> | <code>&quot;This field is compulsory&quot;</code> | Message to show when the input field does not fulfill the validation criteria on form submission. |
| [pattenr] | <code>String</code> | <code>&quot;.*&quot;</code> | A regular expression that the (text) input field must match to be accepted on submission. |
| [required] | <code>Boolean</code> | <code>true</code> | Whether the input field should be required. |

<a name="BasicForm+add_select"></a>

### basicForm.add\_select(label_text, select_id, options, [selected])
Create and append a dropdown before the divider.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the dropdown. |
| select_id | <code>String</code> |  | ID for the dropdown. |
| options | <code>Array.&lt;String&gt;</code> |  | Options for the dropdown. |
| [selected] | <code>String</code> \| <code>Boolean</code> | <code>false</code> | Selected option, if any. |

<a name="BasicForm+add_mover"></a>

### basicForm.add\_mover(label_text, idx, value) ⇒ [<code>MovingChoice</code>](#MovingChoice)
Create and append a moving input field (when creating options for multiple-choice fields).

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  
**Returns**: [<code>MovingChoice</code>](#MovingChoice) - Moving input field.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the input field (e.g. "Select option"). |
| idx | <code>Number</code> |  | Index of the mover in order of creation. |
| value | <code>String</code> \| <code>Boolean</code> | <code>false</code> | Value of the input field in the mover, if it exists. |

<a name="BasicForm+add_moving_options"></a>

### basicForm.add\_moving\_options(label_text, [starting_values])
Initialize a series of moving choice fields, when first generating a form
for a MultipleInput field.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  

| Param | Type | Description |
| --- | --- | --- |
| label_text | <code>String</code> | Text for the label of the input fields (e.g. "Select option"). |
| [starting_values] | <code>Array.&lt;(String\|Number)&gt;</code> | Initial values for the moving fields. |

<a name="BasicForm+add_switches"></a>

### basicForm.add\_switches(id, switchnames, [required], [repeatable], [dropdown])
Create and append a DIV element that contains switches to define boolean values of an InputField.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| id | <code>String</code> |  | ID of the field to which the form belongs. |
| switchnames | <code>Array.&lt;String&gt;</code> |  | Names of the switches to add. Possible values inside are 'required', 'repeatable' and 'dropdown'. |
| [required] | <code>Boolean</code> | <code>false</code> | Default value of the 'required' switch, i.e. whether the InputField is required. |
| [repeatable] | <code>Boolean</code> | <code>false</code> | Default value of the 'repeatable' switch, i.e. whether the InputField is repeatable. |
| [dropdown] | <code>Boolean</code> | <code>false</code> | Default value of the 'dropdown' switch, i.e. whether the MultipleInput will be rendered as a dropdown. |

<a name="BasicForm+add_action_button"></a>

### basicForm.add\_action\_button(text, id, color)
Create and append a button for submission.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| text | <code>String</code> |  | Text in the action button. |
| id | <code>String</code> | <code>draft</code> | ID for the button. |
| color | <code>String</code> | <code>success</code> | Color class for the button, e.g. 'success', 'danger'... |

<a name="BasicForm+add_submit_action"></a>

### basicForm.add\_submit\_action(id, action)
Add an action on submission of the form, depending on the button that is clicked.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  

| Param | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | ID of the button that will trigger this action. |
| action | <code>function</code> | Action to execute when clicking on the button. |

<a name="BasicForm+reset"></a>

### basicForm.reset()
Reset the form, uncheck boxes, remove the 'was-validated' class.

**Kind**: instance method of [<code>BasicForm</code>](#BasicForm)  
<a name="SchemaDraftForm"></a>

## SchemaDraftForm ⇐ [<code>BasicForm</code>](#BasicForm)
Class for forms used when editing a schema (draft).
It includes hidden inputs that are not included in its parent class.

**Kind**: global class  
**Extends**: [<code>BasicForm</code>](#BasicForm)  

* [SchemaDraftForm](#SchemaDraftForm) ⇐ [<code>BasicForm</code>](#BasicForm)
    * [new SchemaDraftForm(schema)](#new_SchemaDraftForm_new)
    * [.add_hidden_field(name, value)](#SchemaDraftForm+add_hidden_field)
    * [.update_field(name, value)](#SchemaDraftForm+update_field)
    * [.add_input(label_text, input_id, [description], [placeholder], [value], [validation_message], [pattenr], [required])](#BasicForm+add_input)
    * [.add_select(label_text, select_id, options, [selected])](#BasicForm+add_select)
    * [.add_mover(label_text, idx, value)](#BasicForm+add_mover) ⇒ [<code>MovingChoice</code>](#MovingChoice)
    * [.add_moving_options(label_text, [starting_values])](#BasicForm+add_moving_options)
    * [.add_switches(id, switchnames, [required], [repeatable], [dropdown])](#BasicForm+add_switches)
    * [.add_action_button(text, id, color)](#BasicForm+add_action_button)
    * [.add_submit_action(id, action)](#BasicForm+add_submit_action)
    * [.reset()](#BasicForm+reset)

<a name="new_SchemaDraftForm_new"></a>

### new SchemaDraftForm(schema)
Initialize a form to edit a schema.


| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | A schema to edit via this form. |

<a name="SchemaDraftForm+add_hidden_field"></a>

### schemaDraftForm.add\_hidden\_field(name, value)
Create a new hidden field and attach to the form.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  

| Param | Type | Description |
| --- | --- | --- |
| name | <code>String</code> | Value of the 'name' attribute of the form input. |
| value | <code>String</code> | Value of the form input. |

<a name="SchemaDraftForm+update_field"></a>

### schemaDraftForm.update\_field(name, value)
Update an existing field of the form with a new value.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  

| Param | Type | Description |
| --- | --- | --- |
| name | <code>String</code> | Value of the 'name' attribute of the form input. |
| value | <code>String</code> | Value of the form input. |

<a name="BasicForm+add_input"></a>

### schemaDraftForm.add\_input(label_text, input_id, [description], [placeholder], [value], [validation_message], [pattenr], [required])
Create a text input element for the form and insert it before the divider or, if they exist, the switches.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_input</code>](#BasicForm+add_input)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the input field. |
| input_id | <code>String</code> |  | ID of the input field. |
| [description] | <code>String</code> \| <code>Boolean</code> | <code>false</code> | A description for the input field. |
| [placeholder] | <code>String</code> | <code>&quot;Some text&quot;</code> | A placeholder for the input field. |
| [value] | <code>String</code> \| <code>Boolean</code> | <code>false</code> | Value to fill into the input field, if it exists. |
| [validation_message] | <code>String</code> | <code>&quot;This field is compulsory&quot;</code> | Message to show when the input field does not fulfill the validation criteria on form submission. |
| [pattenr] | <code>String</code> | <code>&quot;.*&quot;</code> | A regular expression that the (text) input field must match to be accepted on submission. |
| [required] | <code>Boolean</code> | <code>true</code> | Whether the input field should be required. |

<a name="BasicForm+add_select"></a>

### schemaDraftForm.add\_select(label_text, select_id, options, [selected])
Create and append a dropdown before the divider.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_select</code>](#BasicForm+add_select)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the dropdown. |
| select_id | <code>String</code> |  | ID for the dropdown. |
| options | <code>Array.&lt;String&gt;</code> |  | Options for the dropdown. |
| [selected] | <code>String</code> \| <code>Boolean</code> | <code>false</code> | Selected option, if any. |

<a name="BasicForm+add_mover"></a>

### schemaDraftForm.add\_mover(label_text, idx, value) ⇒ [<code>MovingChoice</code>](#MovingChoice)
Create and append a moving input field (when creating options for multiple-choice fields).

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_mover</code>](#BasicForm+add_mover)  
**Returns**: [<code>MovingChoice</code>](#MovingChoice) - Moving input field.  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| label_text | <code>String</code> |  | Text for the label of the input field (e.g. "Select option"). |
| idx | <code>Number</code> |  | Index of the mover in order of creation. |
| value | <code>String</code> \| <code>Boolean</code> | <code>false</code> | Value of the input field in the mover, if it exists. |

<a name="BasicForm+add_moving_options"></a>

### schemaDraftForm.add\_moving\_options(label_text, [starting_values])
Initialize a series of moving choice fields, when first generating a form
for a MultipleInput field.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_moving\_options</code>](#BasicForm+add_moving_options)  

| Param | Type | Description |
| --- | --- | --- |
| label_text | <code>String</code> | Text for the label of the input fields (e.g. "Select option"). |
| [starting_values] | <code>Array.&lt;(String\|Number)&gt;</code> | Initial values for the moving fields. |

<a name="BasicForm+add_switches"></a>

### schemaDraftForm.add\_switches(id, switchnames, [required], [repeatable], [dropdown])
Create and append a DIV element that contains switches to define boolean values of an InputField.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_switches</code>](#BasicForm+add_switches)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| id | <code>String</code> |  | ID of the field to which the form belongs. |
| switchnames | <code>Array.&lt;String&gt;</code> |  | Names of the switches to add. Possible values inside are 'required', 'repeatable' and 'dropdown'. |
| [required] | <code>Boolean</code> | <code>false</code> | Default value of the 'required' switch, i.e. whether the InputField is required. |
| [repeatable] | <code>Boolean</code> | <code>false</code> | Default value of the 'repeatable' switch, i.e. whether the InputField is repeatable. |
| [dropdown] | <code>Boolean</code> | <code>false</code> | Default value of the 'dropdown' switch, i.e. whether the MultipleInput will be rendered as a dropdown. |

<a name="BasicForm+add_action_button"></a>

### schemaDraftForm.add\_action\_button(text, id, color)
Create and append a button for submission.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_action\_button</code>](#BasicForm+add_action_button)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| text | <code>String</code> |  | Text in the action button. |
| id | <code>String</code> | <code>draft</code> | ID for the button. |
| color | <code>String</code> | <code>success</code> | Color class for the button, e.g. 'success', 'danger'... |

<a name="BasicForm+add_submit_action"></a>

### schemaDraftForm.add\_submit\_action(id, action)
Add an action on submission of the form, depending on the button that is clicked.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>add\_submit\_action</code>](#BasicForm+add_submit_action)  

| Param | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | ID of the button that will trigger this action. |
| action | <code>function</code> | Action to execute when clicking on the button. |

<a name="BasicForm+reset"></a>

### schemaDraftForm.reset()
Reset the form, uncheck boxes, remove the 'was-validated' class.

**Kind**: instance method of [<code>SchemaDraftForm</code>](#SchemaDraftForm)  
**Overrides**: [<code>reset</code>](#BasicForm+reset)  
<a name="Modal"></a>

## Modal
Class to create a standard BS5 Modal, typically containing a form to edit a Schema or InputField.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | ID of the modal itself. |
| header_title | <code>String</code> | Text of the title in the header of the modal. |


* [Modal](#Modal)
    * [new Modal(modal_id, header_title)](#new_Modal_new)
    * _instance_
        * [.create_header()](#Modal+create_header) ⇒ <code>HTMLDivElement</code>
        * [.create_body(body_contents)](#Modal+create_body) ⇒ <code>HTMLDivElement</code>
        * [.create_footer()](#Modal+create_footer) ⇒ <code>HTMLDivElement</code>
        * [.create_modal(body_contents, [size])](#Modal+create_modal)
    * _static_
        * [.ask_confirmation(body, action, dismiss)](#Modal.ask_confirmation)
        * [.submit_confirmation(body, url, form_data, extra_Action)](#Modal.submit_confirmation)
        * [.fill_confirmation_form(form_data)](#Modal.fill_confirmation_form)

<a name="new_Modal_new"></a>

### new Modal(modal_id, header_title)
Initialize a modal.


| Param | Type | Description |
| --- | --- | --- |
| modal_id | <code>String</code> | ID of the modal. |
| header_title | <code>String</code> | Text of the title in the header of the modal. |

<a name="Modal+create_header"></a>

### modal.create\_header() ⇒ <code>HTMLDivElement</code>
Create the header for the modal.

**Kind**: instance method of [<code>Modal</code>](#Modal)  
**Returns**: <code>HTMLDivElement</code> - The header for the modal.  
<a name="Modal+create_body"></a>

### modal.create\_body(body_contents) ⇒ <code>HTMLDivElement</code>
Create the body of the modal.

**Kind**: instance method of [<code>Modal</code>](#Modal)  
**Returns**: <code>HTMLDivElement</code> - The body of the modal.  

| Param | Type | Description |
| --- | --- | --- |
| body_contents | <code>Array.&lt;HTMLElement&gt;</code> | Elements to append to the body of the modal, e.g. a form. |

<a name="Modal+create_footer"></a>

### modal.create\_footer() ⇒ <code>HTMLDivElement</code>
Create the footer of the modal

**Kind**: instance method of [<code>Modal</code>](#Modal)  
**Returns**: <code>HTMLDivElement</code> - Footer of the modal.  
<a name="Modal+create_modal"></a>

### modal.create\_modal(body_contents, [size])
Assemble the modal and attach it to the "body" element.

**Kind**: instance method of [<code>Modal</code>](#Modal)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| body_contents | <code>Array.&lt;HTMLElement&gt;</code> |  | Elements to add to the body of the modal, e.g. a form. |
| [size] | <code>String</code> | <code></code> | Size of the modal, e.g. 'sm', 'md'... |

<a name="Modal.ask_confirmation"></a>

### Modal.ask\_confirmation(body, action, dismiss)
Fill in the existing confirmation modal and show it to obtain a simple yes/no answer
to a confirmation question (e.g. Are you sure you want to delete this field?).
This does not apply to modals created with the Modal class, but refers to a modal.

**Kind**: static method of [<code>Modal</code>](#Modal)  

| Param | Type | Description |
| --- | --- | --- |
| body | <code>String</code> | Descriptive text to append to the modal (what are the consequences of accepting this?). |
| action | <code>function</code> | What to do after a positive answer. |
| dismiss | <code>function</code> | What to do after dismissal of the modal (if anything). |

<a name="Modal.submit_confirmation"></a>

### Modal.submit\_confirmation(body, url, form_data, extra_Action)
Fill in the existing confirmation modal and its form and show it to obtain a simple yes/no answer
to a confirmation question (e.g. Are you sure you want to discard this draft?).
This does not apply to modals created with the Modal class, but refers to a modal.
The confirmation button becomes now a submission button for the form contained in the modal.

**Kind**: static method of [<code>Modal</code>](#Modal)  

| Param | Type | Description |
| --- | --- | --- |
| body | <code>String</code> | Descriptive text to append to the modal (what are the consequences of accepting this?). |
| url | <code>String</code> | URL to post the contents of the hidden form to. |
| form_data | <code>Object.&lt;String, String&gt;</code> | Names and values of the hidden fields to add to the form. |
| extra_Action | <code>function</code> | Something extra to do on submission, if relevant. |

<a name="Modal.fill_confirmation_form"></a>

### Modal.fill\_confirmation\_form(form_data)
Update the values of the hidden inputs in the form of the confirmation modal right before submission.

**Kind**: static method of [<code>Modal</code>](#Modal)  

| Param | Type | Description |
| --- | --- | --- |
| form_data | <code>Object.&lt;String, String&gt;</code> | Value of name and value attributes of the fields in the form. |

<a name="AccordionItem"></a>

## AccordionItem
Class to create a standard BS5 Accordion Item, in which the information of a given schema
and all its versions will be displayed.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | The ID of the accordion item we are creating. |
| accordion | <code>String</code> | The ID of the accordion itself. |
| header_title | <code>String</code> | The title of the accordion item, i.e. the name of the schema it shows. |
| div | <code>HTMLDivElement</code> | The accordion item itself. |
| card_body | <code>HTMLDivElement</code> | The body of the accordion item, where the tabs will be displayed. |
| new | <code>Boolean</code> | Whether the item corresponds to the "new schema" editor. |


* [AccordionItem](#AccordionItem)
    * [new AccordionItem(id, header_title, accordion, is_new)](#new_AccordionItem_new)
    * [.create()](#AccordionItem+create)
    * [.append(element, [i])](#AccordionItem+append)

<a name="new_AccordionItem_new"></a>

### new AccordionItem(id, header_title, accordion, is_new)
Initialize a new accordion item to host a schema and all its versions.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| id | <code>String</code> |  | ID of the accordion item. |
| header_title | <code>String</code> |  | Title of the accordion item, i.e. the name of the schema it shows. |
| accordion | <code>String</code> |  | ID of the accordion itself. |
| is_new | <code>Boolean</code> | <code>false</code> | Whether the item corresponds to the "new schema" editor. |

<a name="AccordionItem+create"></a>

### accordionItem.create()
Assemble the parts of the accordion

**Kind**: instance method of [<code>AccordionItem</code>](#AccordionItem)  
<a name="AccordionItem+append"></a>

### accordionItem.append(element, [i])
Append a new element to the accordion item.

**Kind**: instance method of [<code>AccordionItem</code>](#AccordionItem)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| element | <code>HTMLElement</code> |  | An element to append to the accordion item, e.g. a new tab. |
| [i] | <code>Number</code> | <code></code> | Index of the element. |

<a name="NavBar"></a>

## NavBar
Class to create a navigation bar with pills or tabs.
This is used to display the different versions of a schema, with tabs that have badges,
and to switch between views and editors within a version of a schema.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| nav_bar | <code>HTMLUListElement</code> | A list of tabs for navigation. |
| tab_content | <code>HTMLDivElement</code> | The content of the tabs |
| id | <code>String</code> | ID of the instance, used for the IDs of its DOM components. |


* [NavBar](#NavBar)
    * [new NavBar(id, extra_classes)](#new_NavBar_new)
    * [.add_item(item_id, button_text, [active], [position])](#NavBar+add_item)
    * [.remove_item(item_id)](#NavBar+remove_item)
    * [.add_button(item_id, button_text, active, [position])](#NavBar+add_button)
    * [.add_tab(item_id, active, [position])](#NavBar+add_tab)
    * [.add_tab_content(item_id, content)](#NavBar+add_tab_content)
    * [.add_action_button(text, color, action)](#NavBar+add_action_button)

<a name="new_NavBar_new"></a>

### new NavBar(id, extra_classes)
Initialize a navigation bar to host versions of a schema or view/editors of a version.


| Param | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | ID of the NavBar instance, used for the IDs of the navigation list and contents. |
| extra_classes | <code>Array.&lt;String&gt;</code> | Names of classes to be added to the list of navigation bar, e.g. 'justify-content-end' and 'nav-pills'. |

<a name="NavBar+add_item"></a>

### navBar.add\_item(item_id, button_text, [active], [position])
Add a new item to the navigation bar and content.

**Kind**: instance method of [<code>NavBar</code>](#NavBar)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| item_id | <code>String</code> |  | Identifier of the item within the navigation bar. |
| button_text | <code>String</code> \| <code>HTMLElement</code> |  | Content of the button that activates the tab. |
| [active] | <code>Boolean</code> | <code>false</code> | Whether the tab should be focused on. |
| [position] | <code>Number</code> | <code>-1</code> | Index of the item. If -1, the item is added at the end. |

<a name="NavBar+remove_item"></a>

### navBar.remove\_item(item_id)
Remove an item from the navigation bar and content.

**Kind**: instance method of [<code>NavBar</code>](#NavBar)  

| Param | Type | Description |
| --- | --- | --- |
| item_id | <code>String</code> | Identified of the item within the navigation bar. |

<a name="NavBar+add_button"></a>

### navBar.add\_button(item_id, button_text, active, [position])
Add a button to the list in the navigation bar, with the function of activating a corresponding tab.

**Kind**: instance method of [<code>NavBar</code>](#NavBar)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| item_id | <code>String</code> |  | Identifier of the item within the navigation bar. |
| button_text | <code>String</code> \| <code>HTMLElement</code> |  | Content of the button. |
| active | <code>Boolean</code> |  | Whether the tab should be focused on. |
| [position] | <code>Number</code> | <code>-1</code> | Index of the item. If -1, the item is added at the end. |

<a name="NavBar+add_tab"></a>

### navBar.add\_tab(item_id, active, [position])
Add a content tab for an item.

**Kind**: instance method of [<code>NavBar</code>](#NavBar)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| item_id | <code>String</code> |  | Identifier of the item among other tabs. |
| active | <code>Boolean</code> |  | Whether the tab should be focused on. |
| [position] | <code>Number</code> | <code>-1</code> | Index of the item. If -1, the item is added at the end. |

<a name="NavBar+add_tab_content"></a>

### navBar.add\_tab\_content(item_id, content)
Add some content to an existing tab.

**Kind**: instance method of [<code>NavBar</code>](#NavBar)  

| Param | Type | Description |
| --- | --- | --- |
| item_id | <code>String</code> | Identifier of the item among other tabs. |
| content | <code>HTMLElement</code> | Element to append to the tab. |

<a name="NavBar+add_action_button"></a>

### navBar.add\_action\_button(text, color, action)
Add a button to the navigation bar that does not link to a content tab but triggers an action.

**Kind**: instance method of [<code>NavBar</code>](#NavBar)  

| Param | Type | Description |
| --- | --- | --- |
| text | <code>String</code> | Text inside the button. |
| color | <code>String</code> | Color class, e.g. 'success', 'danger'... |
| action | <code>function</code> | Action to trigger when the button is clicked. |

<a name="InputField"></a>

## InputField
Master class to represent input fields. Only the child classes are actually instantiated.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| id | <code>String</code> | Identifier of the field in relation to other fields, used in the DOM elements related to it. It matches `field_id` unless the field is new. |
| field_id | <code>String</code> | ID of the field as it will show in the "ID" input field of the editing form (empty if it has not been defined). |
| form_type | <code>String</code> | Internal type to distinguish different subclasses in the DOM IDs. |
| description | <code>String</code> | Description to show in the example of the options viewer. For now an empty string except in composite fields. |
| dummy_title | <code>String</code> | Title for the example in the options viewer. Always "Informative label". |
| mode | <code>String</code> | In first instance, "add"; when an existing field can be edited, "mod". |
| is_duplicate | <code>Boolean</code> | Whether the field has just been created via duplication of a different field. |
| schema_name | <code>String</code> | Name of the schema the field belongs to. |
| schema_status | <code>String</code> | Derived status of the schema as it is used in the ID of the form ('new', 'draft', 'copy' or 'object...'). |
| required | <code>Boolean</code> | Whether the field should be required when implementing the metadata. |
| repeatable | <code>Boolean</code> | Whether the field can be repeated in the implementation form. |
| values | <code>Object</code> | Variable properties specific to different kinds of fields. |
| default | <code>String</code> \| <code>Number</code> | Default value of the field, if the field is required. |
| form_field | [<code>BasicForm</code>](#BasicForm) | Form to edit the contents of the field. |
| modal | <code>bootstrap.Modal</code> | Modal to which the editing form is attached. |
| button_title | <code>String</code> | User-facing of the type of form. |


* [InputField](#InputField)
    * [new InputField(schema_name, [data_status])](#new_InputField_new)
    * _instance_
        * [.json](#InputField+json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.to_json()](#InputField+to_json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.from_json(data)](#InputField+from_json)
        * [.create_example()](#InputField+create_example) ⇒ <code>HTMLDivElement</code>
        * *[.add_default_field()](#InputField+add_default_field)*
        * *[.create_form()](#InputField+create_form)*
        * [.setup_form()](#InputField+setup_form)
        * [.end_form()](#InputField+end_form)
        * [.create_modal(schema)](#InputField+create_modal)
        * [.render(schema)](#InputField+render) ⇒ <code>HTMLDivElement</code>
        * [.register_fields(schema)](#InputField+register_fields) ⇒ [<code>InputField</code>](#InputField)
        * [.recover_fields(data)](#InputField+recover_fields)
        * [.view(schema)](#InputField+view) ⇒ [<code>MovingViewer</code>](#MovingViewer)
        * [.reset()](#InputField+reset)
    * _static_
        * [.choose_class(schema_name, data_status, id, data)](#InputField.choose_class) ⇒ [<code>InputField</code>](#InputField)

<a name="new_InputField_new"></a>

### new InputField(schema_name, [data_status])
Initialize a new Field in a (mini-)schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema_name | <code>String</code> |  | Name of the schema that the field is attached to, for form identification purposes. |
| [data_status] | <code>String</code> | <code>draft</code> | Status of the schema version that the field is attached to, for form identification purposes. |

<a name="InputField+json"></a>

### inputField.json ⇒ [<code>FieldInfo</code>](#FieldInfo)
Retrieve the contents in JSON format for form submission.

**Kind**: instance property of [<code>InputField</code>](#InputField)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="InputField+to_json"></a>

### inputField.to\_json() ⇒ [<code>FieldInfo</code>](#FieldInfo)
Turn the relevant fields into an Object to be saved in a JSON file.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="InputField+from_json"></a>

### inputField.from\_json(data)
Parse an object to fill in the properties of the object instance.

**Kind**: instance method of [<code>InputField</code>](#InputField)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>FieldInfo</code>](#FieldInfo) | JSON representation of the contents of the field. |

<a name="InputField+create_example"></a>

### inputField.create\_example() ⇒ <code>HTMLDivElement</code>
Generate an example of the field for illustration.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
**Returns**: <code>HTMLDivElement</code> - An element that contains an optional description, a title and an illustration of what the field looks like in a form.  
<a name="InputField+add_default_field"></a>

### *inputField.add\_default\_field()*
Add a field to provide a default value, if relevant.

**Kind**: instance abstract method of [<code>InputField</code>](#InputField)  
<a name="InputField+create_form"></a>

### *inputField.create\_form()*
Create a form to edit the field.

**Kind**: instance abstract method of [<code>InputField</code>](#InputField)  
<a name="InputField+setup_form"></a>

### inputField.setup\_form()
Initalize a form to edit the field and add the components at the beginning of the form.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
<a name="InputField+end_form"></a>

### inputField.end\_form()
Add the last parts of the form
The behavior is more or less subclass-specific, so maybe it can be cleaned up a bit.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
<a name="InputField+create_modal"></a>

### inputField.create\_modal(schema)
Create a modal to host the form to edit the field and define what happens when the form is "submitted".

**Kind**: instance method of [<code>InputField</code>](#InputField)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema that the field is attached to. |

<a name="InputField+render"></a>

### inputField.render(schema) ⇒ <code>HTMLDivElement</code>
Prepare and make a new instance of a field available when editing a schema.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
**Returns**: <code>HTMLDivElement</code> - Element that contains an illustration example and a button to activate an editor modal.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+register_fields"></a>

### inputField.register\_fields(schema) ⇒ [<code>InputField</code>](#InputField)
Create or update an input field and update the Schema it belongs to.
Read the data from the editing form of the field and either update the field or create a new one.
In the latter case, reset the original form so it can be used for new instances of the field.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
**Returns**: [<code>InputField</code>](#InputField) - Updated version of the input field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+recover_fields"></a>

### inputField.recover\_fields(data)
Read the form used to edit the field and register the appropriate values.
Implemented within each subclass, except for `ObjectInput`.

**Kind**: instance method of [<code>InputField</code>](#InputField)  

| Param | Type | Description |
| --- | --- | --- |
| data | <code>FormData</code> | Contents of the editing form of the field. |

<a name="InputField+view"></a>

### inputField.view(schema) ⇒ [<code>MovingViewer</code>](#MovingViewer)
Create an Element to show and edit the field.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
**Returns**: [<code>MovingViewer</code>](#MovingViewer) - Element to show and edit the field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+reset"></a>

### inputField.reset()
Bring the field and its form back to the original settings.

**Kind**: instance method of [<code>InputField</code>](#InputField)  
<a name="InputField.choose_class"></a>

### InputField.choose\_class(schema_name, data_status, id, data) ⇒ [<code>InputField</code>](#InputField)
Select and instantiate the right class depending on the value of the JSON-originated date.

**Kind**: static method of [<code>InputField</code>](#InputField)  
**Returns**: [<code>InputField</code>](#InputField) - The right input field with the data from the FieldInfo object.  

| Param | Type | Description |
| --- | --- | --- |
| schema_name | <code>String</code> | Name of the schema the field is attached to, for DOM ID purposes. |
| data_status | <code>String</code> | Status of the schema version the field is attached to, for DOM ID purposes. |
| id | <code>String</code> | ID of the field to create. |
| data | [<code>FieldInfo</code>](#FieldInfo) | Contents of the field to create. |

<a name="TypedInput"></a>

## TypedInput ⇐ [<code>InputField</code>](#InputField)
Class representing a simple field.
Its `form_type` is always "text", whereas its `type` refers to one of many possible input options.
Its `button_title` is "Simple field" and its `description` includes the many input options.

**Kind**: global class  
**Extends**: [<code>InputField</code>](#InputField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| values.minimum | <code>Number</code> | For numeric inputs, the minimum possible value. |
| values.minimum | <code>Number</code> | For numeric inputs, the maximum possible value. |


* [TypedInput](#TypedInput) ⇐ [<code>InputField</code>](#InputField)
    * [new TypedInput(schema_name, [data_status])](#new_TypedInput_new)
    * _instance_
        * [.json](#InputField+json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.print_range()](#TypedInput+print_range) ⇒ <code>String</code>
        * [.manage_format(format)](#TypedInput+manage_format)
        * [.from_json(data)](#TypedInput+from_json)
        * [.add_default_field()](#TypedInput+add_default_field)
        * [.viewer_input(active)](#TypedInput+viewer_input) ⇒ <code>HTMLDivElement</code>
        * [.create_form()](#TypedInput+create_form)
        * [.recover_fields(data)](#TypedInput+recover_fields)
        * [.reset()](#TypedInput+reset)
        * [.to_json()](#InputField+to_json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.create_example()](#InputField+create_example) ⇒ <code>HTMLDivElement</code>
        * [.setup_form()](#InputField+setup_form)
        * [.end_form()](#InputField+end_form)
        * [.create_modal(schema)](#InputField+create_modal)
        * [.render(schema)](#InputField+render) ⇒ <code>HTMLDivElement</code>
        * [.register_fields(schema)](#InputField+register_fields) ⇒ [<code>InputField</code>](#InputField)
        * [.view(schema)](#InputField+view) ⇒ [<code>MovingViewer</code>](#MovingViewer)
    * _static_
        * [.ex_input()](#TypedInput.ex_input) ⇒ <code>HTMLInputElement</code>

<a name="new_TypedInput_new"></a>

### new TypedInput(schema_name, [data_status])
Initialize a new single field in a (mini-)schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema_name | <code>String</code> |  | Name of the schema that the field is attached to, for form identification purposes. |
| [data_status] | <code>String</code> | <code>draft</code> | Status of the schema version that the field is attached to, for form identification purposes. |

<a name="InputField+json"></a>

### typedInput.json ⇒ [<code>FieldInfo</code>](#FieldInfo)
Retrieve the contents in JSON format for form submission.

**Kind**: instance property of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>json</code>](#InputField+json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="TypedInput+print_range"></a>

### typedInput.print\_range() ⇒ <code>String</code>
Depending on the existence of minimum or maximum for the numeric fields,
provide the appropriate descriptive text.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Returns**: <code>String</code> - Text describing the range of a numeric field.  
<a name="TypedInput+manage_format"></a>

### typedInput.manage\_format(format)
Handle the input fields and values dependent on specific types of simple fields.
If a field editor is generated for the first time, include the appropriate fields.
If a different type is chosen while editing the field, add/remove the appropriate fields.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  

| Param | Type | Description |
| --- | --- | --- |
| format | <code>String</code> | Selected type of the input field. |

<a name="TypedInput+from_json"></a>

### typedInput.from\_json(data)
Parse an object to fill in the properties of the object instance.
Next to the parent class workflow, define the subtitle and retrieve the minimum and maximum for numeric inputs.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>from\_json</code>](#InputField+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>FieldInfo</code>](#FieldInfo) | JSON representation of the contents of the field. |

<a name="TypedInput+add_default_field"></a>

### typedInput.add\_default\_field()
If relevant, create and add an input field for the default value.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>add\_default\_field</code>](#InputField+add_default_field)  
<a name="TypedInput+viewer_input"></a>

### typedInput.viewer\_input(active) ⇒ <code>HTMLDivElement</code>
Create an element with an input field, either to view in a schema-view or to fill in annotation.
The restrictions of the field are described in a subtitle on top of the input field in the schema-view
and as a description under the input field in the annotation form.
In schema-view, the field is read-only, but the default value is filled in if appropriate.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| active | <code>Boolean</code> | <code>false</code> | Whether the form is meant to be used in annotation. |

<a name="TypedInput+create_form"></a>

### typedInput.create\_form()
Create a form to edit the field.
Between setup and ending, add the dropdown to select the type and any other appropriate field.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>create\_form</code>](#InputField+create_form)  
<a name="TypedInput+recover_fields"></a>

### typedInput.recover\_fields(data)
Read the form used to edit the field and register the values (on submission).

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>recover\_fields</code>](#InputField+recover_fields)  

| Param | Type | Description |
| --- | --- | --- |
| data | <code>FormData</code> | Contents of the editing form of the field. |

<a name="TypedInput+reset"></a>

### typedInput.reset()
Bring the field and its form back to the original settings.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>reset</code>](#InputField+reset)  
<a name="InputField+to_json"></a>

### typedInput.to\_json() ⇒ [<code>FieldInfo</code>](#FieldInfo)
Turn the relevant fields into an Object to be saved in a JSON file.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>to\_json</code>](#InputField+to_json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="InputField+create_example"></a>

### typedInput.create\_example() ⇒ <code>HTMLDivElement</code>
Generate an example of the field for illustration.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>create\_example</code>](#InputField+create_example)  
**Returns**: <code>HTMLDivElement</code> - An element that contains an optional description, a title and an illustration of what the field looks like in a form.  
<a name="InputField+setup_form"></a>

### typedInput.setup\_form()
Initalize a form to edit the field and add the components at the beginning of the form.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>setup\_form</code>](#InputField+setup_form)  
<a name="InputField+end_form"></a>

### typedInput.end\_form()
Add the last parts of the form
The behavior is more or less subclass-specific, so maybe it can be cleaned up a bit.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>end\_form</code>](#InputField+end_form)  
<a name="InputField+create_modal"></a>

### typedInput.create\_modal(schema)
Create a modal to host the form to edit the field and define what happens when the form is "submitted".

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>create\_modal</code>](#InputField+create_modal)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema that the field is attached to. |

<a name="InputField+render"></a>

### typedInput.render(schema) ⇒ <code>HTMLDivElement</code>
Prepare and make a new instance of a field available when editing a schema.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>render</code>](#InputField+render)  
**Returns**: <code>HTMLDivElement</code> - Element that contains an illustration example and a button to activate an editor modal.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+register_fields"></a>

### typedInput.register\_fields(schema) ⇒ [<code>InputField</code>](#InputField)
Create or update an input field and update the Schema it belongs to.
Read the data from the editing form of the field and either update the field or create a new one.
In the latter case, reset the original form so it can be used for new instances of the field.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>register\_fields</code>](#InputField+register_fields)  
**Returns**: [<code>InputField</code>](#InputField) - Updated version of the input field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+view"></a>

### typedInput.view(schema) ⇒ [<code>MovingViewer</code>](#MovingViewer)
Create an Element to show and edit the field.

**Kind**: instance method of [<code>TypedInput</code>](#TypedInput)  
**Overrides**: [<code>view</code>](#InputField+view)  
**Returns**: [<code>MovingViewer</code>](#MovingViewer) - Element to show and edit the field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="TypedInput.ex_input"></a>

### TypedInput.ex\_input() ⇒ <code>HTMLInputElement</code>
Create an example of a Simple Field.

**Kind**: static method of [<code>TypedInput</code>](#TypedInput)  
**Returns**: <code>HTMLInputElement</code> - The field to add in an illustration example.  
<a name="ObjectInput"></a>

## ObjectInput ⇐ [<code>InputField</code>](#InputField)
Class representing a composite field
Its `form_type` is always "object", like its `type`.
Its `button_title` is "Composite field" and its description is a brief summary.

**Kind**: global class  
**Extends**: [<code>InputField</code>](#InputField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| editor | [<code>ObjectEditor</code>](#ObjectEditor) | Mini-schema containing the InputFields corresponding to the components of the composite field |
| json_source | [<code>FieldInfo</code>](#FieldInfo) | Contents coming from a JSON file, used to fill in the `editor`. |


* [ObjectInput](#ObjectInput) ⇐ [<code>InputField</code>](#InputField)
    * [new ObjectInput(schema_name, [data_status])](#new_ObjectInput_new)
    * _instance_
        * [.json](#InputField+json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.create_editor()](#ObjectInput+create_editor)
        * [.to_json()](#ObjectInput+to_json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.from_json(data)](#ObjectInput+from_json)
        * [.viewer_input(active)](#ObjectInput+viewer_input) ⇒ <code>HTMLDivElement</code>
        * [.create_form()](#ObjectInput+create_form)
        * [.create_modal(schema)](#ObjectInput+create_modal)
        * [.create_example()](#InputField+create_example) ⇒ <code>HTMLDivElement</code>
        * *[.add_default_field()](#InputField+add_default_field)*
        * [.setup_form()](#InputField+setup_form)
        * [.end_form()](#InputField+end_form)
        * [.render(schema)](#InputField+render) ⇒ <code>HTMLDivElement</code>
        * [.register_fields(schema)](#InputField+register_fields) ⇒ [<code>InputField</code>](#InputField)
        * [.recover_fields(data)](#InputField+recover_fields)
        * [.view(schema)](#InputField+view) ⇒ [<code>MovingViewer</code>](#MovingViewer)
        * [.reset()](#InputField+reset)
    * _static_
        * [.ex_input()](#ObjectInput.ex_input) ⇒ <code>HTMLInputElement</code>

<a name="new_ObjectInput_new"></a>

### new ObjectInput(schema_name, [data_status])
Initialize a new Field in a (mini-)schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema_name | <code>String</code> |  | Name of the schema that the field is attached to, for form identification purposes. |
| [data_status] | <code>String</code> | <code>draft</code> | Status of the schema version that the field is attached to, for form identification purposes. |

<a name="InputField+json"></a>

### objectInput.json ⇒ [<code>FieldInfo</code>](#FieldInfo)
Retrieve the contents in JSON format for form submission.

**Kind**: instance property of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>json</code>](#InputField+json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="ObjectInput+create_editor"></a>

### objectInput.create\_editor()
Create and link a mini-schema (ObjectEditor) to contain the subfields.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
<a name="ObjectInput+to_json"></a>

### objectInput.to\_json() ⇒ [<code>FieldInfo</code>](#FieldInfo)
Turn the relevant fields into an Object to be saved in a JSON file, based on the contents of `editor`.
Overrides the parent version.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>to\_json</code>](#InputField+to_json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="ObjectInput+from_json"></a>

### objectInput.from\_json(data)
Parse an object to fill in the properties of the object instance.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>from\_json</code>](#InputField+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>FieldInfo</code>](#FieldInfo) | JSON representation of the contents of the field. |

<a name="ObjectInput+viewer_input"></a>

### objectInput.viewer\_input(active) ⇒ <code>HTMLDivElement</code>
Create an element with a nested form, either to view in a schema-view or to fill in annotation.
The result is a box with the corresponding `viewer_input` outputs of the components.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| active | <code>Boolean</code> | <code>false</code> | Whether the form is meant to be used in annotation. |

<a name="ObjectInput+create_form"></a>

### objectInput.create\_form()
Create a form to edit the field.
Between setup and ending, create and link an ObjectEditor and fill it with existing data.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>create\_form</code>](#InputField+create_form)  
<a name="ObjectInput+create_modal"></a>

### objectInput.create\_modal(schema)
Create a modal to host the form to edit the field and define what happens when the form is "submitted".

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>create\_modal</code>](#InputField+create_modal)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema that the field is attached to. |

<a name="InputField+create_example"></a>

### objectInput.create\_example() ⇒ <code>HTMLDivElement</code>
Generate an example of the field for illustration.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>create\_example</code>](#InputField+create_example)  
**Returns**: <code>HTMLDivElement</code> - An element that contains an optional description, a title and an illustration of what the field looks like in a form.  
<a name="InputField+add_default_field"></a>

### *objectInput.add\_default\_field()*
Add a field to provide a default value, if relevant.

**Kind**: instance abstract method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>add\_default\_field</code>](#InputField+add_default_field)  
<a name="InputField+setup_form"></a>

### objectInput.setup\_form()
Initalize a form to edit the field and add the components at the beginning of the form.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>setup\_form</code>](#InputField+setup_form)  
<a name="InputField+end_form"></a>

### objectInput.end\_form()
Add the last parts of the form
The behavior is more or less subclass-specific, so maybe it can be cleaned up a bit.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>end\_form</code>](#InputField+end_form)  
<a name="InputField+render"></a>

### objectInput.render(schema) ⇒ <code>HTMLDivElement</code>
Prepare and make a new instance of a field available when editing a schema.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>render</code>](#InputField+render)  
**Returns**: <code>HTMLDivElement</code> - Element that contains an illustration example and a button to activate an editor modal.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+register_fields"></a>

### objectInput.register\_fields(schema) ⇒ [<code>InputField</code>](#InputField)
Create or update an input field and update the Schema it belongs to.
Read the data from the editing form of the field and either update the field or create a new one.
In the latter case, reset the original form so it can be used for new instances of the field.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>register\_fields</code>](#InputField+register_fields)  
**Returns**: [<code>InputField</code>](#InputField) - Updated version of the input field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+recover_fields"></a>

### objectInput.recover\_fields(data)
Read the form used to edit the field and register the appropriate values.
Implemented within each subclass, except for `ObjectInput`.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>recover\_fields</code>](#InputField+recover_fields)  

| Param | Type | Description |
| --- | --- | --- |
| data | <code>FormData</code> | Contents of the editing form of the field. |

<a name="InputField+view"></a>

### objectInput.view(schema) ⇒ [<code>MovingViewer</code>](#MovingViewer)
Create an Element to show and edit the field.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>view</code>](#InputField+view)  
**Returns**: [<code>MovingViewer</code>](#MovingViewer) - Element to show and edit the field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+reset"></a>

### objectInput.reset()
Bring the field and its form back to the original settings.

**Kind**: instance method of [<code>ObjectInput</code>](#ObjectInput)  
**Overrides**: [<code>reset</code>](#InputField+reset)  
<a name="ObjectInput.ex_input"></a>

### ObjectInput.ex\_input() ⇒ <code>HTMLInputElement</code>
Create an example of a Composite Field.

**Kind**: static method of [<code>ObjectInput</code>](#ObjectInput)  
**Returns**: <code>HTMLInputElement</code> - The field to add in an illustration example.  
<a name="MultipleInput"></a>

## MultipleInput ⇐ [<code>InputField</code>](#InputField)
Class representing a multiple-choice field.
Its `form_type` depends on the subclass; its `type` is always "select".
Its `button_title` depends on the subclass.

**Kind**: global class  
**Extends**: [<code>InputField</code>](#InputField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| values.values | <code>Array.&lt;(String\|Number)&gt;</code> | Posible values to choose from. |
| values.multiple | <code>Boolean</code> | Whether multiple values can be selected. |
| values.ui | <code>String</code> | UI rendering of the field (dropdown, checkbox or radio). |
| repeatable | <code>Boolean</code> | Whether the field can be repeatable (it cannot). |


* [MultipleInput](#MultipleInput) ⇐ [<code>InputField</code>](#InputField)
    * [new MultipleInput(schema_name, [data_status])](#new_MultipleInput_new)
    * [.json](#InputField+json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
    * [.from_json(data)](#MultipleInput+from_json)
    * [.viewer_input(active)](#MultipleInput+viewer_input) ⇒ <code>HTMLDivElement</code>
    * [.create_form()](#MultipleInput+create_form)
    * [.recover_fields(data)](#MultipleInput+recover_fields)
    * [.reset()](#MultipleInput+reset)
    * [.to_json()](#InputField+to_json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
    * [.create_example()](#InputField+create_example) ⇒ <code>HTMLDivElement</code>
    * *[.add_default_field()](#InputField+add_default_field)*
    * [.setup_form()](#InputField+setup_form)
    * [.end_form()](#InputField+end_form)
    * [.create_modal(schema)](#InputField+create_modal)
    * [.render(schema)](#InputField+render) ⇒ <code>HTMLDivElement</code>
    * [.register_fields(schema)](#InputField+register_fields) ⇒ [<code>InputField</code>](#InputField)
    * [.view(schema)](#InputField+view) ⇒ [<code>MovingViewer</code>](#MovingViewer)

<a name="new_MultipleInput_new"></a>

### new MultipleInput(schema_name, [data_status])
Initialize a new MultipleInput Field in a (mini-)schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema_name | <code>String</code> |  | Name of the schema that the field is attached to, for form identification purposes. |
| [data_status] | <code>String</code> | <code>draft</code> | Status of the schema version that the field is attached to, for form identification purposes. |

<a name="InputField+json"></a>

### multipleInput.json ⇒ [<code>FieldInfo</code>](#FieldInfo)
Retrieve the contents in JSON format for form submission.

**Kind**: instance property of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>json</code>](#InputField+json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="MultipleInput+from_json"></a>

### multipleInput.from\_json(data)
Parse an object to fill in the properties of the object instance.
Next to the parent class workflow, retrieve the 'values', 'multiple' and 'ui' attributes.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>from\_json</code>](#InputField+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>FieldInfo</code>](#FieldInfo) | JSON representation of the contents of the field. |

<a name="MultipleInput+viewer_input"></a>

### multipleInput.viewer\_input(active) ⇒ <code>HTMLDivElement</code>
Create an element with the right type of input field, either to view in a schema-view or to fill in annotation.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| active | <code>Boolean</code> | <code>false</code> | Whether the form is meant to be used in annotation. |

<a name="MultipleInput+create_form"></a>

### multipleInput.create\_form()
Create a form to edit the field.
Between setup and ending, add moving options depending on the existing values.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>create\_form</code>](#InputField+create_form)  
<a name="MultipleInput+recover_fields"></a>

### multipleInput.recover\_fields(data)
Read the form used to edit the field and register the values (on submission).

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>recover\_fields</code>](#InputField+recover_fields)  

| Param | Type | Description |
| --- | --- | --- |
| data | <code>FormData</code> | Contents of the editing form of the field. |

<a name="MultipleInput+reset"></a>

### multipleInput.reset()
Bring the field and its form back to the original settings.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>reset</code>](#InputField+reset)  
<a name="InputField+to_json"></a>

### multipleInput.to\_json() ⇒ [<code>FieldInfo</code>](#FieldInfo)
Turn the relevant fields into an Object to be saved in a JSON file.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>to\_json</code>](#InputField+to_json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="InputField+create_example"></a>

### multipleInput.create\_example() ⇒ <code>HTMLDivElement</code>
Generate an example of the field for illustration.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>create\_example</code>](#InputField+create_example)  
**Returns**: <code>HTMLDivElement</code> - An element that contains an optional description, a title and an illustration of what the field looks like in a form.  
<a name="InputField+add_default_field"></a>

### *multipleInput.add\_default\_field()*
Add a field to provide a default value, if relevant.

**Kind**: instance abstract method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>add\_default\_field</code>](#InputField+add_default_field)  
<a name="InputField+setup_form"></a>

### multipleInput.setup\_form()
Initalize a form to edit the field and add the components at the beginning of the form.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>setup\_form</code>](#InputField+setup_form)  
<a name="InputField+end_form"></a>

### multipleInput.end\_form()
Add the last parts of the form
The behavior is more or less subclass-specific, so maybe it can be cleaned up a bit.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>end\_form</code>](#InputField+end_form)  
<a name="InputField+create_modal"></a>

### multipleInput.create\_modal(schema)
Create a modal to host the form to edit the field and define what happens when the form is "submitted".

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>create\_modal</code>](#InputField+create_modal)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema that the field is attached to. |

<a name="InputField+render"></a>

### multipleInput.render(schema) ⇒ <code>HTMLDivElement</code>
Prepare and make a new instance of a field available when editing a schema.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>render</code>](#InputField+render)  
**Returns**: <code>HTMLDivElement</code> - Element that contains an illustration example and a button to activate an editor modal.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+register_fields"></a>

### multipleInput.register\_fields(schema) ⇒ [<code>InputField</code>](#InputField)
Create or update an input field and update the Schema it belongs to.
Read the data from the editing form of the field and either update the field or create a new one.
In the latter case, reset the original form so it can be used for new instances of the field.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>register\_fields</code>](#InputField+register_fields)  
**Returns**: [<code>InputField</code>](#InputField) - Updated version of the input field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+view"></a>

### multipleInput.view(schema) ⇒ [<code>MovingViewer</code>](#MovingViewer)
Create an Element to show and edit the field.

**Kind**: instance method of [<code>MultipleInput</code>](#MultipleInput)  
**Overrides**: [<code>view</code>](#InputField+view)  
**Returns**: [<code>MovingViewer</code>](#MovingViewer) - Element to show and edit the field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="SelectInput"></a>

## SelectInput ⇐ [<code>MultipleInput</code>](#MultipleInput)
Class representing a single-value multiple-choice field.
Its `form_type` is always "selection"; its `type` remains "select".
Its `button_type` is always "Single-value multiple choice".
Its `values.multiple` property is always "false"; its `values.ui` property can only be "dropdown" or "radio".

**Kind**: global class  
**Extends**: [<code>MultipleInput</code>](#MultipleInput)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| dropdown_alt | <code>String</code> | The alternative to dropdown: "radio". |


* [SelectInput](#SelectInput) ⇐ [<code>MultipleInput</code>](#MultipleInput)
    * [new SelectInput(schema_name, [data_status])](#new_SelectInput_new)
    * _instance_
        * [.json](#InputField+json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.add_default_field()](#SelectInput+add_default_field)
        * [.from_json(data)](#MultipleInput+from_json)
        * [.viewer_input(active)](#MultipleInput+viewer_input) ⇒ <code>HTMLDivElement</code>
        * [.create_form()](#MultipleInput+create_form)
        * [.recover_fields(data)](#MultipleInput+recover_fields)
        * [.reset()](#MultipleInput+reset)
        * [.to_json()](#InputField+to_json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.create_example()](#InputField+create_example) ⇒ <code>HTMLDivElement</code>
        * [.setup_form()](#InputField+setup_form)
        * [.end_form()](#InputField+end_form)
        * [.create_modal(schema)](#InputField+create_modal)
        * [.render(schema)](#InputField+render) ⇒ <code>HTMLDivElement</code>
        * [.register_fields(schema)](#InputField+register_fields) ⇒ [<code>InputField</code>](#InputField)
        * [.view(schema)](#InputField+view) ⇒ [<code>MovingViewer</code>](#MovingViewer)
    * _static_
        * [.ex_input()](#SelectInput.ex_input) ⇒ <code>HTMLInputElement</code>

<a name="new_SelectInput_new"></a>

### new SelectInput(schema_name, [data_status])
Initialize a new SelectInput Field in a (mini-)schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema_name | <code>String</code> |  | Name of the schema that the field is attached to, for form identification purposes. |
| [data_status] | <code>String</code> | <code>draft</code> | Status of the schema version that the field is attached to, for form identification purposes. |

<a name="InputField+json"></a>

### selectInput.json ⇒ [<code>FieldInfo</code>](#FieldInfo)
Retrieve the contents in JSON format for form submission.

**Kind**: instance property of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>json</code>](#InputField+json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="SelectInput+add_default_field"></a>

### selectInput.add\_default\_field()
If relevant, create and add a dropdown for the default value.
The dropdown options do not adapt as you edit the possible options because that's too much work.
But once you have saved your input, the next edit will offer the right options.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>add\_default\_field</code>](#InputField+add_default_field)  
<a name="MultipleInput+from_json"></a>

### selectInput.from\_json(data)
Parse an object to fill in the properties of the object instance.
Next to the parent class workflow, retrieve the 'values', 'multiple' and 'ui' attributes.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>from\_json</code>](#MultipleInput+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>FieldInfo</code>](#FieldInfo) | JSON representation of the contents of the field. |

<a name="MultipleInput+viewer_input"></a>

### selectInput.viewer\_input(active) ⇒ <code>HTMLDivElement</code>
Create an element with the right type of input field, either to view in a schema-view or to fill in annotation.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>viewer\_input</code>](#MultipleInput+viewer_input)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| active | <code>Boolean</code> | <code>false</code> | Whether the form is meant to be used in annotation. |

<a name="MultipleInput+create_form"></a>

### selectInput.create\_form()
Create a form to edit the field.
Between setup and ending, add moving options depending on the existing values.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>create\_form</code>](#MultipleInput+create_form)  
<a name="MultipleInput+recover_fields"></a>

### selectInput.recover\_fields(data)
Read the form used to edit the field and register the values (on submission).

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>recover\_fields</code>](#MultipleInput+recover_fields)  

| Param | Type | Description |
| --- | --- | --- |
| data | <code>FormData</code> | Contents of the editing form of the field. |

<a name="MultipleInput+reset"></a>

### selectInput.reset()
Bring the field and its form back to the original settings.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>reset</code>](#MultipleInput+reset)  
<a name="InputField+to_json"></a>

### selectInput.to\_json() ⇒ [<code>FieldInfo</code>](#FieldInfo)
Turn the relevant fields into an Object to be saved in a JSON file.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>to\_json</code>](#InputField+to_json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="InputField+create_example"></a>

### selectInput.create\_example() ⇒ <code>HTMLDivElement</code>
Generate an example of the field for illustration.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>create\_example</code>](#InputField+create_example)  
**Returns**: <code>HTMLDivElement</code> - An element that contains an optional description, a title and an illustration of what the field looks like in a form.  
<a name="InputField+setup_form"></a>

### selectInput.setup\_form()
Initalize a form to edit the field and add the components at the beginning of the form.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>setup\_form</code>](#InputField+setup_form)  
<a name="InputField+end_form"></a>

### selectInput.end\_form()
Add the last parts of the form
The behavior is more or less subclass-specific, so maybe it can be cleaned up a bit.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>end\_form</code>](#InputField+end_form)  
<a name="InputField+create_modal"></a>

### selectInput.create\_modal(schema)
Create a modal to host the form to edit the field and define what happens when the form is "submitted".

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>create\_modal</code>](#InputField+create_modal)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema that the field is attached to. |

<a name="InputField+render"></a>

### selectInput.render(schema) ⇒ <code>HTMLDivElement</code>
Prepare and make a new instance of a field available when editing a schema.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>render</code>](#InputField+render)  
**Returns**: <code>HTMLDivElement</code> - Element that contains an illustration example and a button to activate an editor modal.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+register_fields"></a>

### selectInput.register\_fields(schema) ⇒ [<code>InputField</code>](#InputField)
Create or update an input field and update the Schema it belongs to.
Read the data from the editing form of the field and either update the field or create a new one.
In the latter case, reset the original form so it can be used for new instances of the field.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>register\_fields</code>](#InputField+register_fields)  
**Returns**: [<code>InputField</code>](#InputField) - Updated version of the input field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+view"></a>

### selectInput.view(schema) ⇒ [<code>MovingViewer</code>](#MovingViewer)
Create an Element to show and edit the field.

**Kind**: instance method of [<code>SelectInput</code>](#SelectInput)  
**Overrides**: [<code>view</code>](#InputField+view)  
**Returns**: [<code>MovingViewer</code>](#MovingViewer) - Element to show and edit the field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="SelectInput.ex_input"></a>

### SelectInput.ex\_input() ⇒ <code>HTMLInputElement</code>
Create an example of a Single-value Multiple Choice field

**Kind**: static method of [<code>SelectInput</code>](#SelectInput)  
**Returns**: <code>HTMLInputElement</code> - The field to add in an illustration example.  
<a name="CheckboxInput"></a>

## CheckboxInput ⇐ [<code>MultipleInput</code>](#MultipleInput)
Class representing a multiple-value multiple-choice field.
Its `form_type` is always "checkbox"; its `type` remains "select".
Its `button_type` is always "Multiple-value multiple choice".
Its `values.multiple` property is always "true"; its `values.ui` property can only be "dropdown" or "checkbox".

**Kind**: global class  
**Extends**: [<code>MultipleInput</code>](#MultipleInput)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| dropdown_alt | <code>String</code> | The alternative to dropdown: "checkbox". |


* [CheckboxInput](#CheckboxInput) ⇐ [<code>MultipleInput</code>](#MultipleInput)
    * [new CheckboxInput(schema_name, [data_status])](#new_CheckboxInput_new)
    * _instance_
        * [.json](#InputField+json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.from_json(data)](#MultipleInput+from_json)
        * [.viewer_input(active)](#MultipleInput+viewer_input) ⇒ <code>HTMLDivElement</code>
        * [.create_form()](#MultipleInput+create_form)
        * [.recover_fields(data)](#MultipleInput+recover_fields)
        * [.reset()](#MultipleInput+reset)
        * [.to_json()](#InputField+to_json) ⇒ [<code>FieldInfo</code>](#FieldInfo)
        * [.create_example()](#InputField+create_example) ⇒ <code>HTMLDivElement</code>
        * *[.add_default_field()](#InputField+add_default_field)*
        * [.setup_form()](#InputField+setup_form)
        * [.end_form()](#InputField+end_form)
        * [.create_modal(schema)](#InputField+create_modal)
        * [.render(schema)](#InputField+render) ⇒ <code>HTMLDivElement</code>
        * [.register_fields(schema)](#InputField+register_fields) ⇒ [<code>InputField</code>](#InputField)
        * [.view(schema)](#InputField+view) ⇒ [<code>MovingViewer</code>](#MovingViewer)
    * _static_
        * [.ex_input()](#CheckboxInput.ex_input) ⇒ <code>HTMLInputElement</code>

<a name="new_CheckboxInput_new"></a>

### new CheckboxInput(schema_name, [data_status])
Initialize a new CheckboxInput Field in a (mini-)schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema_name | <code>String</code> |  | Name of the schema that the field is attached to, for form identification purposes. |
| [data_status] | <code>String</code> | <code>draft</code> | Status of the schema version that the field is attached to, for form identification purposes. |

<a name="InputField+json"></a>

### checkboxInput.json ⇒ [<code>FieldInfo</code>](#FieldInfo)
Retrieve the contents in JSON format for form submission.

**Kind**: instance property of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>json</code>](#InputField+json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="MultipleInput+from_json"></a>

### checkboxInput.from\_json(data)
Parse an object to fill in the properties of the object instance.
Next to the parent class workflow, retrieve the 'values', 'multiple' and 'ui' attributes.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>from\_json</code>](#MultipleInput+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>FieldInfo</code>](#FieldInfo) | JSON representation of the contents of the field. |

<a name="MultipleInput+viewer_input"></a>

### checkboxInput.viewer\_input(active) ⇒ <code>HTMLDivElement</code>
Create an element with the right type of input field, either to view in a schema-view or to fill in annotation.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>viewer\_input</code>](#MultipleInput+viewer_input)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| active | <code>Boolean</code> | <code>false</code> | Whether the form is meant to be used in annotation. |

<a name="MultipleInput+create_form"></a>

### checkboxInput.create\_form()
Create a form to edit the field.
Between setup and ending, add moving options depending on the existing values.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>create\_form</code>](#MultipleInput+create_form)  
<a name="MultipleInput+recover_fields"></a>

### checkboxInput.recover\_fields(data)
Read the form used to edit the field and register the values (on submission).

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>recover\_fields</code>](#MultipleInput+recover_fields)  

| Param | Type | Description |
| --- | --- | --- |
| data | <code>FormData</code> | Contents of the editing form of the field. |

<a name="MultipleInput+reset"></a>

### checkboxInput.reset()
Bring the field and its form back to the original settings.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>reset</code>](#MultipleInput+reset)  
<a name="InputField+to_json"></a>

### checkboxInput.to\_json() ⇒ [<code>FieldInfo</code>](#FieldInfo)
Turn the relevant fields into an Object to be saved in a JSON file.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>to\_json</code>](#InputField+to_json)  
**Returns**: [<code>FieldInfo</code>](#FieldInfo) - JSON representation of the contents of the field.  
<a name="InputField+create_example"></a>

### checkboxInput.create\_example() ⇒ <code>HTMLDivElement</code>
Generate an example of the field for illustration.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>create\_example</code>](#InputField+create_example)  
**Returns**: <code>HTMLDivElement</code> - An element that contains an optional description, a title and an illustration of what the field looks like in a form.  
<a name="InputField+add_default_field"></a>

### *checkboxInput.add\_default\_field()*
Add a field to provide a default value, if relevant.

**Kind**: instance abstract method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>add\_default\_field</code>](#InputField+add_default_field)  
<a name="InputField+setup_form"></a>

### checkboxInput.setup\_form()
Initalize a form to edit the field and add the components at the beginning of the form.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>setup\_form</code>](#InputField+setup_form)  
<a name="InputField+end_form"></a>

### checkboxInput.end\_form()
Add the last parts of the form
The behavior is more or less subclass-specific, so maybe it can be cleaned up a bit.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>end\_form</code>](#InputField+end_form)  
<a name="InputField+create_modal"></a>

### checkboxInput.create\_modal(schema)
Create a modal to host the form to edit the field and define what happens when the form is "submitted".

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>create\_modal</code>](#InputField+create_modal)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema that the field is attached to. |

<a name="InputField+render"></a>

### checkboxInput.render(schema) ⇒ <code>HTMLDivElement</code>
Prepare and make a new instance of a field available when editing a schema.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>render</code>](#InputField+render)  
**Returns**: <code>HTMLDivElement</code> - Element that contains an illustration example and a button to activate an editor modal.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+register_fields"></a>

### checkboxInput.register\_fields(schema) ⇒ [<code>InputField</code>](#InputField)
Create or update an input field and update the Schema it belongs to.
Read the data from the editing form of the field and either update the field or create a new one.
In the latter case, reset the original form so it can be used for new instances of the field.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>register\_fields</code>](#InputField+register_fields)  
**Returns**: [<code>InputField</code>](#InputField) - Updated version of the input field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="InputField+view"></a>

### checkboxInput.view(schema) ⇒ [<code>MovingViewer</code>](#MovingViewer)
Create an Element to show and edit the field.

**Kind**: instance method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Overrides**: [<code>view</code>](#InputField+view)  
**Returns**: [<code>MovingViewer</code>](#MovingViewer) - Element to show and edit the field.  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | (Mini-)schema the field belongs to. |

<a name="CheckboxInput.ex_input"></a>

### CheckboxInput.ex\_input() ⇒ <code>HTMLInputElement</code>
Create an example of a Multiple-value Multiple Choice field

**Kind**: static method of [<code>CheckboxInput</code>](#CheckboxInput)  
**Returns**: <code>HTMLInputElement</code> - The field to add in an illustration example.  
<a name="MangoRequest"></a>

## MangoRequest ⇐ <code>XMLHttpRequest</code>
Abstract class to handle GET requests

**Kind**: global class  
**Extends**: <code>XMLHttpRequest</code>  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| url | <code>String</code> | The URL to be called. |


* [MangoRequest](#MangoRequest) ⇐ <code>XMLHttpRequest</code>
    * [new MangoRequest(url)](#new_MangoRequest_new)
    * [.json](#MangoRequest+json) ⇒ <code>object</code>
    * [.retrieve()](#MangoRequest+retrieve)

<a name="new_MangoRequest_new"></a>

### new MangoRequest(url)
Instantiate a request.


| Param | Type | Description |
| --- | --- | --- |
| url | <code>string</code> | The URL for the XMLHttpRequest. |

<a name="MangoRequest+json"></a>

### mangoRequest.json ⇒ <code>object</code>
Get the contents of the response.

**Kind**: instance property of [<code>MangoRequest</code>](#MangoRequest)  
**Returns**: <code>object</code> - The parsed contents of the response.  
<a name="MangoRequest+retrieve"></a>

### mangoRequest.retrieve()
Send the GET request.

**Kind**: instance method of [<code>MangoRequest</code>](#MangoRequest)  
<a name="TemplatesRequest"></a>

## TemplatesRequest ⇐ [<code>MangoRequest</code>](#MangoRequest)
Class representing a request for a list of schemas.

**Kind**: global class  
**Extends**: [<code>MangoRequest</code>](#MangoRequest)  
**See**: SchemaGroup  

* [TemplatesRequest](#TemplatesRequest) ⇐ [<code>MangoRequest</code>](#MangoRequest)
    * [new TemplatesRequest(urls, container_id)](#new_TemplatesRequest_new)
    * [.json](#MangoRequest+json) ⇒ <code>object</code>
    * [.parse_response(container_id, urls)](#TemplatesRequest+parse_response)
    * [.retrieve()](#MangoRequest+retrieve)

<a name="new_TemplatesRequest_new"></a>

### new TemplatesRequest(urls, container_id)
Get a list of schemas and deploy them on the screen.


| Param | Type | Description |
| --- | --- | --- |
| urls | [<code>UrlsList</code>](#UrlsList) | Key-value pairs with necessary URLs and other backend information. |
| container_id | <code>String</code> | ID of the DOM elements that the accordions will be attached to. |

<a name="MangoRequest+json"></a>

### templatesRequest.json ⇒ <code>object</code>
Get the contents of the response.

**Kind**: instance property of [<code>TemplatesRequest</code>](#TemplatesRequest)  
**Overrides**: [<code>json</code>](#MangoRequest+json)  
**Returns**: <code>object</code> - The parsed contents of the response.  
<a name="TemplatesRequest+parse_response"></a>

### templatesRequest.parse\_response(container_id, urls)
Read the list of schemas and generate the required accordions and badges.

**Kind**: instance method of [<code>TemplatesRequest</code>](#TemplatesRequest)  
**See**: SchemaGroup  

| Param | Type | Description |
| --- | --- | --- |
| container_id | <code>String</code> | ID of the DOM elements that the accordions will be attached to. |
| urls | [<code>UrlsList</code>](#UrlsList) | Key-value pairs with the necessary urls and other backend information. |

<a name="MangoRequest+retrieve"></a>

### templatesRequest.retrieve()
Send the GET request.

**Kind**: instance method of [<code>TemplatesRequest</code>](#TemplatesRequest)  
**Overrides**: [<code>retrieve</code>](#MangoRequest+retrieve)  
<a name="TemplateReader"></a>

## TemplateReader
Class representing a request for a schema (to manage).

**Kind**: global class  

* [TemplateReader](#TemplateReader)
    * [new TemplateReader(url, schema)](#new_TemplateReader_new)
    * [.parse_response(schema)](#TemplateReader+parse_response)

<a name="new_TemplateReader_new"></a>

### new TemplateReader(url, schema)
Get the existing data for a schema version and render it. Called lazily the first time that the tab is opened.


| Param | Type | Description |
| --- | --- | --- |
| url | <code>String</code> | URL from which to obtain the schema version. |
| schema | [<code>Schema</code>](#Schema) | Initialized Schema to fill in with existing data. |

<a name="TemplateReader+parse_response"></a>

### templateReader.parse\_response(schema)
Provide the contents of the JSON file to the schema and render into the page.

**Kind**: instance method of [<code>TemplateReader</code>](#TemplateReader)  

| Param | Type | Description |
| --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) | Initialized Schema to fill in with existing data. |

<a name="AnnotationRequest"></a>

## AnnotationRequest ⇐ [<code>MangoRequest</code>](#MangoRequest)
Class representing a request for a schema for annotation.

**Kind**: global class  
**Extends**: [<code>MangoRequest</code>](#MangoRequest)  

* [AnnotationRequest](#AnnotationRequest) ⇐ [<code>MangoRequest</code>](#MangoRequest)
    * [new AnnotationRequest(schema_url, annotated_data, prefix)](#new_AnnotationRequest_new)
    * [.json](#MangoRequest+json) ⇒ <code>object</code>
    * [.parse_response(annotated_data, prefix)](#AnnotationRequest+parse_response)
    * [.retrieve()](#MangoRequest+retrieve)

<a name="new_AnnotationRequest_new"></a>

### new AnnotationRequest(schema_url, annotated_data, prefix)
Get an existing schema and metadata associated with it to edit the metadata of a collection or data-object.


| Param | Type | Description |
| --- | --- | --- |
| schema_url | <code>String</code> | URL from which to retrieve the metadata schema. |
| annotated_data | <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code> | Key-value pairs with existing metadata related to the schema. |
| prefix | <code>String</code> | Prefix for the metadata attribute names, e.g. `mgs.book` |

<a name="MangoRequest+json"></a>

### annotationRequest.json ⇒ <code>object</code>
Get the contents of the response.

**Kind**: instance property of [<code>AnnotationRequest</code>](#AnnotationRequest)  
**Overrides**: [<code>json</code>](#MangoRequest+json)  
**Returns**: <code>object</code> - The parsed contents of the response.  
<a name="AnnotationRequest+parse_response"></a>

### annotationRequest.parse\_response(annotated_data, prefix)
Read the JSON of a schema, generate a form for implementation and fill it with existing metadata.

**Kind**: instance method of [<code>AnnotationRequest</code>](#AnnotationRequest)  

| Param | Type | Description |
| --- | --- | --- |
| annotated_data | <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code> | Key-value pairs with existing metadata related to the schema. |
| prefix | <code>String</code> | Prefix for the metadata attribute names, e.g. `mgs.book` |

<a name="MangoRequest+retrieve"></a>

### annotationRequest.retrieve()
Send the GET request.

**Kind**: instance method of [<code>AnnotationRequest</code>](#AnnotationRequest)  
**Overrides**: [<code>retrieve</code>](#MangoRequest+retrieve)  
<a name="ComplexField"></a>

## ComplexField
Master class to represent schemas and mini-schemas. Only the child classes are actually instantiated.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| modal_id | <code>String</code> | ID of the modal through which a new input field can be chosen. |
| initial_name | <code>String</code> | Placeholder name for DOM element IDs. |
| title | <code>String</code> | User-facing label of the schema (or composite field). |
| data_status | <code>String</code> | Derived status used for IDs of DOM elements, e.g. 'new', 'copy', 'draft'... |
| initials | <code>Object.&lt;String, InputField&gt;</code> | Collection of empty fields to start creating. |
| initials.typed | [<code>TypedInput</code>](#TypedInput) | Initial simple field. |
| initials.select | [<code>SelectInput</code>](#SelectInput) | Initial single-value multiple-choice field. |
| initials.checkbox | [<code>CheckboxInput</code>](#CheckboxInput) | Initial multiple-value multiple-choice field. |
| initials.object | [<code>ObjectInput</code>](#ObjectInput) | Initial composite field. |
| field_ids | <code>Array.&lt;String&gt;</code> | Ordered names of the fields. |
| fields | <code>Object.&lt;String, InputField&gt;</code> | Collection of fields that belong to the schema. |
| properties | <code>Object.&lt;String, FieldInfo&gt;</code> | Object-version of the information of the fields, to store in a JSON. |
| new_field_idx | <code>Number</code> | Index of the following field that could be added. |


* [ComplexField](#ComplexField)
    * [new ComplexField(name, data_status)](#new_ComplexField_new)
    * _instance_
        * [.fields_to_json()](#ComplexField+fields_to_json)
        * [.from_json(data)](#ComplexField+from_json)
        * [.set_data_status()](#ComplexField+set_data_status) ⇒ <code>String</code>
        * [.display_options()](#ComplexField+display_options)
        * [.view_field(form_object)](#ComplexField+view_field)
        * [.add_field(form_object)](#ComplexField+add_field)
        * [.update_field(form_object)](#ComplexField+update_field)
        * [.replace_field(old_id, form_object)](#ComplexField+replace_field)
        * [.toggle_saving()](#ComplexField+toggle_saving)
        * [.create_button()](#ComplexField+create_button) ⇒ <code>HTMLDivElement</code>
        * [.reset()](#ComplexField+reset)
    * _static_
        * [.create_viewer(schema, [active])](#ComplexField.create_viewer) ⇒ <code>HTMLDivElement</code> \| <code>HTMLFormElement</code>

<a name="new_ComplexField_new"></a>

### new ComplexField(name, data_status)
Initialize a Schema, mini-schema for a composite field or dummy mini-schema for illustrating a composite field.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| name | <code>String</code> |  | Initial name of the schema, for IDs of the DOM elements. |
| data_status | <code>String</code> | <code>draft</code> | Derived status used in IDs of DOM elements. |

<a name="ComplexField+fields_to_json"></a>

### complexField.fields\_to\_json()
Collect the Object-version of the fields into the `properties` property to save as JSON.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  
<a name="ComplexField+from_json"></a>

### complexField.from\_json(data)
Capture data from the JSON representation of a schema.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>SchemaContents</code>](#SchemaContents) | JSON representation of a schema |

<a name="ComplexField+set_data_status"></a>

### complexField.set\_data\_status() ⇒ <code>String</code>
Compute the `data_status` property based on the status of the version.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  
<a name="ComplexField+display_options"></a>

### complexField.display\_options()
Create a modal that offers the different fields that can be added and fill it when shown.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  
<a name="ComplexField+view_field"></a>

### complexField.view\_field(form_object)
Create a MovingViewer for a field and add it to the editing section of the (mini-)schema.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field belonging to this schema. |

<a name="ComplexField+add_field"></a>

### complexField.add\_field(form_object)
Add a new field to the (mini-)schema.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be added to this schema. |

<a name="ComplexField+update_field"></a>

### complexField.update\_field(form_object)
Update an existing field in a schema.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be updated. |

<a name="ComplexField+replace_field"></a>

### complexField.replace\_field(old_id, form_object)
Replace (rename) an existing field in a schema.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  

| Param | Type | Description |
| --- | --- | --- |
| old_id | <code>String</code> | ID of the field to be replaced. |
| form_object | [<code>InputField</code>](#InputField) | Replacement field. |

<a name="ComplexField+toggle_saving"></a>

### complexField.toggle\_saving()
Disable or enable saving a (mini-)schema based on whether any of the existing fields is a duplicate.
Duplicates don't have ids, so we cannot save a schema until that issue is resolved.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  
<a name="ComplexField+create_button"></a>

### complexField.create\_button() ⇒ <code>HTMLDivElement</code>
Create a button to create more form elements. On click, it updates the value of the `new_field_idx` property.
It also activates the modal that offers the different types of fields.

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  
**Returns**: <code>HTMLDivElement</code> - A DIV with the button.  
<a name="ComplexField+reset"></a>

### complexField.reset()
Reset the contents of this schema: no fields, initial name

**Kind**: instance method of [<code>ComplexField</code>](#ComplexField)  
<a name="ComplexField.create_viewer"></a>

### ComplexField.create\_viewer(schema, [active]) ⇒ <code>HTMLDivElement</code> \| <code>HTMLFormElement</code>
Create a form or simulation of form from a Schema.
In the schema manager, this generates the 'view' of an existing version.
In the metadata annotation, this generates the form to be filled.

**Kind**: static method of [<code>ComplexField</code>](#ComplexField)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| schema | [<code>Schema</code>](#Schema) |  | Schema to view. |
| [active] | <code>Boolean</code> | <code>false</code> | Whether the form will be used for application of metadata. |

<a name="DummyObject"></a>

## DummyObject ⇐ [<code>ComplexField</code>](#ComplexField)
Class for illustration of an ObjectEditor.
It has three fixed IDs to illustrate: a simple text input, a simple date input and a radio.

**Kind**: global class  
**Extends**: [<code>ComplexField</code>](#ComplexField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| schema_name | <code>String</code> | The name of the fake object ("example"). |


* [DummyObject](#DummyObject) ⇐ [<code>ComplexField</code>](#ComplexField)
    * [new DummyObject()](#new_DummyObject_new)
    * [.fields_to_json()](#ComplexField+fields_to_json)
    * [.from_json(data)](#ComplexField+from_json)
    * [.set_data_status()](#ComplexField+set_data_status) ⇒ <code>String</code>
    * [.display_options()](#ComplexField+display_options)
    * [.view_field(form_object)](#ComplexField+view_field)
    * [.add_field(form_object)](#ComplexField+add_field)
    * [.update_field(form_object)](#ComplexField+update_field)
    * [.replace_field(old_id, form_object)](#ComplexField+replace_field)
    * [.toggle_saving()](#ComplexField+toggle_saving)
    * [.create_button()](#ComplexField+create_button) ⇒ <code>HTMLDivElement</code>
    * [.reset()](#ComplexField+reset)

<a name="new_DummyObject_new"></a>

### new DummyObject()
Initialize the DummyObject.

<a name="ComplexField+fields_to_json"></a>

### dummyObject.fields\_to\_json()
Collect the Object-version of the fields into the `properties` property to save as JSON.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>fields\_to\_json</code>](#ComplexField+fields_to_json)  
<a name="ComplexField+from_json"></a>

### dummyObject.from\_json(data)
Capture data from the JSON representation of a schema.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>from\_json</code>](#ComplexField+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>SchemaContents</code>](#SchemaContents) | JSON representation of a schema |

<a name="ComplexField+set_data_status"></a>

### dummyObject.set\_data\_status() ⇒ <code>String</code>
Compute the `data_status` property based on the status of the version.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>set\_data\_status</code>](#ComplexField+set_data_status)  
<a name="ComplexField+display_options"></a>

### dummyObject.display\_options()
Create a modal that offers the different fields that can be added and fill it when shown.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>display\_options</code>](#ComplexField+display_options)  
<a name="ComplexField+view_field"></a>

### dummyObject.view\_field(form_object)
Create a MovingViewer for a field and add it to the editing section of the (mini-)schema.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>view\_field</code>](#ComplexField+view_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field belonging to this schema. |

<a name="ComplexField+add_field"></a>

### dummyObject.add\_field(form_object)
Add a new field to the (mini-)schema.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>add\_field</code>](#ComplexField+add_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be added to this schema. |

<a name="ComplexField+update_field"></a>

### dummyObject.update\_field(form_object)
Update an existing field in a schema.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>update\_field</code>](#ComplexField+update_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be updated. |

<a name="ComplexField+replace_field"></a>

### dummyObject.replace\_field(old_id, form_object)
Replace (rename) an existing field in a schema.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>replace\_field</code>](#ComplexField+replace_field)  

| Param | Type | Description |
| --- | --- | --- |
| old_id | <code>String</code> | ID of the field to be replaced. |
| form_object | [<code>InputField</code>](#InputField) | Replacement field. |

<a name="ComplexField+toggle_saving"></a>

### dummyObject.toggle\_saving()
Disable or enable saving a (mini-)schema based on whether any of the existing fields is a duplicate.
Duplicates don't have ids, so we cannot save a schema until that issue is resolved.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>toggle\_saving</code>](#ComplexField+toggle_saving)  
<a name="ComplexField+create_button"></a>

### dummyObject.create\_button() ⇒ <code>HTMLDivElement</code>
Create a button to create more form elements. On click, it updates the value of the `new_field_idx` property.
It also activates the modal that offers the different types of fields.

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>create\_button</code>](#ComplexField+create_button)  
**Returns**: <code>HTMLDivElement</code> - A DIV with the button.  
<a name="ComplexField+reset"></a>

### dummyObject.reset()
Reset the contents of this schema: no fields, initial name

**Kind**: instance method of [<code>DummyObject</code>](#DummyObject)  
**Overrides**: [<code>reset</code>](#ComplexField+reset)  
<a name="ObjectEditor"></a>

## ObjectEditor ⇐ [<code>ComplexField</code>](#ComplexField)
Class for mini-schemas connected to a composite field.
`data_status` always starts with 'object', followed by the `data_status`
of the schema that the composite field belongs to.

**Kind**: global class  
**Extends**: [<code>ComplexField</code>](#ComplexField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| parent_status | <code>String</code> | `data_status` of the (mini-)schema the composite field belongs to. |
| form_id | <code>String</code> | ID of the editing form of the composite field this is linked to. |
| card_id | <code>String</code> | ID of the editing modal of the composite field this is linked to. Assigned by `ObjectInput.create_modal()`. |


* [ObjectEditor](#ObjectEditor) ⇐ [<code>ComplexField</code>](#ComplexField)
    * [new ObjectEditor(parent)](#new_ObjectEditor_new)
    * [.button](#ObjectEditor+button) ⇒ <code>HTMLDivElement</code>
    * [.form_div](#ObjectEditor+form_div) ⇒ <code>HTMLFormElement</code>
    * [.set_data_status()](#ObjectEditor+set_data_status) ⇒ <code>String</code>
    * [.fields_to_json()](#ComplexField+fields_to_json)
    * [.from_json(data)](#ComplexField+from_json)
    * [.display_options()](#ComplexField+display_options)
    * [.view_field(form_object)](#ComplexField+view_field)
    * [.add_field(form_object)](#ComplexField+add_field)
    * [.update_field(form_object)](#ComplexField+update_field)
    * [.replace_field(old_id, form_object)](#ComplexField+replace_field)
    * [.toggle_saving()](#ComplexField+toggle_saving)
    * [.create_button()](#ComplexField+create_button) ⇒ <code>HTMLDivElement</code>
    * [.reset()](#ComplexField+reset)

<a name="new_ObjectEditor_new"></a>

### new ObjectEditor(parent)
Create a mini-schema for a composite field.


| Param | Type | Description |
| --- | --- | --- |
| parent | [<code>ObjectInput</code>](#ObjectInput) | Composite field this mini-schema is linked to. |

<a name="ObjectEditor+button"></a>

### objectEditor.button ⇒ <code>HTMLDivElement</code>
Create a button to add more fields.

**Kind**: instance property of [<code>ObjectEditor</code>](#ObjectEditor)  
**Returns**: <code>HTMLDivElement</code> - A DIV with a button.  
<a name="ObjectEditor+form_div"></a>

### objectEditor.form\_div ⇒ <code>HTMLFormElement</code>
Get the form with the moving viewers of the fields.

**Kind**: instance property of [<code>ObjectEditor</code>](#ObjectEditor)  
<a name="ObjectEditor+set_data_status"></a>

### objectEditor.set\_data\_status() ⇒ <code>String</code>
Obtain the data_status of the mini-schema.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>set\_data\_status</code>](#ComplexField+set_data_status)  
**Returns**: <code>String</code> - Derived status as used in IDs for DOM elements.  
<a name="ComplexField+fields_to_json"></a>

### objectEditor.fields\_to\_json()
Collect the Object-version of the fields into the `properties` property to save as JSON.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>fields\_to\_json</code>](#ComplexField+fields_to_json)  
<a name="ComplexField+from_json"></a>

### objectEditor.from\_json(data)
Capture data from the JSON representation of a schema.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>from\_json</code>](#ComplexField+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>SchemaContents</code>](#SchemaContents) | JSON representation of a schema |

<a name="ComplexField+display_options"></a>

### objectEditor.display\_options()
Create a modal that offers the different fields that can be added and fill it when shown.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>display\_options</code>](#ComplexField+display_options)  
<a name="ComplexField+view_field"></a>

### objectEditor.view\_field(form_object)
Create a MovingViewer for a field and add it to the editing section of the (mini-)schema.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>view\_field</code>](#ComplexField+view_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field belonging to this schema. |

<a name="ComplexField+add_field"></a>

### objectEditor.add\_field(form_object)
Add a new field to the (mini-)schema.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>add\_field</code>](#ComplexField+add_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be added to this schema. |

<a name="ComplexField+update_field"></a>

### objectEditor.update\_field(form_object)
Update an existing field in a schema.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>update\_field</code>](#ComplexField+update_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be updated. |

<a name="ComplexField+replace_field"></a>

### objectEditor.replace\_field(old_id, form_object)
Replace (rename) an existing field in a schema.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>replace\_field</code>](#ComplexField+replace_field)  

| Param | Type | Description |
| --- | --- | --- |
| old_id | <code>String</code> | ID of the field to be replaced. |
| form_object | [<code>InputField</code>](#InputField) | Replacement field. |

<a name="ComplexField+toggle_saving"></a>

### objectEditor.toggle\_saving()
Disable or enable saving a (mini-)schema based on whether any of the existing fields is a duplicate.
Duplicates don't have ids, so we cannot save a schema until that issue is resolved.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>toggle\_saving</code>](#ComplexField+toggle_saving)  
<a name="ComplexField+create_button"></a>

### objectEditor.create\_button() ⇒ <code>HTMLDivElement</code>
Create a button to create more form elements. On click, it updates the value of the `new_field_idx` property.
It also activates the modal that offers the different types of fields.

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>create\_button</code>](#ComplexField+create_button)  
**Returns**: <code>HTMLDivElement</code> - A DIV with the button.  
<a name="ComplexField+reset"></a>

### objectEditor.reset()
Reset the contents of this schema: no fields, initial name

**Kind**: instance method of [<code>ObjectEditor</code>](#ObjectEditor)  
**Overrides**: [<code>reset</code>](#ComplexField+reset)  
<a name="Schema"></a>

## Schema ⇐ [<code>ComplexField</code>](#ComplexField)
Class for a version of a schema.

**Kind**: global class  
**Extends**: [<code>ComplexField</code>](#ComplexField)  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| card_id | <code>String</code> | ID of the DIV that everything related to this version of the schema is rendered; also part of the IDs of elements inside of it. It combines the name and version. |
| name | <code>String</code> | ID of the schema itself, if it exists. |
| version | <code>String</code> | Version number of this version of the schema. |
| container | <code>String</code> | ID of the DOM element inside which this schema version is displayed. |
| urls | [<code>UrlsList</code>](#UrlsList) | Collection of URLs and other information obtained from the server side. |
| parent | <code>String</code> | If this schema was born as clone of another schema, the name and version of the parent schema. |
| origin | <code>Object</code> | If this is a draft initiated as clone of a published schema, information on the fields that are cloned with it. |
| origin.ids | <code>Array.&lt;String&gt;</code> | IDs of the fields cloned with a clone schema. |
| origin.json | <code>Object.&lt;String, FieldInfo&gt;</code> | Collection of Object-versions of the fields cloned with a clone schema. |
| child | [<code>Schema</code>](#Schema) | If this is a published schema, the draft Schema for its clone. |
| card | [<code>AccordionItem</code>](#AccordionItem) \| <code>HTMLDivElement</code> | The DIV that contains everything related to this version of the schema. It's an `AccordionItem` for the new (empty) schema. |
| form | [<code>SchemaDraftForm</code>](#SchemaDraftForm) | Form that gets submitted when the schema version is saved or published. |
| nav_bar | [<code>NavBar</code>](#NavBar) | Navigation bar and tab contents with view and editor(s) of this version of the schema. |


* [Schema](#Schema) ⇐ [<code>ComplexField</code>](#ComplexField)
    * [new Schema(card_id, container_id, urls, [version], [data_status])](#new_Schema_new)
    * [.form_div](#Schema+form_div) ⇒ <code>HTMLFormElement</code>
    * [.from_json(data)](#Schema+from_json)
    * [.set_data_status()](#Schema+set_data_status) ⇒ <code>String</code>
    * [.create_creator()](#Schema+create_creator)
    * [.create_editor()](#Schema+create_editor)
    * [.from_parent(parent)](#Schema+from_parent)
    * [.setup_copy()](#Schema+setup_copy)
    * [.create_navbar()](#Schema+create_navbar)
    * [.draft_from_publish()](#Schema+draft_from_publish)
    * [.view()](#Schema+view)
    * [.save_draft(action)](#Schema+save_draft)
    * [.fields_to_json()](#ComplexField+fields_to_json)
    * [.display_options()](#ComplexField+display_options)
    * [.view_field(form_object)](#ComplexField+view_field)
    * [.add_field(form_object)](#ComplexField+add_field)
    * [.update_field(form_object)](#ComplexField+update_field)
    * [.replace_field(old_id, form_object)](#ComplexField+replace_field)
    * [.toggle_saving()](#ComplexField+toggle_saving)
    * [.create_button()](#ComplexField+create_button) ⇒ <code>HTMLDivElement</code>
    * [.reset()](#ComplexField+reset)

<a name="new_Schema_new"></a>

### new Schema(card_id, container_id, urls, [version], [data_status])
Initialize a new version of a schema.


| Param | Type | Default | Description |
| --- | --- | --- | --- |
| card_id | <code>String</code> |  | ID for the DIV this version will be hosted on, combining the version number and name. |
| container_id | <code>String</code> |  | ID of the parent DIV. |
| urls | [<code>UrlsList</code>](#UrlsList) |  | Collection of URLs and other information obtained from the server side. |
| [version] | <code>String</code> | <code>1.0.0</code> | Version number of this version of the schema. |
| [data_status] | <code>String</code> | <code>draft</code> | Derived status used for IDs of DOM elements. |

<a name="Schema+form_div"></a>

### schema.form\_div ⇒ <code>HTMLFormElement</code>
Get the form with the moving viewers of the fields.

**Kind**: instance property of [<code>Schema</code>](#Schema)  
<a name="Schema+from_json"></a>

### schema.from\_json(data)
Capture data from the JSON representation of a schema.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>from\_json</code>](#ComplexField+from_json)  

| Param | Type | Description |
| --- | --- | --- |
| data | [<code>SchemaContents</code>](#SchemaContents) | JSON representation of a schema |

<a name="Schema+set_data_status"></a>

### schema.set\_data\_status() ⇒ <code>String</code>
Obtain the data_status of the schema.
This is used in the IDs of DOM elements related to editing a schema.
- 'new' indicates a new draft from a published version.
- 'draft' indicates a new schema from scratch or an existing draft version.
- 'copy' indicates a clone of a published version (before it has been saved as draft).

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>set\_data\_status</code>](#ComplexField+set_data_status)  
**Returns**: <code>String</code> - Derived status as used in IDs for DOM elements.  
<a name="Schema+create_creator"></a>

### schema.create\_creator()
Create the editing form and option-display for a new schema to design from scratch.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
<a name="Schema+create_editor"></a>

### schema.create\_editor()
Create an editing form for this schema. The form contains
- a field to provide a name (read-only if a draft has been saved)
- a field to provide a user-facing title/label (read-only if a version has been published)
- one or more buttons to add fields, and MovingViewers if there are fields already
- submission buttons

**Kind**: instance method of [<code>Schema</code>](#Schema)  
<a name="Schema+from_parent"></a>

### schema.from\_parent(parent)
For clones: fill a clone Schema based on the contents of its parent.

**Kind**: instance method of [<code>Schema</code>](#Schema)  

| Param | Type | Description |
| --- | --- | --- |
| parent | [<code>Schema</code>](#Schema) | Schema of the parent. |

<a name="Schema+setup_copy"></a>

### schema.setup\_copy()
For published versions: create a clone/child as base for a new schema.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
<a name="Schema+create_navbar"></a>

### schema.create\_navbar()
Design the navigation bar and tab contents for this version of the schema.
For a published version, this includes the 'view', 'new draft' (if relevant) and 'copy to new schema',
as well as the 'archive' button.
For a draft version, this includes the 'view' and 'edit' tabs as well as the 'discard' button.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
<a name="Schema+draft_from_publish"></a>

### schema.draft\_from\_publish()
Set up an editor for a draft from a published version

**Kind**: instance method of [<code>Schema</code>](#Schema)  
<a name="Schema+view"></a>

### schema.view()
Show the schema version on the page: create its tabs and render its fields.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
<a name="Schema+save_draft"></a>

### schema.save\_draft(action)
Make final adjustments before posting a draft to be saved or published.

**Kind**: instance method of [<code>Schema</code>](#Schema)  

| Param | Type | Description |
| --- | --- | --- |
| action | <code>String</code> | If 'publish', the draft will be published, otherwise it will just be saved. |

<a name="ComplexField+fields_to_json"></a>

### schema.fields\_to\_json()
Collect the Object-version of the fields into the `properties` property to save as JSON.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>fields\_to\_json</code>](#ComplexField+fields_to_json)  
<a name="ComplexField+display_options"></a>

### schema.display\_options()
Create a modal that offers the different fields that can be added and fill it when shown.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>display\_options</code>](#ComplexField+display_options)  
<a name="ComplexField+view_field"></a>

### schema.view\_field(form_object)
Create a MovingViewer for a field and add it to the editing section of the (mini-)schema.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>view\_field</code>](#ComplexField+view_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field belonging to this schema. |

<a name="ComplexField+add_field"></a>

### schema.add\_field(form_object)
Add a new field to the (mini-)schema.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>add\_field</code>](#ComplexField+add_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be added to this schema. |

<a name="ComplexField+update_field"></a>

### schema.update\_field(form_object)
Update an existing field in a schema.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>update\_field</code>](#ComplexField+update_field)  

| Param | Type | Description |
| --- | --- | --- |
| form_object | [<code>InputField</code>](#InputField) | Field to be updated. |

<a name="ComplexField+replace_field"></a>

### schema.replace\_field(old_id, form_object)
Replace (rename) an existing field in a schema.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>replace\_field</code>](#ComplexField+replace_field)  

| Param | Type | Description |
| --- | --- | --- |
| old_id | <code>String</code> | ID of the field to be replaced. |
| form_object | [<code>InputField</code>](#InputField) | Replacement field. |

<a name="ComplexField+toggle_saving"></a>

### schema.toggle\_saving()
Disable or enable saving a (mini-)schema based on whether any of the existing fields is a duplicate.
Duplicates don't have ids, so we cannot save a schema until that issue is resolved.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>toggle\_saving</code>](#ComplexField+toggle_saving)  
<a name="ComplexField+create_button"></a>

### schema.create\_button() ⇒ <code>HTMLDivElement</code>
Create a button to create more form elements. On click, it updates the value of the `new_field_idx` property.
It also activates the modal that offers the different types of fields.

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>create\_button</code>](#ComplexField+create_button)  
**Returns**: <code>HTMLDivElement</code> - A DIV with the button.  
<a name="ComplexField+reset"></a>

### schema.reset()
Reset the contents of this schema: no fields, initial name

**Kind**: instance method of [<code>Schema</code>](#Schema)  
**Overrides**: [<code>reset</code>](#ComplexField+reset)  
<a name="SchemaGroup"></a>

## SchemaGroup
Class for a schema with all its versions, to render on the page.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| name | <code>String</code> | Name of the schema (shared by all versions). |
| title | <code>String</code> | User-facing label of the schema (shared by all versions). |
| versions | <code>Array.&lt;Object&gt;</code> | List of versions with their name, number and status. |
| statuses | <code>Array.&lt;String&gt;</code> | List of used statuses. |
| urls | [<code>UrlsList</code>](#UrlsList) | Collection of URLs and other info obtained from the server. |
| summary | <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code> | List of versions per status. |


* [SchemaGroup](#SchemaGroup)
    * [new SchemaGroup(name, title, versions, container_id, urls)](#new_SchemaGroup_new)
    * _instance_
        * [.badge_url](#SchemaGroup+badge_url) : <code>String</code>
        * [.status_colors](#SchemaGroup+status_colors) : <code>Object.&lt;String, String&gt;</code>
        * [.load_version(version, nav_bar)](#SchemaGroup+load_version)
    * _static_
        * [.create_badges(version, status)](#SchemaGroup.create_badges) ⇒ <code>Array.&lt;HTMLImageElement&gt;</code>

<a name="new_SchemaGroup_new"></a>

### new SchemaGroup(name, title, versions, container_id, urls)
Create and fill an accordion item and the tabs for the versions of a schema.


| Param | Type | Description |
| --- | --- | --- |
| name | <code>String</code> | Name of the schema. |
| title | <code>String</code> | User-facing label of the schema. |
| versions | <code>Array.&lt;Object&gt;</code> | List of versions with their name, number and status. |
| container_id | <code>String</code> | ID of the DOM element on which the schema is shown. |
| urls | [<code>UrlsList</code>](#UrlsList) | Collection of URLs and other information received from the server. |

<a name="SchemaGroup+badge_url"></a>

### schemaGroup.badge\_url : <code>String</code>
URL for the images that generate the badges.

**Kind**: instance property of [<code>SchemaGroup</code>](#SchemaGroup)  
<a name="SchemaGroup+status_colors"></a>

### schemaGroup.status\_colors : <code>Object.&lt;String, String&gt;</code>
Mapping between status and color of the badge.

**Kind**: instance property of [<code>SchemaGroup</code>](#SchemaGroup)  
<a name="SchemaGroup+load_version"></a>

### schemaGroup.load\_version(version, nav_bar)
Fill in the tab corresponding to a specific version of the schema.
This includes creating a Schema for it and a TemplateReader to retrieve the contents from server-side.

**Kind**: instance method of [<code>SchemaGroup</code>](#SchemaGroup)  

| Param | Type | Description |
| --- | --- | --- |
| version | <code>Object</code> | Information about the version to be loaded. |
| version.number | <code>String</code> | Version number of this version. |
| version.status | <code>String</code> | Status of this version. |
| version.name | <code>String</code> | Name of this schema (=this.name). |
| nav_bar | [<code>NavBar</code>](#NavBar) | Navigation bar and tabs on which the version will be shown. |

<a name="SchemaGroup.create_badges"></a>

### SchemaGroup.create\_badges(version, status) ⇒ <code>Array.&lt;HTMLImageElement&gt;</code>
Create badges for the version number and status of a schema version.

**Kind**: static method of [<code>SchemaGroup</code>](#SchemaGroup)  
**Returns**: <code>Array.&lt;HTMLImageElement&gt;</code> - Version and status badges.  

| Param | Type | Description |
| --- | --- | --- |
| version | <code>String</code> | Version number of the schema version. |
| status | <code>String</code> | Status of a schema version. |

<a name="SchemaForm"></a>

## SchemaForm
Class for a published version of a schema to be used when applying metadata.

**Kind**: global class  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| name | <code>String</code> | Name of the schema. |
| title | <code>String</code> | User-facing label/title of the schema. |
| container_id | <code>String</code> | ID of the DIV to which the form will be attached. |
| prefix | <code>String</code> | Prefix of the metadata attribute names, e.g. `msg.book`. |
| realm | <code>String</code> | Name of the realm to which the schema belongs. |
| version | <code>String</code> | Version number of the current schema version. |
| parent | <code>String</code> | Name of the schema this schema was cloned from, if relevant. (Not implemented) |
| fields | <code>Object.&lt;String, InputField&gt;</code> | Collection of fields that constitute this schema. |
| field_ids | <code>Array.&lt;String&gt;</code> | Ordered list of IDs of the fields. |
| form | <code>HTMLFormElement</code> | Form used to implement the metadata annotation. |


* [SchemaForm](#SchemaForm)
    * [new SchemaForm(json, container_id, prefix)](#new_SchemaForm_new)
    * _instance_
        * [.from_json(schema_json)](#SchemaForm+from_json)
        * [.add_annotation(annotated_data)](#SchemaForm+add_annotation)
        * [.register_object(obj, annotated_data, object_fields, prefix)](#SchemaForm+register_object)
        * [.register_non_object(fid, annotated_data, form)](#SchemaForm+register_non_object)
    * _static_
        * [.flatten_object(object_editor, flattened_id)](#SchemaForm.flatten_object)

<a name="new_SchemaForm_new"></a>

### new SchemaForm(json, container_id, prefix)
Create a form to apply metadata from a schema.


| Param | Type | Description |
| --- | --- | --- |
| json | [<code>SchemaInfo</code>](#SchemaInfo) | Contents of the JSON file on which the schema is stored. |
| container_id | <code>String</code> | ID of the DIV to which the form will be attached. |
| prefix | <code>String</code> | Prefix of the metadata attribute names, e.g. `msg.book`. |

<a name="SchemaForm+from_json"></a>

### schemaForm.from\_json(schema_json)
Create the form with all its fields.

**Kind**: instance method of [<code>SchemaForm</code>](#SchemaForm)  

| Param | Type | Description |
| --- | --- | --- |
| schema_json | <code>Object.&lt;String, FieldInfo&gt;</code> | Collection of Object-versions of fields. |

<a name="SchemaForm+add_annotation"></a>

### schemaForm.add\_annotation(annotated_data)
Fill in the form with existing metadata.

**Kind**: instance method of [<code>SchemaForm</code>](#SchemaForm)  

| Param | Type | Description |
| --- | --- | --- |
| annotated_data | <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code> | Key-value pairs with the existing metadata. |

<a name="SchemaForm+register_object"></a>

### schemaForm.register\_object(obj, annotated_data, object_fields, prefix)
Retrieve the annotated data corresponding to fields inside a given composite field.

**Kind**: instance method of [<code>SchemaForm</code>](#SchemaForm)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| obj | <code>String</code> |  | Flattened ID of the composite field. |
| annotated_data | <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code> |  | Key-value pairs with the existing metadata. |
| object_fields | <code>Array.&lt;String&gt;</code> |  | Flattened IDs of fields inside composite fields. |
| prefix | <code>String</code> | <code></code> | Prefix common to all these fields. |

<a name="SchemaForm+register_non_object"></a>

### schemaForm.register\_non\_object(fid, annotated_data, form)
Register the annotated value of a specific (non composite) field.

**Kind**: instance method of [<code>SchemaForm</code>](#SchemaForm)  

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| fid | <code>String</code> |  | Flattened ID of the field to fill in. |
| annotated_data | <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code> |  | Key-value pairs with the existing metadata. |
| form | <code>HTMLFormElement</code> \| <code>HTMLDivElement</code> | <code></code> | Form or div element inside which we can find the input field to fill in. |

<a name="SchemaForm.flatten_object"></a>

### SchemaForm.flatten\_object(object_editor, flattened_id)
Recursive function that assigns a `name` property to each field with the flattened id.

**Kind**: static method of [<code>SchemaForm</code>](#SchemaForm)  

| Param | Type | Description |
| --- | --- | --- |
| object_editor | [<code>SchemaForm</code>](#SchemaForm) \| [<code>ObjectEditor</code>](#ObjectEditor) | Schema or mini-schema for a composite field. |
| flattened_id | <code>String</code> | Prefix to be added to the id of a field. |

<a name="url_tag"></a>

## url\_tag : <code>HTMLElement</code>
DOM element containing the information for the list ofr URLs.

**Kind**: global variable  
<a name="urls"></a>

## urls : [<code>UrlsList</code>](#UrlsList)
**Kind**: global variable  
<a name="schema_pattern"></a>

## schema\_pattern : <code>String</code>
REGEX Pattern to control possible schema names. This pattern is then filled with existing names.

**Kind**: global variable  
<a name="starting_schema"></a>

## starting\_schema : [<code>Schema</code>](#Schema)
Empty schema to start with.

**Kind**: global variable  
<a name="container_id"></a>

## container\_id : <code>String</code>
ID of the DOM element to hook the form to.

**Kind**: global constant  
<a name="container"></a>

## container : <code>HTMLElement</code>
DOM element to hook the form to. It should also have several attributes with necessary info.

**Kind**: global constant  
<a name="container_id"></a>

## container\_id : <code>String</code>
ID of the DOM element to which all the code will be hooked.

**Kind**: global constant  
<a name="container"></a>

## container : <code>HTMLDivElement</code>
DOM element to which all the code will be hooked. The BS5 class 'accordion' is enforced.

**Kind**: global constant  
<a name="schemas"></a>

## schemas : <code>Object.&lt;String, Array.&lt;String&gt;&gt;</code>
Register of existing schemas

**Kind**: global constant  
<a name="FieldInfo"></a>

## FieldInfo : <code>Object</code>
Representation of a field to be saved as JSON.

**Kind**: global typedef  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| title | <code>String</code> | User-facing label of the field, to be printed in the form and the rendering. |
| type | <code>String</code> | Type of input, to be defined in the specific class or among choices for a simple field. |
| [required] | <code>Boolean</code> | Whether the field will be required in the form. |
| [default] | <code>String</code> | If the field is required (and even then, optionally), the default value in the field. |
| [repeatable] | <code>Boolean</code> | For simple fields, whether the field can be repeated in the form. |
| [minimum] | <code>String</code> | For simple fields with numeric type, the minimum possible value. |
| [maximum] | <code>String</code> | For simple fields with numeric type, the maximum possible value. |
| [multiple] | <code>Boolean</code> | For multiple-choice fields, whether only multiple values can be chosen. |
| [ui] | <code>String</code> | For multiple-choice fields, whether the field is rendered as "dropdown", "checkbox" or "radio". |
| [values] | <code>Array.&lt;String&gt;</code> | For multiple-choice fields, the list of options. |
| [properties] | <code>Object</code> | For composite fields, the collection of subfields. |

<a name="SchemaInfo"></a>

## SchemaInfo : <code>Object</code>
Information about a schema from the backend.

**Kind**: global typedef  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| name | <code>String</code> | Name of the schema. |
| schema_info | <code>Object</code> | Information about the schema. |
| schema_info.archived | <code>Boolean</code> | Whether all existing versions are archived. |
| schema_info.published | <code>Boolean</code> | Whether there is a published version. |
| schema_info.draft | <code>Boolean</code> | Whether there is a draft version. |
| schema_info.draft_count | <code>Number</code> | The number of existing draft versions (max = 1). |
| schema_info.published_count | <code>Number</code> | The number of existing published versions (max = 1). |
| schema_info.total_count | <code>Number</code> | The number of existing versions. |
| schema_info.published_name | <code>String</code> | The filename of the published version. |
| schema_info.draft_name | <code>String</code> | The filename of the draft version. |
| schema_info.latest_version | <code>String</code> | The version number (in semantic versioning) of the latest version. |
| schema_info.versions_sorted | <code>Array.&lt;String&gt;</code> | The existing version numbers. |
| schema_info.realm | <code>String</code> | Realm to which the schema belongs. |
| schema_info.title | <code>String</code> | User-facing label of the schema. |
| schema_info.timestamp | <code>Number</code> | ??? |
| url | <code>String</code> | URL template to retrieve the contents of a version of the schema. |

<a name="SchemaContents"></a>

## SchemaContents : <code>Object</code>
JSON representation of a schema.

**Kind**: global typedef  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| schema_name | <code>String</code> | Name of the schema. |
| version | <code>String</code> | Version number of the schema version. |
| status | <code>String</code> | Status of the schema version ('draft', 'published' or 'archived). |
| title | <code>String</code> | User-facing label of the schema. |
| edited_by | <code>String</code> | User that has last edited the schema. |
| realm | <code>String</code> | Realm to which the schema belongs. |
| parent | <code>String</code> | If relevant, name and version number of the schema from which this schema emerged. |
| properties | <code>Object</code> | Collection of fields that constitute the schema. |

<a name="UrlsList"></a>

## UrlsList : <code>Object</code>
Collection of URLS to communicate with the backend.

**Kind**: global typedef  
**Properties**

| Name | Type | Description |
| --- | --- | --- |
| new | <code>String</code> | The URL to post a schema version on creation, editing or publication. |
| list | <code>String</code> | The URL to retrieve the list of existing schemas. |
| delete | <code>String</code> | The URL to delete a draft. |
| archive | <code>String</code> | The URL to archive a published version. |
| realm | <code>String</code> | Name of the realm to which the schema belongs. |
| schema_name | <code>String</code> | Name of the latest modified schema. |
| schema_version | <code>String</code> | Version number of the latest modified schema version. |


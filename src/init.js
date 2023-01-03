let editing_schema = new Schema('schemaEditor');
editing_schema.init_modal();
let button = document.getElementById('newSchema');
button.setAttribute('data-bs-toggle', 'modal');
button.setAttribute('data-bs-target', '#schemaEditor');

/**
 * Collection of URLS to communicate with the backend.
 * 
 * @typedef {Object} UrlsList
 * @property {String} new - The URL to post a schema version on creation, editing or publication.
 * @property {String} list - The URL to retrieve the list of existing schemas.
 * @property {String} delete - The URL to delete a draft.
 * @property {String} archive - The URL to archive a published version.
 * @property {String} realm - Name of the realm to which the schema belongs.
 * @property {String} schema_name - Name of the latest modified schema.
 * @property {String} schema_version - Version number of the latest modified schema version.
 */


const container_id = 'metadata_template_list_container';
const container = document.getElementById(container_id);
container.className = 'accordion accordion-flush';

let url_tag = document.getElementsByTagName('url-list')[0];
let url_list = url_tag.attributes;
let urls = {};
for (let url of url_list) {
	urls[url.name.replace('-', '_')] = url.value;
}
url_tag.remove();
const realm = urls.realm;

const schemas = {};
let schema_pattern = "[a-z0-9-_]+";

// first the button
let starting_schema = new Schema('schema-editor-100', container_id, urls);
starting_schema.create_creator();

let templates_request = new TemplatesRequest(urls, container_id);
templates_request.retrieve();

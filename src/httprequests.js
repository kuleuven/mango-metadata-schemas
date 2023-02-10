class MangoRequest extends XMLHttpRequest {
    constructor(url) {
        super();
        this.url = url;
    }
    
    get json() {
        return JSON.parse(this.responseText);
    }

    retrieve() {
        this.open("GET", this.url);
        this.send();
    }
}

class TemplatesRequest extends MangoRequest {
    constructor(urls, container_id) {
        super(urls.list);
        this.parse_response(container_id, urls);
    }

    parse_response(container_id, urls) {
        this.addEventListener('load', () => {
            let grouped_templates = this.json;
            for (let template of Object.keys(grouped_templates)) {
                let re = /(?<name>.*)-v(?<version>\d\.\d\.\d)-(?<status>|published|draft).json/
                let this_template = grouped_templates[template];
                let versions = [
                    this_template.published_count > 0 ? this_template.published_name.match(re).groups : {},
                    this_template.draft_count > 0 ? this_template.draft_name.match(re).groups : {}
                ];
                new SchemaGroup(template, versions, container_id, urls) // this will create the schemas, which will load on demand
            }
        })
    }

}


class TemplateReader extends MangoRequest {
    constructor(url, schema) {
        super(url);
        this.parse_response(schema);
    }

    parse_response(schema) {
        this.addEventListener('load', () => {
            let json = Object.values(this.json)[0];
            schema.from_json(json);
            schema.view();
        })
    }
}

class AnnotationRequest extends MangoRequest {
    constructor(schema_url, annotated_data, prefix) {
        super(schema_url);
        console.log(schema_url)
        this.parse_response(annotated_data, prefix);
    }

    parse_response(annotated_data, prefix) {
        this.addEventListener('load', () => {
            let json = this.json;
            let schema = new SchemaForm(Object.keys(json)[0], container_id, 'posting_url', prefix);
            schema.from_json(Object.values(json)[0], annotated_data);
        })
    }
}

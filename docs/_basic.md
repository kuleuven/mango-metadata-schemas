```json
{
    "schema_name": "book",
    "version": "1.0.0",
    "status": "draft",
    "properties": {
        "title": {
            "type": "text",
            "title": "Book title",
            "required": true,
            "help": "Title of the book"
        },
        "cover_colors": {
            "type": "select",
            "multiple": true,
            "ui": "checkbox",
            "title": "Colors in the cover",
            "values": [
                "red",
                "blue",
                "green",
                "yellow"
            ],
            "help": "Colors in the cover"
        },
        "publisher": {
            "type": "select",
            "multiple": false,
            "ui": "dropdown",
            "values": [
                "Penguin House",
                "Tor",
                "Corgi",
                "Nightshade books"
            ],
            "title": "Publishing house",
            "required": true,
            "help": "Company that published the book."
        },
        "author": {
            "type": "object",
            "title": "Author",
            "help": "The person who wrote the book",
            "properties": {
                "name": {
                    "type": "text",
                    "title": "Name and Surname",
                    "required": true,
                    "help": "Input type: text"
                },
                "age": {
                    "type": "integer",
                    "title": "Age",
                    "minimum": "12",
                    "maximum": "99",
                    "help": "Input type: integer between 12 and 99"
                },
                "email": {
                    "type": "email",
                    "title": "Email address",
                    "required": true,
                    "repeatable": true,
                    "help": "Input type: email"
                }
            }
        },
        "ebook": {
            "type": "select",
            "multiple": false,
            "ui": "radio",
            "values": [
                "Available",
                "Unavailable"
            ],
            "title": "Is there an e-book?",
            "required": true
        },
        "genre": {
            "type": "select",
            "multiple": true,
            "ui": "dropdown",
            "values": [
                "Speculative fiction",
                "Mystery",
                "Non-fiction",
                "Encyclopaedia",
                "Memoir",
                "Literary fiction"
            ],
            "title": "Genre"
        },
        "publishing_date": {
            "type": "date",
            "title": "Publishing date",
            "required": true,
            "repeatable": true
        },
        "copies_published": {
            "type": "integer",
            "title": "Number of copies published",
            "minimum": "100"
        },
        "market_price": {
            "type": "float",
            "title": "Market price (in euros)",
            "minimum": "0.99",
            "maximum": "999.99"
        },
        "website": {
            "type": "url",
            "title": "Website"
        },
        "synopsis": {
            "type": "textarea",
            "title": "Synopsis"
        }
    },
    "title": "Book schema as an example",
    "edited_by": "username",
    "realm": "project_collection",
    "parent": ""
}
```
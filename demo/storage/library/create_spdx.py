import json
import requests
from pathlib import Path

lib_dir = Path("storage", "vocabularies")

spdx_request = requests.get(
    "https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json"
)
spdx_json = spdx_request.json()

field_base = {
    "name": "license",
    "data": {
        "title": "License",
        "type": "select",
        "values": [x["name"] for x in spdx_json["licenses"]],
        # "values": {x["licenseId"]: x["name"] for x in spdx_json["licenses"]},
        "multiple": False,
        "ui": "dropdown",
        "help": "Choose a License name.",
    },
    "source": "the <a href='https://github.com/spdx/license-list-data/tree/main'>SPDX License list</a>",
    "tags": [],
}

filename = lib_dir / "library_007.json"
filename.write_text(json.dumps(field_base))

import sqlite3
import os
from pprint import pprint

ICAT_PATH = "storage/demo/mango/realms/demo/icat.db"


# mock classes
class DemoAVU:
    def __init__(self, name, value, units=None):
        self.name = name
        self.value = value
        self.units = units
        self.as_tuple = (self.name, self.value, self.units)

    def __str__(self):
        return f"<mock iRODSMeta {self.name} {self.value} ${self.units}>"

    def to_json(self):
        return {"name": self.name, "value": self.value, "units": self.units}


class DemoItem:
    def __init__(self, item_type, path=None):
        self.type = item_type
        self.id = "demo-" + item_type
        self.path = (
            "/home/demo/demo/paint_samples/sample_001.png"
            if item_type == "data_object"
            else "/home/demo/demo/paint_samples/"
        )
        self.name = "sample_001.png" if item_type == "data_object" else "paint_samples"
        self.retrieve_metadata()

    def apply_operations(self, operations):
        con = sqlite3.connect(ICAT_PATH)
        cur = con.cursor()
        for operation, avu in operations:
            if operation == "remove":
                if avu.units is None:
                    cur.execute(
                        "DELETE FROM icat WHERE name=? AND value=? AND units IS NULL",
                        (avu.name, avu.value),
                    )
                else:
                    cur.execute(
                        "DELETE FROM icat WHERE name=? AND value=? AND units=?",
                        (avu.name, avu.value, avu.units),
                    )
            elif operation == "add":
                cur.execute("INSERT INTO icat VALUES(?, ?, ?)", avu.as_tuple)
            else:
                pass
        con.commit()
        self.update_metadata(cur)
        con.close()

    def update_metadata(self, cur):
        res = cur.execute("SELECT name, value, units FROM icat")
        new_metadata = res.fetchall()
        self.metadata = (
            [DemoAVU(name, value, units) for name, value, units in new_metadata]
            if len(new_metadata) > 0
            else []
        )

    def retrieve_metadata(self):
        con = sqlite3.connect(ICAT_PATH)
        cur = con.cursor()
        self.update_metadata(cur)
        con.close()


# hardcoded variables
demo_collection = DemoItem("collection")
demo_data_object = DemoItem("data_object")

from tinydb import TinyDB

db = TinyDB('db.json', indent=4)

doc = {"name": "Ali Vali", "age": 20}

db.insert(doc)
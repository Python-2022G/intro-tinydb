from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB('db.json', indent=4)

doc = db.contains(doc_id=3)
print(doc)
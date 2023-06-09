from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB('db.json', indent=4)

docs = db.all()
print(docs)
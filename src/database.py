from pymongo import MongoClient
_mongo = None
def get_client(uri=None):
    global _mongo
    if _mongo is None and uri is not None:
        _mongo = MongoClient(uri)
    return _mongo

#def change_client(uri):
#    global _mongo
#    _mongo = MongoClient(uri)

def get_collection(database_name, collection_name):
    db = get_client()[database_name]
    return db[collection_name]
import tinydb


def getoverlays(stylenum):
    Query = tinydb.Query()
    db = tinydb.TinyDB("../bin/data/overlays.json")
    instances = db.search(Query.style == stylenum)[0]
    out = list(instances.values())
    out.pop(0)
    return out

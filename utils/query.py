from pymongo.collection import Collection

def indexedSearch(query, coll: Collection):
    result = coll.find({
        "$text": {
            "$search": query,
            "$caseSensitive": False
        }
    })
    
    result.sort([('score', -1)]) # Ordena por similaridade
    
    return result
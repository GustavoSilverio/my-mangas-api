from pymongo.collection import Collection

def mangasSummaryByQuery(query, coll: Collection):
    result = coll.find({
        "$text": {
            "$search": query,
            "$caseSensitive": False
        }
    }, { "nome": 1, "imgCapa": 1 })
    
    result.sort([('score', -1)]) # Ordena por similaridade
    return result
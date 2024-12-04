import uvicorn
from os import environ
from dotenv import load_dotenv
from pymongo import MongoClient, TEXT
from bson.objectid import ObjectId
from typing import List
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models.manga import Manga
from utils.query import mangasSummaryByQuery
from utils.auth import createToken, validateToken
from utils.exceptions import raiseResponseException

load_dotenv()
MONGO_BASE_URL = environ.get("MONGO_BASE_URL")
ORIGIN = environ.get("ORIGIN")
ACCESS_KEY = environ.get("ACCESS_KEY")

client = MongoClient(MONGO_BASE_URL)
db = client["my-mangas"]
coll = db["manga"]

coll.create_index([("nome", TEXT)])


app = FastAPI(
    title="my-mangas-api",
    version="1.1.0",
    openapi_components={
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    },
    openapi_security=[{"BearerAuth": []}]
)

origins = [ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthy")
def readRoot():
    return { "hello": "mundo" }

@app.get("/mangas-summary") 
def getAllMangas(q: str | None = None, _: str = Depends(validateToken)):
    if q:
        mangas_cursor = mangasSummaryByQuery(q, coll)
    else:
        mangas_cursor = coll.find({}, { "nome": 1, "imgCapa": 1 })
    
    mangas_list : List[Manga] = []
    
    mangas : List[Manga] = [mangas for mangas in mangas_cursor]
    
    for manga in mangas:
        manga["_id"] = str(manga["_id"])
        mangas_list.append(manga)
        
    return mangas_list

@app.get("/manga/{id}")
def getMangaById(id: str, _: str = Depends(validateToken)):
    manga = coll.find_one({ "_id": ObjectId(id) })
    
    manga["_id"] = str(manga["_id"])
    
    return manga  
    

@app.post("/validate")
def validate_key(key: str):
    if key == ACCESS_KEY:
        return { "isValid": True, "token": createToken() }
    else:
        raiseResponseException(400, "Key provided not valid", "key.not-valid")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

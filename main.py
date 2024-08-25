import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pymongo import MongoClient
from typing import List
from models.manga import Manga
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

load_dotenv()

app = FastAPI()
client = MongoClient(os.get)
db = client["my-mangas"]
coll = db["manga"]

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthy")
def readRoot():
    return { "hello": "world" }

@app.get("/mangas")
def getAllMangas():
    mangas_cursor = coll.find()
    
    mangas_list : List[Manga] = []
    
    mangas : List[Manga] = [mangas for mangas in mangas_cursor]
    
    for manga in mangas:
        manga["_id"] = str(manga["_id"])
        mangas_list.append(manga)
        
    return mangas_list 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
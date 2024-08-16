from typing import TypedDict, List
from bson import objectid

class Capitulo(TypedDict):
    nomeCapitulo: str
    paginas: List[str]

class Manga(TypedDict):
    _id: objectid
    nome: str
    capitulos: List[Capitulo]
from typing import Dict, List

from fastapi import FastAPI

app = FastAPI()

produtos: List[Dict[str, any]] = [ # type: ignore
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Smartphone com tela de 6.5 polegadas",
        "preco": 1999.99,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Notebook com processador Intel i7",
        "preco": 4999.99,
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Tablet com tela de 10 polegadas",
        "preco": 899.99,
    }
]

@app.get("/")
def ola_mundo():
    return {"message": "Olá, mundo!"}

@app.get("/produtos")
def listar_produtos():
    return produtos
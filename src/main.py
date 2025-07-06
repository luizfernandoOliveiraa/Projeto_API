from fastapi import FastAPI, HTTPException
from .schema import ProdutosSchema  # type: ignore
from .data import produtos  # type: ignore
from typing import List
app = FastAPI()

@app.get("/produtos", response_model=List[ProdutosSchema])  # type: ignore
def listar_produtos():
    return produtos

@app.get("/produtos/{produto_id}", response_model=ProdutosSchema)  # type: ignore
async def obter_produto(produto_id: int):
    for produto in produtos:
        if produto["id"] == produto_id:
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.post("/produtos", response_model=ProdutosSchema)  # type: ignore
def criar_produto(produto: ProdutosSchema):
    novo_produto = produto.model_dump()
    novo_produto["id"] = len(produtos) + 1
    produtos.append(novo_produto)
    return novo_produto


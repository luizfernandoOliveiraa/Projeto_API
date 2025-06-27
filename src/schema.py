from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat   
    

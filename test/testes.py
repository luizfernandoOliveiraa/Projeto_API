from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200
    
def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"message": "Olá, mundo!"}
    
def testar_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3
    
def test_pegar_produto():
    response = client.get("/produtos/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Smartphone com tela de 6.5 polegadas",
        "preco": 1999.99,
    }
    
def test_produto_inexistente():
    response = client.get("/produtos/999")
    assert response.json() == {"detail": "Produto não encontrado"}


def test_criar_produto():
    response = client.post("/produtos", json={
        "nome": "Novo Produto",
        "descricao": "Descrição do novo produto",
        "preco": 100.00
    })
    assert response.status_code == 200
    
    

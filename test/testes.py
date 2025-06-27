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
    

import pytest
from app import app

def test_caso_automatizado():
    client = app.test_client()
    response = client.get('/')
    # Requisito de validar que la respuesta sea exitosa (HTTP 200)
    assert response.status_code == 200
import pytest
from app import app

def test_caso_automatizado():
    client = app.test_client()
    response = client.get('/')
    # Verifica que la app responda con éxito
    assert response.status_code == 200
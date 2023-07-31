import pytest
import httpx
from main import app


@pytest.fixture
async def client():
    async with httpx.AsyncClient(app=app, base_url="http://testserver") as client:
        yield client


async def test_generate_response(client):
    # Test case for generating a response
    prompt = "Tell me a joke."
    response = await client.get(f"/generate-response/?prompt={prompt}")
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert isinstance(data["response"], str)
    assert len(data["response"]) > 0


async def test_generate_response_missing_prompt(client):
    # Test case for missing prompt in the request
    response = await client.get("/generate-response/")
    assert response.status_code == 400


async def test_generate_response_empty_prompt(client):
    # Test case for an empty prompt in the request
    response = await client.get("/generate-response/?prompt=")
    assert response.status_code == 400

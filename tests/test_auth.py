import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_register_and_login():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Регистрация
        resp = await client.post("/auth/register", json={
            "email": "test@example.com",
            "password": "secret123",
            "full_name": "Test User"
        })
        assert resp.status_code == 201

        # Вход
        resp = await client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "secret123"
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
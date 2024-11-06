from typing import Dict

from fastapi.testclient import TestClient
from pydantic import UUID4

USERNAME = 'test_user'


def create_user(api_client: TestClient, payload: Dict):
    return api_client.post("v1/user/create", json=payload)


def get_all_users(api_client: TestClient):
    return api_client.get("v1/user/get")


def get_user(api_client: TestClient, user_uuid: UUID4):
    return api_client.get(f"v1/user/get/{user_uuid}")

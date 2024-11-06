import pytest
from fastapi.testclient import TestClient

from app.schemas.user import UserOut
from tests.utils.user import create_user, get_all_users, get_user

pytestmark = pytest.mark.usefixtures("use_postgres")
user_payload = {
    'first_name': 'admin',
    'last_name': 'admin',
    'username': 'admin',
    'email': 'admin@admin.ru',
    'date_of_birth': '2000-01-01'
}


class TestCreateUser:
    def test_ok(self, api_client: TestClient) -> None:
        response = create_user(
            api_client=api_client, payload=user_payload)

        assert response.status_code == 201
        user = response.json()
        assert isinstance(user, dict)
        assert user.get("username") == 'admin'

    def test_if_user_exists(self, api_client: TestClient) -> None:
        create_user(api_client=api_client, payload=user_payload)
        response = create_user(
            api_client=api_client, payload=user_payload)
        assert response.status_code == 422


class TestGetAllUsers:
    def test_ok_if_empty(self, api_client: TestClient) -> None:
        response = get_all_users(api_client=api_client)

        assert response.status_code == 200
        assert response.json() == []

    def test_if_not_empty(self, api_client: TestClient) -> None:
        create_user(api_client=api_client, payload=user_payload)

        response = get_all_users(api_client=api_client)

        assert response.status_code == 200
        assert len(response.json()) == 1


class TestGetUser:
    # def test_ok_if_empty(self, api_client: TestClient) -> None:
    #     response = get_all_users(api_client=api_client)

    #     assert response.status_code == 200
    #     assert response.json() == []

    def test_if_exist(self, api_client: TestClient) -> None:
        user_data = create_user(
            api_client=api_client, payload=user_payload)
        user = user_data.json()
        user_uuid = user.get('id')

        response = get_user(api_client=api_client, user_uuid=user_uuid)
        assert response.status_code == 200
        # assert len(response.json()) == 1

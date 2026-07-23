import pytest

from config import Credentials
from src.api.base.api_manager import ApiManager
from src.utils.data_generator import user_auth_data
from src.utils.data_generator import INVALID_USER_PAYLOADS


@pytest.fixture(params=INVALID_USER_PAYLOADS, ids=lambda data: data[1])
def invalid_user_payload(request):
    payload, case_desc = request.param
    return payload


@pytest.fixture(scope="session")
def api():
    manager = ApiManager(base_url=Credentials.URL)
    yield manager
    manager.http.close()


@pytest.fixture
def auth_token(api):
    response = api.users.login_user_get_tokens(user_auth_data())
    response_data = response.json()
    return response_data.get("accessToken") or response_data.get("token")

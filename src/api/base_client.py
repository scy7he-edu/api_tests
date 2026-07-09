import httpx

from config import Credentials


class BaseClient:
    def __init__(self):
        self.client = httpx.Client(base_url=Credentials.URL)

    def _make_request(self, method: str, endpoint: str, **kwargs):
        print(f"\n---> {method} to {endpoint}")
        rq = self.client.request(method, endpoint, **kwargs)
        print(f"<--- Server Response code: {rq.status_code}")
        return rq

    @staticmethod
    def base_assertion(response, response_code: int):
        assert response.status_code == response_code
        response_data = response.json()
        assert isinstance(response_data, dict)
        return response_data

    # @staticmethod
    # def key_assertion(data: list, *args):
    #     assert isinstance(data, list)
    #     for item in data:
    #         for key in args:
    #             assert key in item

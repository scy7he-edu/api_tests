import allure
import httpx

from config import Credentials


class BaseClient:
    def __init__(self):
        self.client = httpx.Client(base_url=Credentials.URL)

    def _make_request(self, method: str, endpoint: str, **kwargs):
        print(f"\n---> {method} to {endpoint}")
        rq = self.client.request(method, endpoint, **kwargs)
        print(f"<--- Server Response code: {rq.status_code}")

        allure.attach(
            body=f"Method: {method}\nURL: {rq.url}\nPayload: {kwargs.get('json', {})}",
            name="API Request details",
            attachment_type=allure.attachment_type.TEXT,
        )

        allure.attach(
            body=f"Status code: {rq.status_code}\nResponse body:\n{rq.text}",
            name="Api Response details",
            attachment_type=allure.attachment_type.TEXT,
        )
        return rq

    @staticmethod
    def base_assertion(response, response_code: int):
        assert response.status_code == response_code
        response_data = response.json()
        assert isinstance(response_data, dict)
        return response_data

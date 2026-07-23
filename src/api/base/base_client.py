import allure
import httpx


class BaseClient:
    def __init__(self, client: httpx.Client):
        self.client = client

    def _get(self, endpoint: str, **params):
        return self._make_request(
            "GET", endpoint, params={k: v for k, v in params.items() if v is not None}
        )

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

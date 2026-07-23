from src.api.base.base_client import BaseClient


class QuotesClient(BaseClient):
    def get_all_quotes(self):
        return self._make_request("GET", "/quotes")

    def get_single_quote(self, quote_id: int):
        return self._make_request("GET", f"/quotes/{quote_id}")

    def get_random_quote(self):
        return self._make_request("GET", "/quotes/random")

    def limit_skip_quotes(self, limit: int, skip: int):
        return self._make_request("GET", f"/quotes?limit={limit}&skip={skip}")

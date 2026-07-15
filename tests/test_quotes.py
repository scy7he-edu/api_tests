import pytest

from src.api.base_client import BaseClient
from src.schemas.quotes_schemas import QuotesSchema, QuotesListSchema


@pytest.mark.quotes
class TestQuotes:
    @pytest.mark.positive
    def test_get_all_quotes(self, quotes_client):
        response = quotes_client.get_all_quotes()
        response_data = BaseClient.base_assertion(response, 200)
        QuotesListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_quote(self, quotes_client):
        response = quotes_client.get_single_quote(1)
        response_data = BaseClient.base_assertion(response, 200)
        QuotesSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_random_quote(self, quotes_client):
        response = quotes_client.get_random_quote()
        response_data = BaseClient.base_assertion(response, 200)
        QuotesSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_quotes(self, quotes_client):
        response = quotes_client.limit_skip_quotes(3, 10)
        response_data = BaseClient.base_assertion(response, 200)
        QuotesListSchema.model_validate(response_data)

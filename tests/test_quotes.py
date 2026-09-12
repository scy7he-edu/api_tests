import pytest

from src.utils.assertions import Asserts
from src.api.quotes.quotes_schemas import QuoteListResponseSchema, QuoteResponseSchema
from src.utils.data_generator import invalid_ids


@pytest.mark.quotes
class TestQuotes:
    @pytest.mark.positive
    def test_get_all_quotes(self, api):
        response = api.quotes.get_all_quotes()
        response_data = Asserts.base_assertion(response, 200)
        assert len(response_data["quotes"]) > 0
        QuoteListResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_quote(self, api):
        response = api.quotes.get_single_quote(1)
        response_data = Asserts.base_assertion(response, 200)
        QuoteResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_random_quote(self, api):
        response = api.quotes.get_random_quote()
        response_data = Asserts.base_assertion(response, 200)
        QuoteResponseSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_quotes(self, api):
        limit = 3
        skip = 10
        response = api.quotes.limit_skip_quotes(limit=limit, skip=skip)
        response_data = Asserts.base_assertion(response, 200)
        assert response_data["limit"] == limit
        assert response_data["skip"] == skip
        assert len(response_data["quotes"]) == limit
        QuoteListResponseSchema.model_validate(response_data)


class TestQuotesNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_quote_id", invalid_ids(5, 9999, 99999))
    def test_get_invalid_quote(self, api, invalid_quote_id):
        response = api.quotes.get_single_quote(invalid_quote_id)
        assert response.status_code == 404

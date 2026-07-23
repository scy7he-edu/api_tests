class Asserts:
    @staticmethod
    def base_assertion(response, response_code: int):
        assert response.status_code == response_code
        response_data = response.json()
        assert isinstance(response_data, dict)
        return response_data

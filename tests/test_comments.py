import pytest

from config import Credentials
from src.api.base_client import BaseClient
from src.schemas.comments_schemas import CommentSchema, CommentListSchema

credentials = Credentials()


@pytest.mark.comments
class TestComments:
    @pytest.mark.positive
    def test_get_all_comments(self, comments_client):
        response = comments_client.get_all_comments()
        response_data = BaseClient.base_assertion(response, 200)
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_comment(self, comments_client):
        response = comments_client.get_single_comment(1)
        response_data = BaseClient.base_assertion(response, 200)
        CommentSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_comments(self, comments_client):
        selection = ["body", "postId"]
        response = comments_client.limit_skip_comments(10, 10, *selection)
        response_data = BaseClient.base_assertion(response, 200)
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_comments_by_post_id(self, comments_client):
        response = comments_client.get_comments_by_post_id(6)
        response_data = BaseClient.base_assertion(response, 200)
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_new_comment(self, comments_client):
        response = comments_client.add_new_comment(credentials.comment_data)
        BaseClient.base_assertion(response, 201)

    @pytest.mark.positive
    def test_update_comment(self, comments_client):
        response = comments_client.update_comment(1)
        BaseClient.base_assertion(response, 200)

    @pytest.mark.positive
    def test_delete_comment(self, comments_client):
        response = comments_client.delete_comment(1)
        assert response.status_code == 200

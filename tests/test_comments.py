import pytest

from src.utils.assertions import Asserts
from src.utils.data_generator import comment_data, invalid_ids
from src.api.comments.comments_schemas import CommentSchema, CommentListSchema


@pytest.mark.comments
class TestComments:
    @pytest.mark.positive
    def test_get_all_comments(self, api):
        response = api.comments.get_all_comments()
        response_data = Asserts.base_assertion(response, 200)
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_comment(self, api):
        response = api.comments.get_single_comment(1)
        response_data = Asserts.base_assertion(response, 200)
        CommentSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_comments(self, api):
        selection = ["body", "postId"]
        response = api.comments.limit_skip_comments(10, 10, *selection)
        response_data = Asserts.base_assertion(response, 200)
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_comments_by_post_id(self, api):
        response = api.comments.get_comments_by_post_id(6)
        response_data = Asserts.base_assertion(response, 200)
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_new_comment(self, api):
        response = api.comments.add_new_comment(comment_data())
        Asserts.base_assertion(response, 201)

    @pytest.mark.positive
    def test_update_comment(self, api):
        response = api.comments.update_comment(1, comment_data())
        Asserts.base_assertion(response, 200)

    @pytest.mark.positive
    def test_delete_comment(self, api):
        response = api.comments.delete_comment(1)
        assert response.status_code == 200


class TestCommentsNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_comment_id", invalid_ids(5, 99999, 999999))
    def test_get_invalid_comment(self, api, invalid_comment_id):
        response = api.comments.get_single_comment(invalid_comment_id)
        assert response.status_code == 404

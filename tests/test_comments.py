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
        assert len(response_data["comments"]) > 0
        CommentListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_comment(self, api):
        response = api.comments.get_single_comment(1)
        response_data = Asserts.base_assertion(response, 200)
        CommentSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_comments(self, api):
        limit = 10
        skip = 10
        selection = ["body", "postId"]
        response = api.comments.limit_skip_comments(limit, skip, *selection)
        response_data = Asserts.base_assertion(response, 200)
        assert response_data["limit"] == limit
        assert response_data["skip"] == skip
        assert len(response_data["comments"]) == limit

        expected_fields = set(selection) | {"id"}
        for comment in response_data["comments"]:
            assert set(comment.keys()) == expected_fields

    @pytest.mark.positive
    def test_get_comments_by_post_id(self, api):
        post_id = 6
        response = api.comments.get_comments_by_post_id(post_id)
        response_data = Asserts.base_assertion(response, 200)
        assert len(response_data["comments"]) > 0
        for comment in response_data["comments"]:
            assert comment["postId"] == post_id
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
        comment_id = 1
        response = api.comments.delete_comment(comment_id)
        response_data = Asserts.base_assertion(response, 200)
        assert response_data["id"] == comment_id
        assert response_data.get("isDeleted") is True


class TestCommentsNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_comment_id", invalid_ids(5, 99999, 999999))
    def test_get_invalid_comment(self, api, invalid_comment_id):
        response = api.comments.get_single_comment(invalid_comment_id)
        assert response.status_code == 404

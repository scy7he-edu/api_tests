import pytest

from src.utils.data_generator import post_data, invalid_ids
from src.utils.assertions import Asserts
from src.api.posts.posts_schemas import (
    PostListSchema,
    PostSchema,
    PostTagListSchema,
    PostListCommentsSchema,
)


@pytest.mark.posts
class TestPosts:
    @pytest.mark.positive
    def test_get_all_posts(self, api):
        response = api.posts.get_all_posts()
        response_data = Asserts.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_post(self, api):
        response = api.posts.get_single_post(1)
        response_data = Asserts.base_assertion(response, 200)
        PostSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_search_posts(self, api):
        response = api.posts.search_posts("love")
        response_data = Asserts.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_posts(self, api):
        selection = ["id", "title", "body", "tags", "reactions", "views", "userId"]
        response = api.posts.limit_skip_posts(10, 10, *selection)
        Asserts.base_assertion(response, 200)

    @pytest.mark.positive
    def test_sort_posts(self, api):
        response = api.posts.sort_posts("id", "asc")
        response_data = Asserts.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_all_posts_tags(self, api):
        response = api.posts.get_all_posts_tags()
        assert response.status_code == 200
        PostTagListSchema.model_validate(response.json())

    @pytest.mark.positive
    def test_get_posts_tag_list(self, api):
        response = api.posts.get_posts_tag_list()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.positive
    def test_get_posts_by_tag(self, api):
        response = api.posts.get_posts_by_tag("life")
        response_data = Asserts.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_all_posts_by_user_id(self, api):
        response = api.posts.get_all_posts_by_user_id(5)
        response_data = Asserts.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_post_comments(self, api):
        response = api.posts.get_post_comments(1)
        response_data = Asserts.base_assertion(response, 200)
        PostListCommentsSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_post(self, api):
        response = api.posts.add_post(post_data())
        assert response.status_code == 201

    @pytest.mark.positive
    def test_update_post(self, api):
        response = api.posts.update_post(1, post_data())
        Asserts.base_assertion(response, 200)

    @pytest.mark.positive
    def test_delete_post(self, api):
        response = api.posts.delete_post(1)
        Asserts.base_assertion(response, 200)


class TestPostsNegative:
    @pytest.mark.negative
    @pytest.mark.parametrize("invalid_post_id", invalid_ids(5, 9999, 99999))
    def test_get_invalid_post(self, api, invalid_post_id):
        response = api.posts.get_single_post(invalid_post_id)
        assert response.status_code == 404

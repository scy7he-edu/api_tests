import pytest

from config import Credentials
from src.api.base_client import BaseClient
from src.schemas.posts_schemas import (
    PostSchema,
    PostListSchema,
    PostTagListSchema,
    PostCommentsListSchema,
)

credentials = Credentials()


@pytest.mark.posts
class TestPosts:
    @pytest.mark.positive
    def test_get_all_posts(self, posts_client):
        response = posts_client.get_all_posts()
        response_data = BaseClient.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_single_post(self, posts_client):
        response = posts_client.get_single_post(1)
        response_data = BaseClient.base_assertion(response, 200)
        PostSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_search_posts(self, posts_client):
        response = posts_client.search_posts("love")
        response_data = BaseClient.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_limit_skip_posts(self, posts_client):
        selection = ["id", "title", "body", "tags", "reactions", "views", "userId"]
        response = posts_client.limit_skip_posts(10, 10, *selection)
        BaseClient.base_assertion(response, 200)

    @pytest.mark.positive
    def test_sort_posts(self, posts_client):
        response = posts_client.sort_posts("id", "asc")
        response_data = BaseClient.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_all_posts_tags(self, posts_client):
        response = posts_client.get_all_posts_tags()
        assert response.status_code == 200
        PostTagListSchema.model_validate(response.json())

    @pytest.mark.positive
    def test_get_posts_tag_list(self, posts_client):
        response = posts_client.get_posts_tag_list()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.positive
    def test_get_posts_by_tag(self, posts_client):
        response = posts_client.get_posts_by_tag("life")
        response_data = BaseClient.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_all_posts_by_user_id(self, posts_client):
        response = posts_client.get_all_posts_by_user_id(5)
        response_data = BaseClient.base_assertion(response, 200)
        PostListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_get_post_comments(self, posts_client):
        response = posts_client.get_post_comments(1)
        response_data = BaseClient.base_assertion(response, 200)
        PostCommentsListSchema.model_validate(response_data)

    @pytest.mark.positive
    def test_add_post(self, posts_client):
        response = posts_client.add_post(credentials.post_data)
        assert response.status_code == 201

    @pytest.mark.positive
    def test_update_post(self, posts_client):
        response = posts_client.update_post(1, credentials.post_data)
        BaseClient.base_assertion(response, 200)

    @pytest.mark.positive
    def test_delete_post(self, posts_client):
        response = posts_client.delete_post(1)
        BaseClient.base_assertion(response, 200)

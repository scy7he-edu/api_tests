from src.api.base.base_client import BaseClient
from src.api.posts.posts_schemas import CreatePostRequestSchema


class PostsClient(BaseClient):
    def get_all_posts(self):
        return self._make_request("GET", "/posts")

    def get_single_post(self, post_id: int):
        return self._make_request("GET", f"/posts/{post_id}")

    def search_posts(self, query: str):
        return self._make_request("GET", f"/posts/search?q={query}")

    def limit_skip_posts(self, limit: int, skip: int, *args):
        selection = args
        return self._make_request(
            "GET", f"/posts?limit={limit}&skip={skip}&select={selection}"
        )

    def sort_posts(self, sort_by: str, order: str):
        return self._make_request("GET", f"/posts?sortBy={sort_by}&order={order}")

    def get_all_posts_tags(self):
        return self._make_request("GET", "/posts/tags")

    def get_posts_tag_list(self):
        return self._make_request("GET", "/posts/tag-list")

    def get_posts_by_tag(self, tag: str):
        return self._make_request("GET", f"/posts/tag/{tag}")

    def get_all_posts_by_user_id(self, user_id: int):
        return self._make_request("GET", f"/posts/user/{user_id}")

    def get_post_comments(self, post_id: int):
        return self._make_request("GET", f"/posts/{post_id}/comments")

    def add_post(self, post_data: CreatePostRequestSchema):
        return self._make_request("POST", "/posts/add", json=post_data.model_dump())

    def update_post(self, post_id: int, post_data: CreatePostRequestSchema):
        return self._make_request(
            "PATCH", f"/posts/{post_id}", json=post_data.model_dump()
        )

    def delete_post(self, post_id: int):
        return self._make_request("DELETE", f"/posts/{post_id}")

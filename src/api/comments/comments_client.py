from src.api.base.base_client import BaseClient
from src.api.comments.comments_schemas import CreateCommentRequestSchema


class CommentsClient(BaseClient):
    def get_all_comments(self):
        return self._make_request("GET", "/comments")

    def get_single_comment(self, comment_id: int):
        return self._make_request("GET", f"/comments/{comment_id}")

    def limit_skip_comments(self, limit: int, skip: int, *args):
        selection = ",".join(args)
        return self._make_request(
            "GET", f"/comments?limit={limit}&skip={skip}&select={selection}"
        )

    def get_comments_by_post_id(self, post_id: int):
        return self._make_request("GET", f"/comments/post/{post_id}")

    def add_new_comment(self, comment_data: CreateCommentRequestSchema):
        return self._make_request(
            "POST", "/comments/add", json=comment_data.model_dump()
        )

    def update_comment(self, comment_id: int, comment_data: CreateCommentRequestSchema):
        return self._make_request(
            "PATCH", f"/comments/{comment_id}", json=comment_data.model_dump()
        )

    def delete_comment(self, comment_id: int):
        return self._make_request("DELETE", f"/comments/{comment_id}")

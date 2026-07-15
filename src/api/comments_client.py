from src.api.base_client import BaseClient


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

    def add_new_comment(self, comment_data: dict):
        return self._make_request("POST", "/comments/add", json=comment_data)

    def update_comment(self, comment_id: int):
        comment = {"body": "test comment body"}
        return self._make_request("PATCH", f"/comments/{comment_id}", json=comment)

    def delete_comment(self, comment_id: int):
        return self._make_request("DELETE", f"/comments/{comment_id}")

from src.api.base.base_client import BaseClient
from src.api.products.products_schemas import CreateProductRequestSchema


class ProductsClient(BaseClient):
    def get_all_products(self):
        return self._make_request("GET", "/products")

    def get_single_product(self, product_id: int):
        return self._make_request("GET", f"/products/{product_id}")

    def search_products(self, search_request: str):
        return self._make_request("GET", f"/products/search?q={search_request}")

    def limit_and_skip_products(self, limit: int, skip: int, *args):
        query_string = ",".join(args)
        return self._make_request(
            "GET", f"/products?limit={limit}&skip={skip}&select={query_string}"
        )

    def sort_products(self, sort_by: str, order: str):
        return self._make_request("GET", f"/products?sortBy={sort_by}&order={order}")

    def get_products_categories(self):
        return self._make_request("GET", "/products/categories")

    def get_products_category_list(self):
        return self._make_request("GET", "/products/category-list")

    def get_products_by_category(self, category: str):
        return self._make_request("GET", f"/products/category/{category}")

    def add_product(self, product_data: CreateProductRequestSchema):
        return self._make_request(
            "POST", "/products/add", json=product_data.model_dump()
        )

    def update_product(self, product_data: CreateProductRequestSchema, product_id: int):
        return self._make_request(
            "PATCH", f"/products/{product_id}", json=product_data.model_dump()
        )

    def rewrite_product(
        self, product_data: CreateProductRequestSchema, product_id: int
    ):
        return self._make_request(
            "PUT", f"/products/{product_id}", json=product_data.model_dump()
        )

    def delete_product(self, product_id: int):
        return self._make_request("DELETE", f"/products/{product_id}")

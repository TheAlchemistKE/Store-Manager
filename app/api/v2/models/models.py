from .database import DatabaseActions


class UserOperations(DatabaseActions):
    def __init__(self):
        pass

    def create_new_user(self, name, username, email, role, password, confirm_password):
        pass

    def delete_user(self, username):
        pass

    def get_all_users(self):
        pass


class ProductsOperations:
    def __init__(self):
        pass

    def add_new_product(self):
        pass

    def delete_product(self, user):
        pass

    def get_products(self):
        pass

    def update_product_details(self):
        pass


class SalesOperations:
    def __init__(self):
        pass

    def save_sales_records(self):
        pass

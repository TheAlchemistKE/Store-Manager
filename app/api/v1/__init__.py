from flask import Blueprint
from flask_restful import Api

# Local Imports
from .views.product_views import ProductList, SingleProduct
from .views.sales_views import SalesList


version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(ProductList, '/products')
api.add_resource(SalesList, '/sales')
api.add_resource(SingleProduct, '/products/<int:product_id>')

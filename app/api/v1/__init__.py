from flask import Blueprint
from flask_restful import Api

# Local Imports
from .views.product_views import ProductList


version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)

api.add_resource(ProductList, '/products')

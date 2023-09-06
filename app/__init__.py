from flask_restx import Api

from .producto import api as producto_api

api = Api(
    title="Antonio APP",
    version="1.0",
    description="A simple demo API",
)

api.add_namespace(producto_api)

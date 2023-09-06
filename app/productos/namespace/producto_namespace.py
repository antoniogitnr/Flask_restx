from flask_restx import Namespace,fields

api = Namespace("Productos", description="operacion relacionada con productos")

producto = api.model(
    "Producto",
    {
        "idProducto": fields.Integer(required=True, description="identificador del producto"),
        "nombreProducto": fields.String(required=True, description="nombre del producto"),
        "precio": fields.Integer(required=True, description="Precio del producto"),
    },
)

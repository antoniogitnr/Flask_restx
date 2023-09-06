from flask import request
from flask_restx import Resource,fields
from app.productos.namespace.producto_namespace import api
from app.database.entities.producto import Producto
@api.route("/")
class listaProductos(Resource):
    @api.doc("list_producto") 
    #@api.marshal_list_with(product)
    def get(self):
        """List all productos"""
        return Producto().all()

@api.route("/<id>")
@api.param("id", "identificacion del producto")
@api.response(404, "No hay carpetas de producto")
class product(Resource):
    @api.doc("get_producto")
    #@api.marshal_with(recibo)
    def get(self, id):
        "leer producto"
        return Producto().get(id)
        api.abort(404)

@api.route("/crear")
class CreateProduct(Resource):
    @api.doc("post_producto")
    @api.expect(api.model("producto", {
        "idProducto": fields.Float(required=False),
        "nombreProducto": fields.String(required=True),
        "precio": fields.Float(required=True)
    }))
    def post(self):
        data = request.json
        nombreProducto = data["nombreProducto"]
        precio = data["precio"]
        return Producto().crear(nombreProducto,precio)
@api.route("/delete/<id>")
@api.param("id","identificador del producto")
class DeleteProducto(Resource):
    @api.doc("delete_producto")
    def delete(self,id):
        "borrar producto"
        return Producto().borrar(id)
@api.route("/update/<id>")
@api.param("id","identificador del producto")
class updateProducto(Resource):
    @api.doc("put_producto")
    @api.expect(api.model("producto",{
        "nombreProducto": fields.String(required=True),
        "precio":fields.Integer(required=True)
    }))
    def put(self,id):
        data = request.json
        precio = data["precio"]
        nombreProducto = data["nombreProducto"]
        return Producto().actualizar(nombreProducto,precio,id)
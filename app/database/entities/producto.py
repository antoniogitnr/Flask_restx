from app.database import db

class Producto:
    
    @staticmethod
    def all():
        products = db.select("SELECT * FROM productos;")
        results = []
        for product in products:
            results.append({"idProducto": product[0], "nombreProducto": product[1], "precio":product[2]})
        return results
    @staticmethod
    def get(idProducto):
        result = db.selectone("SELECT * FROM productos WHERE idProducto = %s",(idProducto))
        return {"idProducto": result[0], "nombreProducto": result[1], "precio":result[2]}
    
    @staticmethod
    def crear(nombreProducto,precio):
        result = db.create("INSERT INTO productos(idProducto,nombreProducto,precio) VALUES (NULL,%s,%s)",(nombreProducto,precio))
        return result
    
    @staticmethod
    def borrar(idProducto):
        result = db.delete("DELETE FROM productos WHERE idProducto = %s",(idProducto))
        return result
    
    @staticmethod 
    def actualizar(nombreProducto,precio,idProducto):
        result = db.update("UPDATE productos SET nombreProducto = %s,precio = %s WHERE idProducto = %s",(nombreProducto,precio,idProducto))
        return result
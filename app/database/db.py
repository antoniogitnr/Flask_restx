import pymysql
def crearConexion():
    return pymysql.connect(
        host='localhost',
        user='panda',
        password='root',
        database='poo'
    )
    
def select(query:str):
    conectado = crearConexion()
    lista = []
    with conectado.cursor() as cursor:
        cursor.execute(query)
        lista = cursor.fetchall()
    conectado.commit()
    conectado.close()
    return lista
def selectone(query:str, args):
    conectado = crearConexion()
    with conectado.cursor() as cursor:
        cursor.execute(query,args=args)
        one = cursor.fetchone()
    conectado.commit()
    conectado.close()
    return one
def create(query:str,args):
    conectado = crearConexion()
    with conectado.cursor() as cursor:
        cursor.execute(query,args=args)
    conectado.commit()
    conectado.close() 
    return 'Producto creado'
def delete(query:str,arg):
    conectado = crearConexion()
    with conectado.cursor() as cursor:
        cursor.execute(query,arg)
    conectado.commit()
    conectado.close()
    return 'Producto eliminado'
def update(query:str,arg):
    conectado = crearConexion()
    with conectado.cursor() as cursor:
        cursor.execute(query,arg)
    conectado.commit()
    conectado.close()
    return 'Producto actualizado'
    
    
if __name__ == '__main__':
   """ lista = select("select * from recibo")   """ 
"""    x = 2 
   one = selectone("SELECT * FROM recibo(idProducto,nombreProducto,precio) WHERE idProducto = %s",x)
   print(one)  """
""" 
datos = ('zapatos',150)
create("INSERT INTO recibo(idProducto,nombreProducto,precio) VALUES (NULL,%s,%s)",datos)   """
""" x=3
delete("DELETE FROM productos WHERE idProducto = %s",(x))
 """
""" x = ('aaaaa',222,5)
update("UPDATE productos SET nombreProducto = %s,precio = %s WHERE idProducto = %s",(x)) """
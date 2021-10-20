from tienda_viertual import init_app
from models.producto import Producto, db

app = init_app()


@app.route("/")
def hola_mundo():
    return "hola_mundo"


@app.route("/cu")
def fabricon():
    return "fabricio maricon"


@app.route("/crear_producto")
def crear_producto():
    producto = Producto(nombre="minoxidil_caja", precio=350000, referencia="1")
    db.session.add(producto)
    db.session.commit()
    return "producto_creado"

@app.route("/productos")
def devolver_productos():
    lista = []
    for p in Producto.query.all():
        lista.append(p.id)
    return str(lista)

app.run(host="0.0.0.0")

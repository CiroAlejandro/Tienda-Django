from tienda_viertual import db
class Producto(db.Model):
    __tablename__ = "producto"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(32), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    referencia = db.Column(db.String, nullable=False)
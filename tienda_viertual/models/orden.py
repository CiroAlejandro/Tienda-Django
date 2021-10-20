from tienda_viertual import db
class Orden(db.Model):
    __tablename__ = "orden"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    producto_id = db.Column(db.Integer, db.ForeignKey("producto.id"))

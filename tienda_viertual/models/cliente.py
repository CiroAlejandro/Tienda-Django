from tienda_viertual import db
class Cliente(db.Model):
    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(32), nullable=False)
    cedula = db.Column(db.String(16), nullable=False)

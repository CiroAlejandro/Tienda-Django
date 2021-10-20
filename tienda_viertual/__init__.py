from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()
def init_app():
    app = Flask("tienda_virtual")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
        return app

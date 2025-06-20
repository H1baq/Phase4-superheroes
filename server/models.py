from .app import db

class Hero(db.Model):
    __tablename__="heroes"
    id=db.Column(db.Integer, primary_key=True)
    name =db.Column (db.String)
    super_name=db.Column(db.String)

from .app import db
from sqlalchemy.orm import validates
class Hero(db.Model):
    __tablename__="heroes"
    id=db.Column(db.Integer, primary_key=True)
    name =db.Column (db.String)
    super_name=db.Column(db.String)



class Power (db.Model):
    __tablename__="powers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return value

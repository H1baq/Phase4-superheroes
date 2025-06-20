from .app import db
from sqlalchemy.orm import validates
class Hero(db.Model):
    __tablename__="heroes"
    id=db.Column(db.Integer, primary_key=True)
    name =db.Column (db.String)
    super_name=db.Column(db.String)

    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete')




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
    


class HeroPower(db.Model):
    __tablename__="hero_powers"
    id = db.Column(db.Integer, primary_key =True)
    strength =db.Column(db.String)
    hero_id =db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id =db.Column(db.Integer, db.ForeignKey('powers.id'))


    @validates("strength")
    def validate_strength(self, key, value):
        if value not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        return value
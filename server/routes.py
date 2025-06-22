from flask import Blueprint, jsonify, request
from .models import db, Hero, Power, HeroPower

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Superheroes API"}), 200

@routes.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

@routes.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get_or_404(id)
    data = hero.to_dict()
    data["powers"] = [
        {
            "id": hp.power.id,
            "name": hp.power.name,
            "description": hp.power.description
        } for hp in hero.hero_powers
    ]
    return jsonify(data), 200

@routes.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

@routes.route("/powers/<int:id>", methods=["PATCH"])
def update_power(id):
    power = Power.query.get_or_404(id)
    try:
        data = request.get_json()
        power.description = data["description"]
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except ValueError as ve:
        return {"errors": [str(ve)]}, 400

@routes.route("/hero_powers", methods=["POST"])
def create_hero_power():
    try:
        data = request.get_json()
        hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(hero_power)
        db.session.commit()

        hero = Hero.query.get(hero_power.hero_id)
        result = hero.to_dict()
        result["powers"] = [
            {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            } for hp in hero.hero_powers
        ]
        return jsonify(result), 201

    except ValueError as ve:
        return {"errors": [str(ve)]}, 400

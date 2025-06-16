


from flask import Blueprint, request, jsonify
from server import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint("restaurant", __name__)

@restaurant_bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": [{"id": p.pizza.id, "name": p.pizza.name, "ingredients": p.pizza.ingredients} for p in restaurant.restaurant_pizzas]
    })

@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    
    return "", 204

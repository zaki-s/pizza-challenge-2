


@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()
    
    try:
        restaurant_pizza = RestaurantPizza(price=data["price"], restaurant_id=data["restaurant_id"], pizza_id=data["pizza_id"])
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify({
            "id": restaurant_pizza.id,
            "price": restaurant_pizza.price,
            "restaurant_id": restaurant_pizza.restaurant_id,
            "pizza_id": restaurant_pizza.pizza_id,
            "pizza": {"id": restaurant_pizza.pizza.id, "name": restaurant_pizza.pizza.name, "ingredients": restaurant_pizza.pizza.ingredients},
            "restaurant": {"id": restaurant_pizza.restaurant.id, "name": restaurant_pizza.restaurant.name, "address": restaurant_pizza.restaurant.address}
        }), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

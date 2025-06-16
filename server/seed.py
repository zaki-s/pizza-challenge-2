


from server import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

db.create_all()

restaurant1 = Restaurant(name="Kiki's Pizza", address="123 Main Street")
pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")

db.session.add_all([restaurant1, pizza1])
db.session.commit()

restaurant_pizza1 = RestaurantPizza(price=10, restaurant_id=restaurant1.id, pizza_id=pizza1.id)
db.session.add(restaurant_pizza1)
db.session.commit()

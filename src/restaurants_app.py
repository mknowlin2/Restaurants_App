#!/usr/bin/env python3
#
# The Restaurants Web application.
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def restaurants():
    '''Mock Restaurants'''
    restaurants = [{"name": "Mock Restaurant 1", "id": "1"},
                   {"name": "Mock Restaurant 2", "id": "2"},
                   {"name": "Mock Restaurant 3", "id": "3"},
                   {"name": "Mock Restaurant 4", "id": "4"},
                   {"name": "Mock Restaurant 5", "id": "5"}]

    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurants/new/")
def restaurantNew():
    return "Create new restaurant page."


@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def restaurantMenu(restaurant_id):
    return "Restaurant Menu page."


@app.route("/restaurants/<int:restaurant_id>/edit/")
def restaurantEdit(restaurant_id):
    return "Restaurant Edit page."


@app.route("/restaurants/<int:restaurant_id>/delete/")
def restaurantDelete(restaurant_id):
    return "Restaurant Delete page."


@app.route("/restaurants/<int:restaurant_id>/menu/new/")
def menuItemNew(restaurant_id):
    return "Create a new menu item page."


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/")
def menuItemEdit(restaurant_id, menu_id):
    return "Menu Item Edit page."


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/")
def menuItemDelete(restaurant_id, menu_id):
    return "Menu Item Delete page."


@app.route("/restaurants/JSON/")
def restaurantsJSON():
    return "Restaurants JSON response."


@app.route("/restaurants/<int:restaurant_id>/JSON/")
@app.route("/restaurants/<int:restaurant_id>/menu/JSON/")
def restaurantMenuJSON(restaurant_id):
    return "Restaurant Menu JSON response."


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/")
def restaurantMenuItemJSON(restaurant_id, menu_id):
    return "Restaurant Menu Item JSON response."


if __name__ == '__main__':
    app.secret_key = 'dev_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/env python3
#
# The Restaurants Web application.
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def restaurants():
    return "Main restaurants page."


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
def menuItemNew(menu_id):
    return "Create a new menu item page."


if __name__ == '__main__':
    app.secret_key = 'dev_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/env python3
#
# The Restaurants Web application.
from flask import Flask, render_template, request, redirect, url_for
from database.data_access import get_all_restaurants

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def restaurants():
    restaurants = get_all_restaurants()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurants/new/", methods=['GET', 'POST'])
def restaurantNew():
    if request.method == 'POST':
        '''TODO: Add Data Access Layer code'''
        return redirect(url_for("restaurants"))
    else:
        return render_template("newRestaurant.html")


@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def restaurantMenu(restaurant_id):
    '''Mock Restaurant'''
    restaurant = {"name": "Mock Restaurant 1", "id": "1"}

    items = [{"id":"1", "name": "Mock Entree", "course": "Entree", "price": "$12.00", "description": "Mock description"},
             {"id":"2", "name": "Mock Dessert", "course": "Dessert", "price": "$4.00", "description": "Mock description"},
             {"id":"3", "name": "Mock Appetizer", "course": "Appetizer", "price": "$4.00", "description": "Mock description"}]

    return render_template("menu.html", restaurant=restaurant, items=items)


@app.route("/restaurants/<int:restaurant_id>/edit/", methods=['GET', 'POST'])
def restaurantEdit(restaurant_id):
    if request.method == 'POST':
        '''TODO: Add Data Access Layer code'''
        return redirect(url_for("restaurants"))
    else:
        '''Mock Restaurant'''
        restaurant = {"name": "Mock Restaurant 1", "id": "1"}
        return render_template("editRestaurant.html",
                               restaurant_id=restaurant_id,
                               restaurant=restaurant)


@app.route("/restaurants/<int:restaurant_id>/delete/", methods=['GET', 'POST'])
def restaurantDelete(restaurant_id):
    if request.method == 'POST':
        '''TODO: Add Data Access Layer code'''
        return redirect(url_for("restaurants"))
    else:
        '''Mock Restaurant'''
        restaurant = {"name": "Mock Restaurant 1", "id": "1"}
        return render_template("deleteRestaurant.html",
                               restaurant_id=restaurant_id,
                               restaurant=restaurant)


@app.route("/restaurants/<int:restaurant_id>/menu/new/", methods=['GET', 'POST'])
def menuItemNew(restaurant_id):
    if request.method == 'POST':
        '''TODO: Add Data Access Layer code'''
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template("newMenuItem.html", restaurant_id=restaurant_id)


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/",
           methods=['GET', 'POST'])
def menuItemEdit(restaurant_id, menu_id):
    if request.method == 'POST':
        '''TODO: Add Data Access Layer code'''
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        item = {"id":"1", "name": "Mock Entree", "course": "Entree",
                 "price": "$12.00", "description": "Mock description"}
        return render_template("editMenuItem.html",
                               restaurant_id=restaurant_id, item=item)


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/",
           methods=['GET', 'POST'])
def menuItemDelete(restaurant_id, menu_id):
    if request.method == 'POST':
        '''TODO: Add Data Access Layer code'''
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        item = {"id":"1", "name": "Mock Entree", "course": "Entree",
                 "price": "$12.00", "description": "Mock description"}
        return render_template("deleteMenuItem.html",
                               restaurant_id=restaurant_id, menu_id=menu_id, item=item)


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

#!/usr/bin/env python3
#
# The Restaurants Web application.
from flask import Flask, render_template, request, redirect, url_for, \
     jsonify
from database.data_access import get_all_restaurants, get_restaurant, \
     add_restaurant, update_restaurant, delete_restaurant, \
     get_all_menu_items_for_restaurant, get_menu_item, add_menu_item, \
     update_menu_item, delete_menu_item

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def restaurants():
    restaurants = get_all_restaurants()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/restaurants/new/", methods=['GET', 'POST'])
def restaurantNew():
    if request.method == 'POST':
        add_restaurant(request.form['name'])
        return redirect(url_for("restaurants"))
    else:
        return render_template("newRestaurant.html")


@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def restaurantMenu(restaurant_id):
    restaurant = get_restaurant(restaurant_id)
    items = get_all_menu_items_for_restaurant(restaurant_id)
    return render_template("menu.html", restaurant=restaurant, items=items)


@app.route("/restaurants/<int:restaurant_id>/edit/", methods=['GET', 'POST'])
def restaurantEdit(restaurant_id):
    if request.method == 'POST':
        update_restaurant(restaurant_id, request.form['name'])
        return redirect(url_for("restaurants"))
    else:
        restaurant = get_restaurant(restaurant_id)
        return render_template("editRestaurant.html",
                               restaurant_id=restaurant_id,
                               restaurant=restaurant)


@app.route("/restaurants/<int:restaurant_id>/delete/",
           methods=['GET', 'POST'])
def restaurantDelete(restaurant_id):
    if request.method == 'POST':
        delete_restaurant(restaurant_id)
        return redirect(url_for("restaurants"))
    else:
        restaurant = get_restaurant(restaurant_id)
        return render_template("deleteRestaurant.html",
                               restaurant_id=restaurant_id,
                               restaurant=restaurant)


@app.route("/restaurants/<int:restaurant_id>/menu/new/",
           methods=['GET', 'POST'])
def menuItemNew(restaurant_id):
    if request.method == 'POST':
        add_menu_item(restaurant_id, request.form['name'],
                      request.form['course'], request.form['price'],
                      request.form['description'])
        return redirect(url_for("restaurantMenu",
                                restaurant_id=restaurant_id))
    else:
        return render_template("newMenuItem.html",
                               restaurant_id=restaurant_id)


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/",
           methods=['GET', 'POST'])
def menuItemEdit(restaurant_id, menu_id):
    item = get_menu_item(menu_id)

    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['course']:
            item.course = request.form['course']
        if request.form['price']:
            item.price = request.form['price']
        if request.form['description']:
            item.description = request.form['description']
        update_menu_item(menu_id, item.name, item.course, item.price,
                         item.description)
        return redirect(url_for("restaurantMenu",
                                restaurant_id=restaurant_id))
    else:
        return render_template("editMenuItem.html",
                               restaurant_id=restaurant_id, item=item)


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/",
           methods=['GET', 'POST'])
def menuItemDelete(restaurant_id, menu_id):
    if request.method == 'POST':
        delete_menu_item(menu_id)
        return redirect(url_for("restaurantMenu",
                                restaurant_id=restaurant_id))
    else:
        item = get_menu_item(menu_id)
        return render_template("deleteMenuItem.html",
                               restaurant_id=restaurant_id, menu_id=menu_id,
                               item=item)


@app.route("/restaurants/JSON/")
def restaurantsJSON():
    # Retrieve data for the restaurants
    restaurants = get_all_restaurants()
    return jsonify(Restaurant=[restaurant.serialize
                               for restaurant in restaurants])


@app.route("/restaurants/<int:restaurant_id>/JSON/")
@app.route("/restaurants/<int:restaurant_id>/menu/JSON/")
def restaurantMenuJSON(restaurant_id):
    # Retrieve data for the restaurant with id = restaurant_id
    items = get_all_menu_items_for_restaurant(restaurant_id)
    return jsonify(MenuItem=[item.serialize for item in items])


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/")
def restaurantMenuItemJSON(restaurant_id, menu_id):
    # Retrieve data for menu item with restaurant_id and menu_id
    item = get_menu_item(menu_id)
    return jsonify(MenuItem=[item.serialize])


if __name__ == '__main__':
    app.secret_key = 'dev_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

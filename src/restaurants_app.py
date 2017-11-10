#!/usr/bin/env python3
#
# The Restaurants Web application.
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/restaurants/")
def restaurants():
    return "Main restaurants page."


@app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
def restaurantMenu(restaurant_id):
    return "Restaurant Menu page."


if __name__ == '__main__':
    app.secret_key = 'dev_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

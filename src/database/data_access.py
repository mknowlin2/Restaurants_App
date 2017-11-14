#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db_setup import Base, Restaurant

'''Set up database engine and database session '''
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_all_restaurants():
    '''Retrieve all records from the Restaurant table'''
    restaurants = session.query(Restaurant).all()
    return restaurants


def get_restaurant(restaurant_id):
    '''Retrieve restaurant by restaurant_id from the Restaurant table'''
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    return restaurant


def add_restaurant(restaurant_name):
    '''Insert new restaurant into the Restaurant table'''
    newRestaurant = Restaurant(name=restaurant_name)
    session.add(newRestaurant)
    session.commit()


def update_restaurant(restaurant_id, new_name):
    '''Update the restaurant with new name.'''
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    restaurant.name = new_name
    session.add(restaurant)
    session.commit()


def delete_restaurant(restaurant_id):
    '''Delete the restaurant from the Restaurant table'''
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    session.delete(restaurant)
    session.commit()


def get_all_menu_items_for_restaurant(rest_id):
    '''Retrieve all menu items for given restaurant_id from MenuItem'''
    items = session.query(MenuItem).filter_by(restaurant_id=rest_id)
    return items


def get_menu_item(item_id):
    '''Retrieve all records from the Restaurant table'''
    item = session.query(MenuItem).filter_by(id=item_id).one()
    return item

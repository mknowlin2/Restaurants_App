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

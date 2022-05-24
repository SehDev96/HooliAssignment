import sqlite3
import sys

from model.Customer import Customer
from model.Restaurant import Restaurant


def update_restaurant_info(restaurant):
    connection = sqlite3.connect("database/database_dev.sqlite")
    cursor = connection.cursor()
    try:
        # connection = sqlite3.connect("database/database_dev.sqlite")

        print("Connected to SQLite")

        update_query = "UPDATE restaurant " \
                       "set name='{name}', " \
                       "hooli_number='{number}' " \
                       "where id='{id}'".format(name=restaurant.get_name(),
                                                number=restaurant.get_hooli_number(),
                                                id=restaurant.get_id())
        cursor.execute(update_query)
        connection.commit()
        print("Record Updated Successfully")
        cursor.close()


    except sqlite3.Error as error:
        connection.rollback()
        print("Failed to update details", error)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed")
    return cursor.rowcount


def get_customer_info_by_hooli_number(hooli_number):
    connection = sqlite3.connect("database/database_dev.sqlite")
    customer_data = None
    try:
        # connection = sqlite3.connect("database/database_dev.sqlite")
        cursor = connection.cursor()
        print("Connected to SQLite", file=sys.stderr)

        query = "SELECT * FROM customer where hooli_number='{hooli_number}'".format(hooli_number=hooli_number)
        print(query, file=sys.stderr)
        cursor.execute(query)
        customer_data = cursor.fetchone()
    except sqlite3.Error as error:
        print("Error fetching data from database", error)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed")

    print("End of get customer info", file=sys.stderr)
    print(customer_data, file=sys.stderr)
    return Customer(customer_data)


def get_restaurant_info_by_hooli_number(hooli_number):
    connection = sqlite3.connect("database/database_dev.sqlite")
    restaurant_data = None
    try:
        # connection = sqlite3.connect("database/database_dev.sqlite")
        cursor = connection.cursor()
        print("Connected to SQLite", file=sys.stderr)

        query = "SELECT * FROM restaurant where hooli_number='{hooli_number}'".format(hooli_number=hooli_number)
        cursor.execute(query)
        restaurant_data = cursor.fetchone()
    except sqlite3.Error as error:
        print("Error fetching data from database", error, file=sys.stderr)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed", file=sys.stderr)

    print("End of get restaurant function", file=sys.stderr)
    return Restaurant(restaurant_data)


def get_restaurant_info_by_id(id):
    connection = sqlite3.connect("database/database_dev.sqlite")
    restaurant_data = None
    try:
        # connection = sqlite3.connect("database/database_dev.sqlite")
        cursor = connection.cursor()
        print("Connected to SQLite", file=sys.stderr)

        query = "SELECT * FROM restaurant where id='{id}'".format(id=id)
        cursor.execute(query)
        restaurant_data = cursor.fetchone()
    except sqlite3.Error as error:
        print("Error fetching data from database", error, file=sys.stderr)
    finally:
        if connection:
            connection.close()
            print("SQLite connection closed", file=sys.stderr)

    print("End of get restaurant function", file=sys.stderr)
    return Restaurant(restaurant_data)

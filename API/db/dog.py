import psycopg2
from flask import current_app

from db.database import get_connection
from model.Dog import Dog

LOG_PREFIX = "DB/Table Dogs ->"


def fetch_records(id_=None, limit=None):
    current_app.logger.info(f"{LOG_PREFIX} Fetching records from database")
    connection = get_connection()
    cursor = None
    if connection:
        try:
            query = "SELECT * FROM dogs"
            if limit:
                query += " LIMIT %(limit)s"
            if id_:
                query += f" WHERE id = %(id)s"
            cursor = connection.cursor()
            params = None
            if id_:
                params = {"id": id_}
            elif limit:
                params = {"limit": limit}

            cursor.execute(query, params)
            if id_:
                record = cursor.fetchone()
                if record:
                    return Dog(record[2], record[0], record[1]).serialize()
            else:
                records = cursor.fetchall()
                dogs = []
                for row in records:
                    dogs.append(Dog(row[2], row[0], row[1]).serialize())
                return dogs
        except (Exception, psycopg2.Error) as error:
            current_app.logger.error(f"{LOG_PREFIX} Error while fetching dogs", error)
        finally:
            cursor.close()
            connection.close()
            current_app.logger.info(f"{LOG_PREFIX} Closing dogs database connection")


def insert_record(dog):
    current_app.logger.info(f"{LOG_PREFIX} Creating a record in database")
    connection = get_connection()
    cursor = None
    if connection:
        try:
            name = dog.get("name", None)
            age = dog.get("age", None)
            if age and name:
                query = f"INSERT INTO dogs(name, age) VALUES (%(name)s, %(age)s)"
                params = {"name": name, "age": age}
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
        except (Exception, psycopg2.Error) as error:
            current_app.logger.error(f"{LOG_PREFIX} Error while creating dog", error)
        finally:
            cursor.close()
            connection.close()
            current_app.logger.info(f"{LOG_PREFIX} Closing dogs database connection")


def update_record(id_, dog):
    current_app.logger.info(f"{LOG_PREFIX} Updating a record in database")
    connection = get_connection()
    cursor = None
    if connection:
        try:
            name = dog.get("name", None)
            age = dog.get("age", None)
            if name and age:
                query = f"UPDATE dogs SET name = %(name)s, age = %(age)s WHERE id = %(id)s"
                params = {"name": name, "age": age, "id": id_}
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
        except (Exception, psycopg2.Error) as error:
            current_app.logger.error(f"{LOG_PREFIX} Error while updating dog", error)
        finally:
            cursor.close()
            connection.close()
            current_app.logger.info(f"{LOG_PREFIX} Closing dogs database connection")


def delete_record(id_):
    current_app.logger.info(f"{LOG_PREFIX} Deleting a record in database")
    connection = get_connection()
    cursor = None
    if connection:
        try:
            query = f"DELETE FROM dogs WHERE id = %(id)s"
            params = {"id": id_}
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            current_app.logger.error(f"{LOG_PREFIX} Error while deleting dog", error)
        finally:
            cursor.close()
            connection.close()
            current_app.logger.info(f"{LOG_PREFIX} Closing dogs database connection")

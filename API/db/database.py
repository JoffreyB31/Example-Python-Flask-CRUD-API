import logging

import psycopg2

log = logging.getLogger('__main__')


def get_connection():
    try:
        return psycopg2.connect(user="postgres",
                                password="admin",
                                host="localhost",
                                port="5432",
                                database="python_api")
    except (psycopg2.Error, psycopg2.OperationalError) as e:
        log.error("Error while connecting to database", e)

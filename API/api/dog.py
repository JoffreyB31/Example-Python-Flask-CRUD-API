from flask import abort, make_response

from db.dog import fetch_records, delete_record, update_record, insert_record


def read_all(limit=None):
    """
    Responds to (GET) /api/dogs and return the complete lists of dogs
    :return:            json string with list of dogs
    """
    return fetch_records(None, limit)


def read_one(name):
    """
    Responds to (GET) /api/dogs/{name} with the corresponding dog
    :param name:        name of the dog to find
    :return:            a dog with the name passed in parameters
    """
    dog = fetch_records(name)
    if not dog:
        abort(404, f"Dog with name {name} not found")

    return dog


def create(dog):
    """
    Responds to (POST) /api/dogs, create a new dog
    :param dog:         dog to create in database
    :return:            201 on successful delete, 404 if not found
    """
    name = dog.get("name", None)

    if name:
        insert_record(dog)
        make_response(f"Dog with {name} inserted in database", 200)


def update(id_, dog):
    """
    Responds to (PUT) /api/dogs/{name}, update a dog in the database
    :param id_:        id of the dog to update
    :param dog:         dog to update in database
    :return:            the updated dog
    """
    dog_exists = read_one(id_)
    if dog_exists:
        update_record(id_, dog)
        make_response(f"Dog with {id_} updated in database", 200)
    else:
        abort(404, f"Dog with name {id_} not found")


def delete(id_):
    """
    Responds to (DELETE) /api/dogs/{name}, delete a dog in the database
    :param id_:         id of the dog to delete
    :return:            200 on successful delete, 404 if not found
    """
    dog_exists = read_one(id_)
    if dog_exists:
        delete_record(id_)
        make_response(f"Dog {id_} deleted from database", 200)
    else:
        abort(404, f"Dog {id_} not found")
    return

class Dog:
    id = 0
    name = ""
    age = 0

    def __init__(self, id_, name, age):
        self.id = id_
        self.name = name
        self.age = age

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

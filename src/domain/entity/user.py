

class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, user_dict):
        user_entity = User(id = user_dict['id'],
                           name = user_dict['name'])

        return user_entity

from base_client import *


class GetUser(BaseClient):
    method = 'users.get'
    http_method = 'get'

    def __init__(self, username):
        self.parameters = (('user_ids', username), ('fields', 'bdate'))

    def load_ids_username(self):
        try:
            self.execute()
            user = self.get_json()['response']
        except KeyError:
            print('Incorrect id or username')
        else:
            user_id = user[0]['uid']
        return user_id
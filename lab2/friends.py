from base_client import *


class GetFriends(BaseClient):
    method = 'friends.get'
    http_method = 'get'

    def __init__(self, user_id):
        self.parameters = (('user_id', user_id),('fields', 'bdate'))

    def load_friends_id(self):
        friendlist = []
        try:
            self.execute()
            friends = self.get_json()['response']
        except KeyError:
            print('Incorrect id or username')
        else:
            for friend in friends:
                if 'bdate' in friend:
                    if len(friend['bdate'].split('.')) > 2:
                        friendlist.append(friend)
        return friendlist

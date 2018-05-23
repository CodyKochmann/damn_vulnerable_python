#!python

import base64
from json import loads, dumps
import os

''' this is an api to plug into a web app for authentication and storing user data '''

class EasyUserDB(object):
    ''' this is a handy little database that lets you store user data for things like web apps! '''
    def __init__(self, path='/tmp'):
        self.db_path = os.path.join(
            path,
            'user.db'
        )
        
    @staticmethod
    def encrypt(input_string):
        ''' undergo 3 transformations to make this really hard to guess '''
        return ''.join(reversed(base64.b64encode(input_string.encode()).hex()))
        
    @staticmethod
    def decrypt(input_string):
        ''' undergo 3 transformations to make this really hard to guess '''
        return base64.b64decode(bytes().fromhex(''.join(reversed(input_string)))).decode()
        
    def get_user(self, username):
        ret = None
        for user in self.users():
            if username == user['username']:
                ret = user
        return ret
            
    def new_user(self, username, password):
        return self.save_user_data({
            'username': username,
            'password': self.encrypt(password)
        })
        
    def save_user_data(self, data):
        with open(self.db_path, 'a') as f:
            f.write(dumps(data)+'\n')
        return data
    
    def update_user_field(self, username, field, value):
        user = self.get_user(username)
        user[field] = value
        return self.save_user_data(user)
    
    def users(self):
        with open(self.db_path, 'r') as f:
            for line in filter(len, f):
                yield dict(loads(line))
                
    def change_password(self, username, old_pass, new_pass):
        user = self.get_user(username)
        old_pass = self.encrypt(old_pass)
        new_pass = self.encrypt(new_pass)
        assert user is not None, 'invalid user in %s'%(locals(),)
        if user['password'] == old_pass:
            return self.update_user_field(
                user, 
                'password', 
                new_pass
            )
        else:
            raise Exception('"%s" did not match "%s"' % (
                old_pass,
                user['password']
            ))

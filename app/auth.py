
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = [
    {
        'id': 1,
        'name': u'Tauren Kristich',
        'username': u'taurenk',
        'password': u'unsafepw'
    },
    {
        'id': 2,
        'name': u'Henry Dog',
        'username': u'otto',
        'password': u'otto123'
    }
]


@auth.get_password
def get_password(username):
    target_user = filter(lambda t: t['username'] == username, users)
    if not target_user:
        return {'username or password incorrect'}, 401
    return target_user[0]['password']

def get_user_id(username):
    target_user = filter(lambda t: t['username'] == username, users)
    if not target_user:
        raise ValueError('UserNotFound: %s' % username)
    return target_user[0]['id']
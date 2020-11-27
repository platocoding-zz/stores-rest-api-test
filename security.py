from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username,password):
    """
    Function that gets called when a user calls the auth endpoint
    with their username and password
    :param username: User's username in str format
    :param password: Password un-encrypted password in str format
    :return A UserModel obj if authentication was successful, None otherwise.
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user


def identity(payload):
    """
    Function that gets called when user has already authenticated, and Flask-JWT
    verified their authorization header is correct
    :param payload: A dict with 'identity' as a key, which is the user id
    :return: A UserModel obj
    """

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
"""Contains User class"""


class User(object):
    """User class"""
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'

    def __init__(self):
        """Initialize class attributes"""
        self.username = None
        self.email = None
        self.password = None

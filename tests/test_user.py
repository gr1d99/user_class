import unittest
from user_model import User, Users


class TestUser(unittest.TestCase):
    """Tests all functionalities"""

    def setUp(self):
        self.user = User()
        self.users = Users()

    #  -->start of User attributes<--
    def test_default_username_value(self):
        self.assertTrue(self.user.username is None)

    def test_default_email_value(self):
        self.assertTrue(self.user.email is None)

    def test_default_password_value(self):
        self.assertTrue(self.user.password is None)

    def test_get_username(self):
        self.assertTrue(self.user.get_username is None)

    def test_get_email(self):
        self.assertTrue(self.user.get_email is None)
    #  -->end of User attributes<--

    # -->start of Users attributes<--


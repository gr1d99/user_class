import unittest
from user_model import User


class TestUser(unittest.TestCase):
    """Tests all functionalities"""

    def setUp(self):
        self.user = User()

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


if __name__ == '__main__':
    unittest.main()

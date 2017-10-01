import unittest
from model.user import User


class TestUser(unittest.TestCase):
    """Tests all functionalities"""

    def setUp(self):
        self.user = User()

    #  -->start of User attributes and methods<--
    def test_has_username_field(self):
        self.assertTrue(hasattr(self.user, 'USERNAME_FIELD'))

    def test_has_email_field(self):
        self.assertTrue(hasattr(self.user, 'EMAIL_FIELD'))

    def test_has_password_field(self):
        self.assertTrue(hasattr(self.user, 'PASSWORD_FIELD'))

    def test_username_default_is_none(self):
        self.assertTrue(getattr(self.user, self.user.USERNAME_FIELD) is None)

    def test_email_default_is_none(self):
        self.assertTrue(getattr(self.user, self.user.EMAIL_FIELD) is None)

    def test_password_default_is_none(self):
        self.assertTrue(getattr(self.user, self.user.PASSWORD_FIELD) is None)

    #  -->end of User attributes<--


if __name__ == '__main__':
    unittest.main()

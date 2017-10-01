import unittest
from user_model import User


class TestUser(unittest.TestCase):
    """Tests all functionalities"""

    def setUp(self):
        self.user = User()

    #  -->start of User attributes and methods<--
    def test_has_username_field(self):
        self.assertTrue(hasattr(self.user, 'USERNAME_FIELD'))

    #  -->end of User attributes<--


if __name__ == '__main__':
    unittest.main()

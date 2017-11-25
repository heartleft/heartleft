import unittest

from heartleft.app.db import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='example')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='example')
        with self.assertRaises(AttributeError):
            tmp = u.password

    def test_password_verification(self):
        u = User(password='example')
        self.assertTrue(u.verify_password('example'))
        self.assertFalse(u.verify_password('wrong'))

    def test_password_salts_are_random(self):
        u = User(password='example')
        u2 = User(password='example')
        self.assertTrue(u.password_hash != u2.password_hash)

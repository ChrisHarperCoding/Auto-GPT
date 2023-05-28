import pinterest_api
import os
import unittest

class TestPinterestApp(unittest.TestCase):
    def test_login(self):
        username = os.environ.get('PINTEREST_USERNAME')
        password = os.environ.get('PINTEREST_PASSWORD')
        pinterest_api.login(username, password)
        self.assertTrue(pinterest_api.is_logged_in())
        pinterest_api.logout()

    def test_browse_posts(self):
        pinterest_api.browse_posts()
        self.assertTrue(pinterest_api.is_browsing_posts())

    def test_logout(self):
        pinterest_api.logout()
        self.assertFalse(pinterest_api.is_logged_in())

if __name__ == '__main__':
    unittest.main()
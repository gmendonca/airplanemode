import unittest
from context import airplanemode

class ViewsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = airplanemode.app.test_client()

    def test_hello_word(self):
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data.decode('utf-8')

if __name__ == '__main__':
    unittest.main()

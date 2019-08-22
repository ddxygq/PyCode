import os
import unittest
import tempfile
import flaskr


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        print(flaskr.app.config['DATABASE'])
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_table()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        print(str(rv.data))
        assert 'No entries here so far' not in str(rv.data)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        """测试登陆、登出"""
        rv = self.login('name', 'password')
        assert 'You were logged in' in str(rv.data)

        rv = self.logout()
        assert 'You were logged out' in str(rv.data)


if __name__ == '__main__':
    unittest.main()
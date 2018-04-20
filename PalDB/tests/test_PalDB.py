#! /usr/bin/env python2.7
__author__ = "Adam Richardson"
__Date__ = 18 / 04 / 18

import os
import PalDB
import unittest
import tempfile


class PalDBTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, PalDB.app.config['DATABASE'] = tempfile.mkstemp()
        PalDB.app.testing = True
        self.app = PalDB.app.test_client()
        with PalDB.app.app_context():
            PalDB.Pal.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(PalDB.app.config['DATABASE'])

    # Test to see if home page works
    def test_loads(self):
        rv = self.app.get('/')
        assert b'Please add you palindromes below:' in rv.data

    # Test to see if a non-palindrome was rejected
    def test_rejection(self):
        rv = self.app.post('/add', data=dict(
            palindromes="Not a palindrome"
        ), follow_redirects=True)
        assert b'Sorry, your word was not a palindrome' in rv.data

    # Test to see if a palindrome was accepted
    def test_new_pal(self):
        rv = self.app.post('/add', data=dict(
            palindromes="Dammit I'm mad"
        ), follow_redirects=True)
        assert b'New palindrome accepted' in rv.data

if __name__ == '__main__':
    unittest.main()

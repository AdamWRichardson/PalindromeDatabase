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

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(PalDB.app.config['DATABASE'])

    def test_loads(self):
        rv = self.app.get('/')
        assert b'Please add you palindromes below:' in rv.data

    def test_rejection(self):
        rv = self.app.post('/add', data=dict(
            title="<strong>HTML</strong> Not a palindrome"
        ), follow_redirects=True)
        assert b'Sorry, your word was not a palindrome' in rv.data

    def test_pal_entry(self):
        self.app.post('/add', data=dict(
            title="<Dammit I'm mad>"
        ), follow_redirects=True)
        rv = self.app.get('/display')
        assert b"Dammit I'm mad" in rv.data


if __name__ == '__main__':
    unittest.main()

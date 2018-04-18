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

if __name__ == '__main__':
    unittest.main()
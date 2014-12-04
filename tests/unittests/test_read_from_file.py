#from __future__ import unicode_literals
from unittest import TestCase
import unittest
import mock
import game.io_
import StringIO

__author__ = 'avasilyev2'

TEST_TEXT = """
domain1.com
domain2.com
domain3.com
"""

class TestReadFromFile(TestCase):
    def test_read_from_file(self):
        my_mock = mock.MagicMock(spec=file)
        with mock.patch('__builtin__.open', mock.mock_open(read_data=TEST_TEXT), create=True):
            lines = game.io_.read_from_file(my_mock)
        self.assertEquals(lines, TEST_TEXT.strip().splitlines())

    def test_get_answer(self):
        f = ["12\n", "23\n", "34\n"]
        ret = game.io_.get_answer(f)
        self.assertIsInstance(ret, list, "List should be returned")

    def test_get_guess(self):
        f = ["12345\n", "12346\n", "12347\n"]
        ret = game.io_.get_guess(f)
        self.assertIsInstance(ret, str, "Str should be returned")
        pass

if __name__ == '__main__':
    unittest.main()
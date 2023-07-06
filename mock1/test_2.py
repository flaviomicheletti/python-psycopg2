import unittest
from unittest.mock import MagicMock, patch

from script import get_languages


class TestGetLanguages(unittest.TestCase):

    def setUp(self):
        # configure mock database connection
        self.mock_cursor = MagicMock()
        self.mock_cursor.fetchall.return_value = [('English',), ('Spanish',)]

        self.mock_conn = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

        # patch the psycopg2.connect method to return the mock connection
        self.patcher = patch('psycopg2.connect', return_value=self.mock_conn)
        self.patcher.start()

    def tearDown(self):
        # stop the patcher
        self.patcher.stop()

    def test_get_languages(self):
        # call the function and assert the result
        result = get_languages()
        self.assertEqual(result, [('English',), ('Spanish',)])

        # assert that the mock connection and cursor were called with the correct arguments
        self.mock_conn.cursor.assert_called_once()
        self.mock_cursor.execute.assert_called_once_with('SELECT * FROM languages')
        self.mock_cursor.fetchall.assert_called_once()
        self.mock_cursor.close.assert_called_once()


#
# 100% coverage
#
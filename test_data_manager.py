import unittest
from unittest.mock import MagicMock, patch
from data_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        db_name = "test_db"
        db_user = "test_user"
        db_password = "test_password"
        db_host = "localhost"
        db_port = 5432
        self.manager = DatabaseManager(db_name, db_user, db_password, db_host, db_port)

        # Simuliuokite prisijungimo metodą
        self.manager.__connection = MagicMock()
        self.manager.__cursor = MagicMock()

    @patch('data_manager.DatabaseManager.execute_query')
    def test_create_table(self, mock_execute_query):
        create_table_query = "CREATE TABLE TestTable (id SERIAL PRIMARY KEY, name VARCHAR(50));"
        self.manager.execute_query(create_table_query)
        mock_execute_query.assert_called_once_with(create_table_query)

    @patch('data_manager.DatabaseManager.execute_query')
    def test_delete_data(self, mock_execute_query):
        delete_query = "DELETE FROM TestTable WHERE id = %s;"
        self.manager.execute_query(delete_query, (1,))
        mock_execute_query.assert_called_once_with(delete_query, (1,))

    @patch('data_manager.DatabaseManager.execute_query')
    def test_insert_data(self, mock_execute_query):
        insert_query = "INSERT INTO TestTable (name) VALUES (%s);"
        self.manager.execute_query(insert_query, ('John',))
        mock_execute_query.assert_called_once_with(insert_query, ('John',))

    @patch('data_manager.DatabaseManager.execute_query')
    def test_update_data(self, mock_execute_query):
        update_query = "UPDATE TestTable SET name = %s WHERE id = %s;"
        self.manager.execute_query(update_query, ('John', 1))
        mock_execute_query.assert_called_once_with(update_query, ('John', 1))

    @patch('data_manager.psycopg2.connect')
    def test_database_connection(self, mock_connect):
        mock_connect.return_value = MagicMock()

        try:
            self.manager.connect()
            self.assertIsNotNone(self.manager._DatabaseManager__connection, "Failed to connect to the database.")
            self.assertIsNotNone(self.manager._DatabaseManager__cursor, "Failed to create a database cursor.")
        except Exception as e:
            self.fail(f"An exception occurred: {e}")

if __name__ == '__main__':
    unittest.main()

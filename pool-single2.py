import psycopg2
from psycopg2 import pool


class Database:
    def __init__(self, min_connections, max_connections, **kwargs):
        self.connection_pool = pool.SimpleConnectionPool(
            minconn=min_connections,
            maxconn=max_connections,
            **kwargs
        )

    def get_connection(self):
        return self.connection_pool.getconn()

    def return_connection(self, connection):
        self.connection_pool.putconn(connection)

    def close_all_connections(self):
        self.connection_pool.closeall()


class MyApp:
    def __init__(self, database):
        self.database = database

    def perform_query(self):
        connection = self.database.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM your_table")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            cursor.close()
        finally:
            self.database.return_connection(connection)


# Create a database instance with connection pool settings
min_connections = 1
max_connections = 5
database = Database(
    min_connections=min_connections,
    max_connections=max_connections,
    host='your_host',
    port='your_port',
    dbname='your_database',
    user='your_username',
    password='your_password'
)

# Create an instance of the application with the database
app = MyApp(database)

# Perform a query using the application
app.perform_query()

# Close all connections in the pool
database.close_all_connections()

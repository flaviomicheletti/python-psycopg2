import config
from psycopg2 import pool

# Create a connection pool
min_connections = 1
max_connections = 5
connection_pool = pool.SimpleConnectionPool(
    minconn=min_connections,
    maxconn=max_connections,
    host=config.host,
    port=config.port,
    database=config.database,
    user=config.user,
    password=config.password
)

# Get a connection from the pool
connection = connection_pool.getconn()

try:
    # Use the connection to perform database operations
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

finally:
    # Return the connection to the pool
    connection_pool.putconn(connection)

# Close all connections in the pool
connection_pool.closeall()

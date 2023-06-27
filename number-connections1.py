"""
The get_total_connections() function establishes a connection to the database 
using psycopg2, executes a query to retrieve the count of connections from 
pg_stat_activity, and then returns the total number of connections. You can 
call this function whenever you want to monitor the current number of 
connections in your application. 
"""

import psycopg2
import config


def get_total_connections():
    conn = psycopg2.connect(
        host=config.host,
        port=config.port,
        database=config.database,
        user=config.user,
        password=config.password
    )
    cursor = conn.cursor()

    query = "SELECT count(*) FROM pg_stat_activity WHERE datname = current_database();"
    cursor.execute(query)

    total_connections = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total_connections


# Usage
total_connections = get_total_connections()
print("Total connections:", total_connections)

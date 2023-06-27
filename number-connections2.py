"""
By enabling and querying the `pg_stat_statements` extension, you can get 
insights into the number of statements executed, which can indirectly 
indicate the number of connections made to the database. 

1. Enable `pg_stat_statements` in PostgreSQL:
```sql
-- Connect to your PostgreSQL database using an administrator account
psql -U your_user -d your_database

-- Enable the extension
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

In this example, after enabling the pg_stat_statements extension, the 
get_total_connections() function connects to the database, executes a query 
to sum the number of calls made to all statements, and returns the total 
number of statements executed. While this metric doesn't directly represent 
the number of connections, it can provide an approximation of the activity 
level in the database, which is often correlated with connection counts. 

Note that enabling pg_stat_statements has some overhead on the database 
performance, so it should be used with caution in production environments.
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

    query = "SELECT sum(calls) FROM pg_stat_statements;"
    cursor.execute(query)

    total_statements_executed = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total_statements_executed


# Usage
total_statements = get_total_connections()
print("Total statements executed:", total_statements)


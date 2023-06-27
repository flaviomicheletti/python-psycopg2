import psycopg2
import config

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=config.host,
    port=config.port,
    database=config.database,
    user=config.user,
    password=config.password
)

# Create a cursor object to interact with the database
curs = conn.cursor()

# Define the SQL statement for deleting data
delete_query = "DELETE FROM your_table_name WHERE column1 = %s"

# Define the value for the deletion condition
condition_value = "Condition Value"

# Execute the delete statement
curs.execute(delete_query, (condition_value,))

# Commit the transaction
conn.commit()

# Close the cursor and the connection
curs.close()
conn.close()

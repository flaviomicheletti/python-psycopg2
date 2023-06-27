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

# Define the SQL statement for updating data
update_query = "UPDATE your_table_name SET column1 = %s WHERE column2 = %s"

# Define the new values for the update
new_value = "New Value"
condition_value = "Condition Value"

# Execute the update statement
curs.execute(update_query, (new_value, condition_value))

# Commit the transaction
conn.commit()

# Close the cursor and the connection
curs.close()
conn.close()

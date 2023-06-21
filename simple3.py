import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
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

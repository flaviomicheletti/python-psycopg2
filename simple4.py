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

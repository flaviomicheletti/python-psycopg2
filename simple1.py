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

# Execute a query
curs.execute("SELECT * FROM your_table_name")

# Fetch all rows from the result set
rows = curs.fetchall()

# Process the fetched data
for row in rows:
    print(row)

# Close the curs and the connection
curs.close()
conn.close()

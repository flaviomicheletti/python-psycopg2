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

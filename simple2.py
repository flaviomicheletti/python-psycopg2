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

# Define the SQL statement for inserting data
insert_query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"

# Data to be inserted
data = [
    ("Value1", 10),
    ("Value2", 20),
    ("Value3", 30)
]

# Execute the insert statement for each row of data
for row in data:
    curs.execute(insert_query, row)

# Commit the transaction
conn.commit()

# Close the cursor and the connection
curs.close()
conn.close()

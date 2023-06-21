import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

try:
    # Create a cursor object to interact with the database
    curs = conn.cursor()

    # Begin the transaction
    curs.execute("BEGIN;")

    try:
        # Execute multiple queries within the transaction
        curs.execute("INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)", ("Value1", 10))
        curs.execute("UPDATE your_table_name SET column1 = %s WHERE column2 = %s", ("New Value", 10))
        
        # Commit the transaction
        conn.commit()
        
        print("Transaction successfully executed!")
    
    except Exception as e:
        # Rollback the transaction in case of an error
        conn.rollback()
        print("Transaction rolled back due to error:", str(e))

    # Close the cursor
    curs.close()

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL:", error)

finally:
    # Close the connection
    conn.close()

# Concept of cursor

- https://www.psycopg.org/docs/cursor.html
- https://www.psycopg.org/docs/usage.html#server-side-cursors

In the context of database programming, a cursor is a database object or data 
structure that allows you to retrieve and manipulate rows from a result set 
obtained from a database query. It provides a way to navigate through the 
query results and perform operations such as fetching data, updating rows, 
inserting new rows, or deleting rows. 

Here are some key concepts related to cursors: 

1. Result Set: When you execute a database query, the database management 
system (DBMS) returns a result set, which is a collection of rows that 
satisfy the query. A cursor provides a way to iterate over this result set 
and access the individual rows. 

2. Cursor Object: A cursor object represents a position within the result 
set. It provides methods and attributes to navigate through the result set, 
fetch data from the current position, and perform operations on the data. 

3. Fetching Data: Cursors typically provide methods like `fetchone()`, `
fetchmany()`, and `fetchall()` to retrieve rows from the result set. These 
methods allow you to fetch a single row, a specified number of rows, or all 
remaining rows, respectively. 

4. Cursor Position: Cursors maintain an internal position that tracks the 
current row being accessed. Initially, the cursor points to the first row in 
the result set. As you fetch rows, the cursor moves forward through the 
result set. You can also move the cursor to a specific position using methods 
like `scroll()`. 

5. Data Manipulation: In addition to fetching data, cursors can be used to 
perform various database operations. For example, you can use a cursor to 
update rows in the result set or insert new rows into a table. 

6. Transaction Scope: Cursors are often associated with database 
transactions. They allow you to perform a series of operations within a 
transaction context, where changes made by the cursor are not visible to 
other transactions until the transaction is committed. 

It's important to note that the exact behavior and functionality of cursors 
may vary depending on the specific database management system and the 
database library or API you are using. Psycopg2, for example, provides a 
cursor object that follows the Python Database API Specification 2.0 (PEP 
249), which defines a common interface for database access in Python.
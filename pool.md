# pool docs

- https://www.psycopg.org/docs/pool.html

1. `psycopg2.pool.AbstractConnectionPool`: This is the base class 
   implementing generic key-based pooling code. It defines the basic behavior of 
   a connection pool, including creating new connections, retrieving a 
   connection from the pool, returning a connection to the pool, and closing all 
   connections in the pool. Subclasses of this base class are expected to 
   implement specific behavior. 

    Methods: 

    - `getconn(key=None)`: Retrieves a free connection from the pool. If a key is 
    specified, the connection will be associated with that key, and subsequent 
    calls to `getconn()` with the same key will return the same connection. 
    
    - `putconn(conn, key=None, close=False)`: Put away a connection. 
    If `close` is set to `True`, the connection is discarded from the pool. The `
    key` parameter should be used consistently with the key used to retrieve the 
    connection. 
    
    - `closeall()`: Closes all connections in the pool, including ones that are 
    currently in use by the application. 

2. `psycopg2.pool.SimpleConnectionPool`: This is a subclass of `
    AbstractConnectionPool` that provides a simple connection pool implementation 
    suitable for single-threaded applications. It cannot be shared across 
    different threads. 

3. `psycopg2.pool.ThreadedConnectionPool`: This is another subclass of `
   AbstractConnectionPool` that works with the `threading` module. It is 
   designed to be used in multi-threaded applications and can safely manage 
   connections across different threads. 


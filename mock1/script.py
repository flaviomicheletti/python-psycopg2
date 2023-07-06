import psycopg2

# configuration
DEBUG = True
HOST = "localhost"
PORT = "5438"
DATABASE = "yourDatabase"
USERNAME = "john"
PASSWORD = "1234"


# set up the database connection
def getConn():
    return psycopg2.connect(
        dbname=DATABASE,
        user=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )


def get_languages():
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM languages")
    languages = cursor.fetchall()
    cursor.close()
    return languages


""""
print(get_languages())
[
    (1, 'English', datetime.datetime(2023, 3, 1, 12, 0), datetime.datetime(2023, 3, 1, 12, 0)), 
    (2, 'Spanish', datetime.datetime(2023, 3, 2, 12, 0), datetime.datetime(2023, 3, 2, 12, 0)), 
    (3, 'French', datetime.datetime(2023, 3, 3, 12, 0), datetime.datetime(2023, 3, 3, 12, 0)), 
    (4, 'German', datetime.datetime(2023, 3, 4, 12, 0), datetime.datetime(2023, 3, 4, 12, 0)), 
    (5, 'Italian', datetime.datetime(2023, 3, 5, 12, 0), datetime.datetime(2023, 3, 5, 12, 0))
]
"""
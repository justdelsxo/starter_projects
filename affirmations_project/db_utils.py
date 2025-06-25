import mysql.connector
from config import USER, PASSWORD, HOST, DB_NAME

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    return cnx

def get_daily_affirmation():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print(f"Connected to DB: {DB_NAME}")

        query = """
            SELECT text
            FROM affirmations 
            ORDER BY RAND() 
            LIMIT 1;
        """

        cur.execute(query)
        result = cur.fetchone()

        if result:
            return result[0]
        else:
            return "No affirmations found."

    except Exception as e:
        print(f"Error: {e}")
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def add_affirmation_to_db(text, author, category):
    cnx = None
    try:
        cnx = _connect_to_db()
        cursor = cnx.cursor()

        query = """
            INSERT INTO affirmations (text, author, category)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (text, author, category))
        cnx.commit()
        return "Affirmation added successfully"

    except Exception as e:
        raise DbConnectionError(f"DB insert error: {e}")

    finally:
        if cnx:
            cnx.close()



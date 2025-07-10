import mysql.connector
from config import USER, PASSWORD, HOST, DB_NAME

class DbConnectionError(Exception):
    pass

# initialise connection with my mysql database
def _connect_to_db():
    db_connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    return db_connection

# get a random affirmation from the database
def get_daily_affirmation():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor()
        print(f"Connected to DB: {DB_NAME}")
# SQL query to select a random affirmation
        query = """
            SELECT text
            FROM affirmations 
            ORDER BY RAND() 
            LIMIT 1;
        """

        cursor.execute(query)
        result = cursor.fetchone()
# return error message if none found, if found, return a affirmation
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

# add a new affirmation to the database
def add_affirmation_to_db(text, author, category):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor()

# SQL insert query
        query = """
            INSERT INTO affirmations (text, author, category)
            VALUES (%s, %s, %s) 
        """
        cursor.execute(query, (text, author, category))
        db_connection.commit()
        return "Affirmation added successfully"

    except Exception as e:
        raise DbConnectionError(f"DB insert error: {e}")

    finally:
        if db_connection:
            db_connection.close()

# get all affirmations for the specified category
def get_affirmations_for_category(category):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cursor = db_connection.cursor()
        query = """
            SELECT text, author
            FROM affirmations
            WHERE category = %s
        """
        cursor.execute(query, (category,))
        results = cursor.fetchall()

        # if results are found, return results in the below format
        if results:
            return [{'text': text, 'author': author} for text, author in results]
        else:
            return ["Sorry, no affirmations found for this category, try a different category or add your own affirmation :)"] # if not found, return error message

    except Exception as e:
        raise DbConnectionError(f"DB query error: {e}") # if the query fails, return error

    finally:
        if db_connection:
            db_connection.close()




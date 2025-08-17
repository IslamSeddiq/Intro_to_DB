import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Try to connect to MySQL Server (no database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Always close the connection
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run function
create_database()

mycursor.close()
mydb.close()

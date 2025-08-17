import mysql.connector
from mysql.connector import Error

def create_tables():
    connection = None
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="alx_book_store"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Authors table first (referenced by Books)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Authors(
                author_id INT PRIMARY KEY,
                author_name VARCHAR(215)
            )
            """)
            print("Table 'Authors' created successfully!")

            # Books table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books(
                book_id INT PRIMARY KEY,
                title VARCHAR(130),
                price DOUBLE,
                publication_date DATE,
                author_id INT,
                FOREIGN KEY (author_id) REFERENCES Authors(author_id)
            )
            """)
            print("Table 'Books' created successfully!")

            # Customers table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers(
                customer_id INT PRIMARY KEY,
                customer_name VARCHAR(215),
                email VARCHAR(215),
                address TEXT
            )
            """)
            print("Table 'Customers' created successfully!")

            # Orders table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders(
                order_id INT PRIMARY KEY,
                customer_id INT,
                order_date DATE,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
            """)
            print("Table 'Orders' created successfully!")

            # Order_Details table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Order_Details(
                orderdetailid INT PRIMARY KEY,
                book_id INT,
                order_id INT,
                quantity DOUBLE,
                FOREIGN KEY (book_id) REFERENCES Books(book_id),
                FOREIGN KEY (order_id) REFERENCES Orders(order_id)
            )
            """)
            print("Table 'Order_Details' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

# Run function
create_tables()
import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
    host="localhost",       # Change if needed
    user="root",            # Your MySQL username
    password="root",    # Your MySQL password
    database ="alx_book_store"
)

cursor = mydb.cursor()
cursor.execute("USE alx_book_store;")

# Create Authors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
)
""")

# Create Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    price DECIMAL(10,2),
    publication_date DATE,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
)
""")

# Create Customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
)
""")

# Create Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

# Create Order_Details table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT PRIMARY KEY,
    book_id INT,
    order_id INT,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
)
""")

print("Database and tables created successfully!")

# Close connection
cursor.close()
mydb.close()

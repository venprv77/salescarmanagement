import MySQLdb


class DatabaseConnection:

    def __init__(self):
        self.con = MySQLdb.connect(
            host="localhost",
            user="root",
            password="moksha"
        )

        self.cursor = self.con.cursor()

        self.cursor.execute(
            "CREATE DATABASE IF NOT EXISTS car_sales_db"
        )

        self.cursor.execute("USE car_sales_db")

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars(
                car_id INT PRIMARY KEY AUTO_INCREMENT,
                brand VARCHAR(50),
                model VARCHAR(50),
                price FLOAT,
                quantity INT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50),
                phone VARCHAR(20),
                email VARCHAR(100)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales(
                sale_id INT PRIMARY KEY AUTO_INCREMENT,
                car_id INT,
                customer_id INT,
                sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                sale_price FLOAT,
                FOREIGN KEY(car_id) REFERENCES cars(car_id),
                FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
            )
        """)

        self.con.commit()

    def close(self):
        self.cursor.close()
        self.con.close()
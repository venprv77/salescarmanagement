from car import Car
from customer import Customer
from sale import Sale


class CarSalesSystem:

    def __init__(self, db):
        self.con = db.con
        self.cursor = db.cursor

    # ---------- CAR ----------

    def add_car(self):

        brand = input("Brand: ")
        model = input("Model: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        car = Car(brand, model, price, quantity)

        sql = """
        INSERT INTO cars(brand, model, price, quantity)
        VALUES(%s,%s,%s,%s)
        """

        self.cursor.execute(
            sql,
            (car.brand, car.model, car.price, car.quantity)
        )

        self.con.commit()

        print("Car added successfully.")

    def view_cars(self):

        self.cursor.execute("SELECT * FROM cars")

        rows = self.cursor.fetchall()

        print("\nID  Brand  Model  Price  Quantity")

        for row in rows:
            print(row)

    def search_car(self):

        name = input("Enter brand/model: ")

        self.cursor.execute(
            """
            SELECT * FROM cars
            WHERE brand LIKE %s OR model LIKE %s
            """,
            ("%" + name + "%", "%" + name + "%")
        )

        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def update_car(self):

        car_id = int(input("Car ID: "))
        price = float(input("New Price: "))

        self.cursor.execute(
            """
            UPDATE cars
            SET price=%s
            WHERE car_id=%s
            """,
            (price, car_id)
        )

        self.con.commit()

        print("Car updated.")

    def delete_car(self):

        car_id = int(input("Car ID: "))

        self.cursor.execute(
            "DELETE FROM cars WHERE car_id=%s",
            (car_id,)
        )

        self.con.commit()

        print("Car deleted.")

    # ---------- CUSTOMER ----------

    def add_customer(self):

        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        customer = Customer(name, phone, email)

        self.cursor.execute(
            """
            INSERT INTO customers(name,phone,email)
            VALUES(%s,%s,%s)
            """,
            (
                customer.name,
                customer.phone,
                customer.email
            )
        )

        self.con.commit()

        print("Customer added.")

    def view_customers(self):

        self.cursor.execute(
            "SELECT * FROM customers"
        )

        for row in self.cursor.fetchall():
            print(row)

    def search_customer(self):

        name = input("Customer name: ")

        self.cursor.execute(
            """
            SELECT * FROM customers
            WHERE name LIKE %s
            """,
            ("%" + name + "%",)
        )

        for row in self.cursor.fetchall():
            print(row)

    def update_customer(self):

        customer_id = int(input("Customer ID: "))
        phone = input("New Phone: ")
        email = input("New Email: ")

        self.cursor.execute(
            """
            UPDATE customers
            SET phone=%s,email=%s
            WHERE customer_id=%s
            """,
            (phone, email, customer_id)
        )

        self.con.commit()

        print("Customer updated.")

    def delete_customer(self):

        customer_id = int(input("Customer ID: "))

        self.cursor.execute(
            """
            DELETE FROM customers
            WHERE customer_id=%s
            """,
            (customer_id,)
        )

        self.con.commit()

        print("Customer deleted.")

    # ---------- SALE ----------

    def sell_car(self):

        customer_id = int(input("Customer ID: "))
        car_id = int(input("Car ID: "))

        self.cursor.execute(
            "SELECT * FROM cars WHERE car_id=%s",
            (car_id,)
        )

        car = self.cursor.fetchone()

        if car is None:
            print("Car not found.")
            return

        if car[4] <= 0:
            print("Car is unavailable.")
            return

        sale = Sale(
            car_id,
            customer_id,
            car[3]
        )

        self.cursor.execute(
            """
            INSERT INTO sales
            (car_id,customer_id,sale_price)
            VALUES(%s,%s,%s)
            """,
            (
                sale.car_id,
                sale.customer_id,
                sale.price
            )
        )

        self.cursor.execute(
            """
            UPDATE cars
            SET quantity=quantity-1
            WHERE car_id=%s
            """,
            (car_id,)
        )

        self.con.commit()

        print("Car sold successfully.")

    # ---------- SALES ----------

    def view_sales(self):

        sql = """
        SELECT
            s.sale_id,
            c.name,
            ca.brand,
            ca.model,
            s.sale_price,
            DATE_FORMAT(s.sale_date, '%%d-%%m-%%Y %%h:%%i:%%s %%p')

        FROM sales s

        JOIN customers c
        ON s.customer_id=c.customer_id

        JOIN cars ca
        ON s.car_id=ca.car_id
        """

        self.cursor.execute(sql)

        print("\nSaleID Customer Car Price Date")

        for row in self.cursor.fetchall():
            print(row)
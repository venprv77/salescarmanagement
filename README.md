# Car Sales Management System

## Python Practical Task

This project combines:

- Python
- OOP
- PDBC
- MySQL
- SQL
- SQL JOIN

## Project Structure

car_sales_system/

    main.py
    database.py
    car.py
    customer.py
    sale.py
    car_sales_system.py
    README.md

## Database

Database name:

car_sales_db

Tables:

1. cars
2. customers
3. sales

## MySQL Configuration

Open database.py.

Change these values if required:

host = "localhost"
user = "root"
password = "moksha"

## Install MySQL Library

Run:

pip install mysqlclient

## Run the Project

Make sure MySQL is running.

Then open PowerShell inside the project folder.

Run:

python main.py

## Car Operations

1. Add Car
2. View Cars
3. Search Car
4. Update Car Price
5. Update Car Quantity
6. Delete Car

## Customer Operations

1. Add Customer
2. View Customers
3. Search Customer
4. Update Customer
5. Delete Customer

## Sale Process

1. Enter Customer ID
2. Enter Car ID
3. Check customer
4. Check car
5. Check available quantity
6. Create sale
7. Reduce available quantity
8. Store sale in sales table

## OOP Classes

### Car

Represents a car.

Attributes:

- car_id
- brand
- model
- price
- available_quantity

### Customer

Represents a customer.

Attributes:

- customer_id
- name
- phone
- email

### Sale

Represents a car sale.

Attributes:

- sale_id
- car_id
- customer_id
- sale_price
- sale_date

### DatabaseConnection

Handles:

- MySQL connection
- Database creation
- Table creation
- Connection closing

### CarSalesSystem

Handles:

- Car operations
- Customer operations
- Sales operations
- Business logic

## Important Questions for Viva

### 1. Why did you create separate classes?

Each class represents a real-world entity and has its own responsibility.

### 2. How does Python connect to MySQL?

Python uses the MySQL database connectivity library and creates a connection using host, username and password.

### 3. What is %s?

%s is a parameter placeholder used in SQL queries.

Example:

cursor.execute(
    "SELECT * FROM cars WHERE car_id = %s",
    (car_id,)
)

### 4. What is a primary key?

A primary key uniquely identifies each record in a table.

### 5. What is a foreign key?

A foreign key connects one table with another table.

### 6. Why is JOIN used?

JOIN combines related data from multiple tables.

### 7. How does selling work?

The system checks the customer, checks the car, checks available quantity, creates the sale and decreases the car quantity.

### 8. Why is commit() used?

commit() permanently saves INSERT, UPDATE and DELETE changes to the database.

### 9. Why is rollback() used?

rollback() cancels changes when an error occurs.

### 10. What happens if quantity is 0?

The system displays:

Car is currently unavailable.

and does not create the sale.
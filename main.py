from database import DatabaseConnection
from car_sales_system import CarSalesSystem


db = DatabaseConnection()
system = CarSalesSystem(db)


while True:

    print("\n===== CAR SALES SYSTEM =====")

    print("1. Add Car")
    print("2. View Cars")
    print("3. Search Car")
    print("4. Update Car")
    print("5. Delete Car")

    print("6. Add Customer")
    print("7. View Customers")
    print("8. Search Customer")
    print("9. Update Customer")
    print("10. Delete Customer")

    print("11. Sell Car")
    print("12. View Sales")
    print("13. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":
            system.add_car()

        elif choice == "2":
            system.view_cars()

        elif choice == "3":
            system.search_car()

        elif choice == "4":
            system.update_car()

        elif choice == "5":
            system.delete_car()

        elif choice == "6":
            system.add_customer()

        elif choice == "7":
            system.view_customers()

        elif choice == "8":
            system.search_customer()

        elif choice == "9":
            system.update_customer()

        elif choice == "10":
            system.delete_customer()

        elif choice == "11":
            system.sell_car()

        elif choice == "12":
            system.view_sales()

        elif choice == "13":
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)


db.close()
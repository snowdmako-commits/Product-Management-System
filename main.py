from database import *
from product import addProduct, showProducts, removeProduct, filterProducts
from csv_operations import saveToCSV, showCSV


products = loadProducts()

while True:
    print("""
    ===== PRODUCT MANAGEMENT SYSTEM =====

    1. Add Product
    2. Show All Products
    3. Remove Product
    4. Filter Products by Price
    5. Save Products to JSON
    6. Load Products from JSON
    7. Save Products to CSV
    8. Show Products from CSV
    9. Exit
    """)

    try:
        choice = input("enter choice: ")

        if choice == "1":
            addProduct(products)

        elif choice == "2":
            showProducts(products)

        elif choice == "3":
            removeProduct(products)

        elif choice == "4":
            filterProducts(products)

        elif choice == "5":
            saveProducts(products)
            print("products saved to JSON")

        elif choice == "6":
            products = loadProducts()
            print("products loaded from JSON")

        elif choice == "7":
            saveToCSV(products)

        elif choice == "8":
            showCSV()

        elif choice == "9":
            print("goodbye")
            break

        else:
            print("invalid choice! Please choose 1-9.")

    except Exception as e:
        print("an error occurred:", e)

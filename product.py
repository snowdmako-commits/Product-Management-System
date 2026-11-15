from database import saveProducts


def addProduct(products):
    try:
        productID = 1

        if products:
            for p in products:
                if p["id"] >= productID:
                    productID = p["id"] + 1

        name = input("enter product name: ")

        if not name.strip():
            print("name cannot be empty")
            return

        price = float(input("enter product price: "))
        quantity = int(input("enter product quantity: "))

        if price <= 0:
            print("price must be greater than 0")
            return

        if quantity < 0:
            print("quantity cannot be negative")
            return

        product = {
            "id": productID,
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)
        saveProducts(products)

        print("product added successfully")

    except ValueError:
        print("please enter valid numbers")

def showProducts(products):
    if not products:
        print("product list is empty")
        return

    for p in products:
        print("--------------------")
        print("ID:", p["id"])
        print("Name:", p["name"])
        print("Price:", p["price"])
        print("Quantity:", p["quantity"])

def removeProduct(products):
    try:
        productID = int(input("enter product ID: "))

        for p in products:
            if p["id"] == productID:
                products.remove(p)
                saveProducts(products)
                print("product removed")
                return

        print("product not found")

    except ValueError:
        print("please enter a valid ID")

def filterProducts(products):
    if not products:
        print("product list is empty")
        return

    print("""
        1. Ascending (Low - High)
        2. Descending (High - Low)
    """)

    choice = input("enter choice: ")

    if choice == "1":
        sortedProducts = sorted(products,key=lambda p: p["price"])

    elif choice == "2":
        sortedProducts = sorted(products,key=lambda :p["price"],reverse=True)

    else:
        print("invalid choice")
        return

    for p in sortedProducts:
        print(p)
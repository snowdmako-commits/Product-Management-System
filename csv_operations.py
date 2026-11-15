import csv

def saveToCSV(products):
    try:
        file = open("products.csv", "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(file, fieldnames=["id", "name", "price", "quantity"])

        writer.writeheader()
        writer.writerows(products)

        file.close()
        print("products saved successfully")

    except FileNotFoundError as e:
        print("file not found:", e)

    except Exception as e:
        print("Error:", e)

def loadFromCSV():
    try:
        file = open("products.csv", "r", encoding="utf-8")
        reader = csv.DictReader(file)

        products = []

        for p in reader:
            products.append({
                "id": int(p["id"]),
                "name": p["name"],
                "price": float(p["price"]),
                "quantity": int(p["quantity"])
            })

        file.close()
        return products

    except FileNotFoundError as e:
        print("file not found:", e)
        return []

    except (ValueError, KeyError) as e:
        print("invalid CSV data:", e)
        return []

    except Exception as e:
        print("Error:", e)
        return []

def showCSV():
    try:
        products = loadFromCSV()

        if not products:
            print("no products found")
            return

        for p in products:
            print(p)

    except Exception as e:
        print("Error:", e)

        
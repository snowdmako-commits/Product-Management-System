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
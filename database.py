import json

def loadProducts():
    try:
        file = open("products.json", "r", encoding="utf-8")
        products = json.load(file)
        file.close()
        return products

    except FileNotFoundError:
        print("file not found")
        return []

def saveProducts(products):
    file = open("products.json", "w", encoding="utf-8")
    json.dump(products, file, indent=4)
    file.close()
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
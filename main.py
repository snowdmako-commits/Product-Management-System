from database import *
from product import *
from csv_operations import *

products = loadProducts()

while True:
    print("""

===== PRODUCT MANAGEMENT SYSTEM =====

# 1. Add Product
# 2. Show All Products
# 3. Remove Product
# 4. Filter Products by Price
# 5. Save Products to JSON
# 6. Load Products from JSON
# 7. Save Products to CSV
# 8. Show Products from CSV
# 9. Exit

""")
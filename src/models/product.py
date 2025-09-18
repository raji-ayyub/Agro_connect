import json
import random, string
import os

class Product:
    def __init__(self, farmer_id, product_name, unit_price, location, quantity,  description):
        self.farmer_id = farmer_id
        self.product_name = product_name
        self.product_name = product_name
        self.unit_price = unit_price
        self.location = location        
        self.quantity = quantity
        self.description = description
        self.id = Product.generate_id()
        self.date_posted = str((__import__('datetime').datetime).now().date())

    @staticmethod
    def generate_id():
        while True:
            # generate number (2 digits, zero-padded) + 2 random uppercase letters
            gen_num = str(random.randint(0, 99)).zfill(2)
            gen_2letter = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            new_id = gen_num + gen_2letter

            # check if id already exists
            id_exist = Product.check_Product_exist(new_id)
            if not id_exist:  # unique id found
                return new_id

    @staticmethod
    def check_Product_exist(id):
        file_path = "data/products.json"

        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            # look if id exists
            existing_Product = next((f for f in data if f.get("id") == id), None)
            return existing_Product

        except FileNotFoundError:
            # Create empty file if not exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                json.dump([], f)
            return None

        except json.JSONDecodeError:
            print(f"Error: {file_path} contains invalid JSON.")
            return None

    def upload(self):
        # Validate inputs
        if not self.product_name.strip():
            print("❌ Error: Product name cannot be empty.")
            return False
        if not isinstance(self.unit_price, (int, float)) or self.unit_price <= 0:
            print("❌ Error: Unit price must be a positive number.")
            return False
        if not self.location.strip():
            print("❌ Error: Location cannot be empty.")
            return False
        if not isinstance(self.quantity, (int, float)) or self.quantity <= 0:
            print("❌ Error: Quantity must be a positive number.")
            return False
        if not self.description.strip():
            print("❌ Error: Description cannot be empty.")
            return False

        file_path = "data/products.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        try:
            with open(file_path, "r+") as file:
                data = json.load(file)

                # Check if product with same name by the same farmer exists
                if any(prod.get("product_name").lower() == self.product_name.lower() and prod.get("farmer_id") == self.farmer_id for prod in data):
                    print(f"❌ Error: Product '{self.product_name}' by this farmer already exists.")
                    return False

                new_product = {
                    "id": self.id,
                    "farmer_id": self.farmer_id,
                    "product_name": self.product_name.strip().title(),
                    "unit_price": self.unit_price,
                    "location": self.location.strip().title(),
                    "quantity": self.quantity,
                    "description": self.description.strip(),
                    "date_posted": self.date_posted
                }

                data.append(new_product)
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

            print(f"✅ Product '{self.product_name}' uploaded successfully with ID {self.id}.")
            return True

        except FileNotFoundError:
            with open(file_path, "w") as file:
                json.dump([], file)
            return self.upload()

        except json.JSONDecodeError as e:
            print(f"❌ Error: {file_path} contains invalid JSON: {e}")
            return False

    @staticmethod
    def get_all_products():
        file_path = "data/products.json"
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                return data if data else None
        except FileNotFoundError:
            print("❌ Error: No products found.")
            return None
        except json.JSONDecodeError:
            print(f"❌ Error: {file_path} contains invalid JSON.")
            return None
    
    @staticmethod
    def get_products_by_farmer(farmer_id):
        file_path = "data/products.json"
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                farmer_products = [prod for prod in data if prod.get("farmer_id") == farmer_id]
                return farmer_products if farmer_products else None
        except FileNotFoundError:
            print("❌ Error: No products found.")
            return None
        except json.JSONDecodeError:
            print(f"❌ Error: {file_path} contains invalid JSON.")
            return None
    
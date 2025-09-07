import json
import random, string
import os

class User:
    def __init__(self, name, phone, location, usertype):
        self.name = name
        self.phone = phone
        self.location = location
        self.usertype = usertype
        self.pin = User.generate_pin(usertype)

    @staticmethod
    def generate_pin(usertype):
        while True:
            # generate number (2 digits, zero-padded) + 2 random uppercase letters
            gen_num = str(random.randint(0, 99)).zfill(2)
            gen_2letter = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            new_pin = gen_num + gen_2letter

            # check if pin already exists
            pin_exist = User.check_user_exist(new_pin, usertype)
            if not pin_exist:  # unique pin found
                return new_pin

    @staticmethod
    def check_user_exist(pin, usertype):
        if usertype == "farmer":
            file_path = "data/farmer.json"
        else:
            file_path = "data/buyer.json"

        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            # look if pin exists
            existing_user = next((f for f in data if f.get("pin") == pin), None)
            return existing_user

        except FileNotFoundError:
            # Create empty file if not exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                json.dump([], f)
            return None

        except json.JSONDecodeError:
            print(f"Error: {file_path} contains invalid JSON.")
            return None

    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Phone: {self.phone}')
        print(f'Location: {self.location}')
        print(f'Pin: {self.pin}')

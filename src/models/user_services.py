from models.farmer import Farmer
from models.buyer import Buyer

import json
import os

class UserService:
   
    @staticmethod
    def login(phone, pin, usertype):
        farmers = load_farmer_data()
        buyers = load_buyer_data()
        records = None
        if usertype == "farmer":
            # first checking farmers records
            for f in farmers:
                if f["phone"] == phone and f["pin"] == pin:
                    # return f
                    records = f
        elif usertype == "buyer":
            # now check buyers record
            for f in buyers:
                if f["phone"] == phone and f["pin"] == pin:
                    records = f
                    
        if records == None:
            print("No record found, check no. or pin")
        else:
            return records
    

   # update profile
    @staticmethod
    def update_profile(phone, updates: dict, usertype: str):
        """
        Update user profile fields for farmer or buyer.
        """
        if usertype == "farmer":
            file_path = "data/farmer.json"
        elif usertype == "buyer":
            file_path = "data/buyer.json"
        else:
            return "❌ Invalid user type."

        try:
            with open(file_path, "r+") as file:
                data = json.load(file)
                user = next((u for u in data if u.get("phone") == phone), None)
                if not user:
                    return "❌ User not found."

                for key, value in updates.items():
                    if key in user:
                        user[key] = value

                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                return "✅ Profile updated successfully."
        except FileNotFoundError:
            return "❌ User data file not found."
        except json.JSONDecodeError:
            return "❌ User data file is corrupted."

   



# Loading farmer data functions
farmer_data = "data/farmer.json"

def load_farmer_data():
    if not os.path.exists(farmer_data):
        return []
    with open(farmer_data, "r") as f:
        return json.load(f)

def save_farmer_data(data):
    with open(farmer_data, "w") as f:
        json.dump(data, f, indent=4)


# Loading Buyer data functions
buyer_data = "data/buyer.json"

def load_buyer_data():
    if not os.path.exists(buyer_data):
        return []
    with open(buyer_data, "r") as f:
        return json.load(f)

def save_buyer_data(data):
    with open(buyer_data, "w") as f:
        json.dump(data, f, indent=4)
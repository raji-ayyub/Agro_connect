import json
from .user import User
import os
class Buyer(User):
    def __init__ (self,name,phone, location,organisation_name):
        #calling the parent class user with usertype as User
        super().__init__(name,phone,location,"user")
        self.organisation_name=organisation_name
        

# function to display User details
    def display_info(self):
        super.display_info()
        print(f"organisation_name: {self.organisation_name}")
        print(f"Reg PIN: {self.pin}")

# function User Registration
    def registration(self):
        # checking Inputs for validations
        if not self.name.strip():
            print("❌ Error: Name cannot be empty.")
            return True
        if not self.phone.isdigit():
            print("❌ Error: Phone number must contain only digits.")
            return True
        if not self.location.strip():
            print("❌ Error: Location cannot be empty.")
            return True
        if not self.organisation_name.strip():
            print("❌ Error: organisation name cannot be empty.")
            return True
        
        file_path="data/Buyer.json"
        # make sure file exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([],file)
        # 
        try:
            with open(file_path, "r+") as file:
                data= json.load(file)
                # check if user with same phone number exist
                if any(user.get("phone")== self.phone for user in data):
                    print(f"❌Error: User with phone {self.phone} already exists.")
                    return True
                # get the User data in to dict
                new_user={
                    "name": self.name.strip().title(),
                    "phone": self.phone.strip(),
                    "location": self.location.strip().title(),
                    "pin": self.pin,
                    "organisation_name": self.organisation_name.strip().title(),
                }
                # add new User 
                data.append(new_user)
                # updating the file
                file.seek(0)
                json.dump(data,file,indent=4)
                file.truncate()
            print(f"✅ User {self.name} registered successfully with PIN {self.pin}.")
            print("Please keep your PIN save.. Thank you👌")
            # return False
        # except json.JSONDecodeError as e:
        #     print(f"❌Error: User.json contain invalid JSON: {e}")
        #     return True
        except Exception as e:
            print(f"❌Unexpected error: {e}")
            return True

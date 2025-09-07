import json
import user as User
import os
class Farmer(User) :
    def __init__ (self,name,phone, location,farm_size,major_crop):
        #calling the parent class user with usertype as farmer
        super().__init__(name,phone,location,"farmer")
        self.farm_size=farm_size
        self.major_crop=major_crop

# function to display farmer details
    def display_info(self):
        super.display_info()
        print(f"Farm_size: {self.farm_size}")
        print(f"Major Crop: {self.major_crop}")
        print(f"Reg PIN: {self.pin}")

# function Farmer Registration
    def registration(self):
        # checking Inputs for validations
        if not self.name.strip():
            print("❌ Error: Name cannot be empty.")
            return False
        if not self.phone.isdigit():
            print("❌ Error: Phone number must contain only digits.")
            return False
        if not self.location.strip():
            print("❌ Error: Location cannot be empty.")
            return False
        if not self.farm_size or not str(self.farm_size).isdigit():
            print("❌ Error: Farm size must be a number.")
            return False
        if not self.major_crop.strip():
            print("❌ Error: Major crop cannot be empty.")
            return False
        file_path="data/farmer.json"
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
                if any(farmer.get("phone")== self.phone for farmer in data):
                    print(f"❌Error: Farmer with phone {self.phone} already exists.")
                    return False
                # get the farmer data in to dict
                new_farmer={
                    "name": self.name.strip().title(),
                    "phone": self.phone.strip(),
                    "location": self.location.strip().title(),
                    "pin": self.pin,
                    "farm_size": self.farm_size,
                    "major_crop": self.major_crop.strip().title(),
                }
                # add new farmer 
                data.append(new_farmer)
                # updating the file
                file.seek(0)
                json.dump(data,file,indent=4)
                file.truncate()
            print(f"✅ Farmer {self.name} registered successfully with PIN {self.pin}.")
            print("Please keep your PIN save.. Thank you👌")
            return True
        except json.JSONDecodeError:
            print("❌Error: farmer.json contain invalid JSON")
            return False
        except Exception as e:
            print(f"❌Unexpected error: {e}")
            return False

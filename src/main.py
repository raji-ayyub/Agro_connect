from models.farmer import Farmer 
from models.buyer import Buyer

from models.user_services import UserService
from models.product import Product

import json


# goback=False
while True:
    print("__________________________________________")
    print(" ----- Welcome to Agro_Connect App ------ ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("")

# checking the input and redirect to correct flow

    while True:
        choice= input("Enter operation to perform: ")
        try:
            choice=int(choice)
            break
        except ValueError:
            print("⚠ Please enter a numeric number")
    # whlie loop end here

    while True:
        if choice==1:
            # registration
            print("__________________________________________")
            print(" ----- Registration interface ------ ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1. Farmer")
            print("2. Buyer")
            print("3. Exit")
            # option 3 should go back not exit, to be fixed later
            print("======================")
            # collecting usertype input
            while True:
                option=input("Enter choice (1/2): ")
                if int(option) not in (1,2,3):
                    print("Enter a valid option (1/2/3)")
                    continue
                try:
                    option= int(option)
                    break
                except ValueError:
                    print("Please enter a numeric number")  
                # whlie loop end here
                # goback=True
                # while True:
                # option for farmer registration
            if option==1:
                accounttype="farmer"
                name=input("Enter your fullname: ")
                location=input("Enter your Location(e.g Ibadan): ")
                phone=input("Enter your phone number: ")
                farm_size=input("Enter your farm size(e.g 4 acres): ")
                major_crop=input("Enter your primary crop(e.g casava, yam, maize): ")
                farmer=Farmer(name,phone,location,farm_size,major_crop)
                farmer.registration()
                continue
            # option for buyer registration
            elif option ==2:
                
                accounttype="buyer"
                name=input("Enter your fullname: ")
                location=input("Enter your Location(e.g Ibadan): ")
                phone=input("Enter your phone number: ")
                organisation_name=input("Enter Organisation Name: ")
                buyer=Buyer(name,phone,location, organisation_name)
                buyer.registration()
                continue
            # option for Go back
            elif option ==3:
                # goback=False
                break
            else:
                print("Invalid option")
                # continue
                # 
        # login flow
        elif choice==2:
            print("__________________________________________")
            print(" ----- Login interface ------ ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("1. Farmer")
            print("2. Buyer")
            usertype = input("Login as (1/2): ")
            phone = input("Phone: ")
            pin = input("PIN: ")
            if usertype == "1":
                usertype = "farmer"
                farmer_details = UserService.login(phone, pin, usertype)

                if farmer_details:
                    print(f"\n\n ")
                    print("__________________________________________")
                    print(f" --FARMER:--- Welcome {farmer_details['name']}! ------ ")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    while True:
                        print("\n1. View Profile\n2. Update Profile\n3. Upload Product\n4. View My Products\n5. View Market Prices\n6. Logout")
                        sub = input("Choose: ")
                        if sub == "1":
                            print(farmer_details)
                        elif sub == "2":
                            key = input("Field to update (name/location/farm_size/crops): ")
                            val = input("New value: ")
                            msg = UserService.update_profile(phone, {key: val}, usertype)
                            print(msg)
                        elif sub == "3":
                            product_name= input("Enter Product name(e.g Casava): ")
                            unit_price= float(input("Enter Unit price(e.g 2000): "))
                            location=input("Enter Product Location(e.g Ibadan): ")
                            quantity= int(input("Enter Quantity(e.g 50kg): "))
                            description=input("Enter Product Description: ")
                            farmer_id=farmer_details.get("phone")
                            product = Product(farmer_id, product_name, unit_price, location, quantity, description)
                            product.upload()
                        elif sub == "4":
                            products = Product.get_products_by_farmer(farmer_details.get("phone"))
                            if products:
                                for prod in products:
                                    print(prod)
                            else:
                                print("No products found.")
                            
                        elif sub == "5":
                            # View Market Prices from market_prices.json
                            print(f"\n\n--- The list of market prices in available locations ---\n")
                            try:
                                with open("data/market_price.json", "r") as file:
                                    prices = json.load(file)
                                    for item in prices:
                                        print(f"Crop: {item['product_name']}, Average Price: {item['unit_price']}, Location: {item['location']}")
                            except FileNotFoundError:
                                print("Market prices data not found.")
                        else:
                            break
            elif usertype == "2":
                usertype = "buyer"
                if buyer_details := UserService.login(phone, pin, usertype):
                    print(f"\n\n ")
                    print("__________________________________________")
                    print(f" --BUYER:--- Welcome {buyer_details['name']}! ------ ")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    while True:
                        print("\n1. View Profile\n2. Update Profile\n3. check available Products\n4. Logout")
                        sub = input("Choose: ")
                        if sub == "1":
                            print(buyer_details)
                        elif sub == "2":
                            key = input("Field to update (name/location/organisation_name): ")
                            val = input("New value: ")
                            msg = UserService.update_profile(phone, {key: val}, usertype)
                            print(msg)
                        elif sub == "3":
                             # View Market Prices from market_prices.json
                            print(f"\n\n--- The list of market prices in available locations ---\n")
                            try:
                                with open("data/market_price.json", "r") as file:
                                    prices = json.load(file)
                                    for item in prices:
                                        print(f"Crop: {item['product_name']}, Average Price: {item['unit_price']}, Location: {item['location']}")
                            except FileNotFoundError:
                                print("Market prices data not found.")
                            
                            
                        
                            
                        elif sub == "4":
                            # View Market Prices from market_prices.json
                            break
                        else:
                            break
            else:
                print("Invalid login!")
        # Exit
        elif choice==3:
            print("Exiting... Goodbye!")
            break
    print("__________________________________________")
    print("--- Thanks for using Agro_Connect App ---")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    break


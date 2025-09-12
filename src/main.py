from models.farmer import Farmer 
from models.buyer import Buyer

goback=False
# while goback==True:
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

# while True:
if choice==1:
    # registration
    print("======================")
    print("1. Farmer")
    print("2. Buyer")
    print("3. Go back")
    print("======================")
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
    goback=True
    while goback==True:
        if option==1:
            # option for farmer registration
            accounttype="farmer"
            name=input("Enter your fullname: ")
            location=input("Enter your Location(e.g Ibadan): ")
            phone=input("Enter your phone number: ")
            farm_size=input("Enter your farm size(e.g 4 acres): ")
            major_crop=input("Enter your primary crop(e.g casava, yam, maize): ")
            farmer=Farmer(name,phone,location,farm_size,major_crop)
            goback=farmer.registration()
        elif option ==2:
            # option for buyer registration
            accounttype="buyer"
            name=input("Enter your fullname: ")
            location=input("Enter your Location(e.g Ibadan): ")
            phone=input("Enter your phone number: ")
            organisation_name=input("Enter Organisation Name: ")
            buyer=Buyer(name,phone,location, organisation_name)
            goback=buyer.registration()
            goback=False
        elif option ==3:
            # option for Go back
            goback=False
        else:
            print("Invalid option")
            # continue
        # 
   
elif choice==2:
    print("no fuction yet!")
elif choice==3:
    print("no fuction yet!")

print("__________________________________________")
print("--- Thanks for using Agro_Connect App ---")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

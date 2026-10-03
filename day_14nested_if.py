age = int(input("Enter your age:"))
membership_card = input("Do you have a membership card? (yes/no): ")
if age >=18:
    if membership_card == "yes":
        print("Access granted to VIP lounge")
    elif membership_card == "no":
        print("Access granted to Standard area")
else:
    print("Access denied.")
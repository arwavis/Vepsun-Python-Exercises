user_name = {"aravind": "aravind123", "rajesh": "rajesh123", "ramesh": "ramesh123", "kiran": "kiran123"}
user_count = 0
password_count = 0

while user_count < 5:
    user = input("Enter a user Name:\n ")
    if user in user_name:
        while password_count < 5:
            password = input("Enter the password:\n")
            if password == user_name[user]:
                print("Login Successfully !!!")
                break

            else:
                print("Wrong password, try again")
                password_count += 1
                print(f"Attempt{password_count}")
        else:
            print("Account locked because of wrong password, Please try after an hour")
        break

    else:
        print("Wrong UserName, try again")
        user_count += 1
        print(f"Attempt{user_count}")
else:
    print("Account locked because of wrong userName, Please try after an hour")

import re
import json

def registartion(user_id):

    user_id += 1

    first_name = input("First name : ")
    last_name = input("Last name : ")
    email = input("Email : ")
    password = input("Password : ")
    confirm_password = input("Confirm password : ")
    mobile_phone = input("Mobile phone : ")


    list_data = {'user_id': user_id,'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password,
                 'mobile_phone': mobile_phone}

    # Name Validation
    if first_name.isdigit() or not first_name:
        print("\nyour name is invalid ,, please enter valid name")
        registartion(user_id)
    else:
        # Email Validation
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, email)):
            # Password Validation
            if password == confirm_password:
                # Phone Validation
                if re.match("^01[0125][0-9]{8}$", mobile_phone):
                    users_data = open("users_data.json", "a")
                    json.dump(list_data, users_data)
                    users_data.write("\n")
                    users_data.close()

            else:
                print("\nYour password is invalid ,, please enter valid password :")
                registartion(user_id)
        else:
            print("Invalid Email ,, please try again")
            registartion(user_id)
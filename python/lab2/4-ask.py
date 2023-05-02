def inf():
    name=input("Enter your name: ")
    if name.isnumeric():
        print("The name is not allowed to be integer!!!")
    elif name =="":
        print("The name is not allowed to be empty!!!")
    else:
        email=input("Enter your email: ")

        import re  
        def validate_email(email):  
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
                return True  
            return False  
  
        email = email  
        if validate_email(email):    
            print("Your name is:" ,name)
            print("Your email is:" ,email)
        else:  
            print("Invalid email address!!!!")  
    
inf()
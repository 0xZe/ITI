def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
   
print ("The reversed string is:",reverse(input("Enter the string: ")) )  
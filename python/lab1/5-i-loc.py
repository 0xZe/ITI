string = input("Enter the string: ")
   
char = "i" 

pos = None
for i in range(0, len(string)): 
    if string[i] == char: 
        pos = i + 1
    #list append
if pos == None: 
    print ("character is not available in string") 
else:  
    print ("Character {} is present at position {}".format(char, str(pos)))
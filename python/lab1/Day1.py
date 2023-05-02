""" 
Q1:
Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string

"""
string=input("Enter the string:")
vowels_num=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or 
      i=='I' or i=='O' or i=='U'):
            vowels_num=vowels_num+1
print("Num of vowels is:")
print(vowels_num)

################################################################################################

""" 
Q2:
Fill an array of 5 elements from the user, Sort it in descending
and ascending orders then display the output

"""

# creating an empty list
lst = []
 
# number of elements 
n = 5
 
# iterating till the range
for i in range(n):
    ele = input("ENTER A VALUE: ")
    # adding the element
    lst.append(ele) 

lst.sort()
print("Ascending list is ",lst)

lst.reverse()
print("Descending list is ",lst)

################################################################################################

""" 
Q3:
Write a program that prints the number of times the string 'iti' occurs in anystring

"""

string = input("Enter the string: ")
occurence = "iti"
num_occurence = string.count(occurence)
print(occurence, "occurs", num_occurence, "times")

################################################################################################

""" 
Q4:
Write a program that remove all vowels from the input word and generate a brief version of it

"""

string=input("Enter the string:  ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in string:
    if char not in vowels:
        result = result + char

print("After removing Vowels: ", result)

################################################################################################

""" 
Q5:
Write a program that prints the locations of "i" character in any string you added

"""

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

################################################################################################

""" 
Q6:
Write a program that generate a multiplication table from 1 to the number passed

"""

num = int(input("Enter number: "))
result = []
for i in range(1,num+1):
    ele = []
    for j in range(1 , i+1):
        ele.append(i*j)
    result.append(ele)
print(result)

################################################################################################

""" 
Q7:
Write a program that build a Mario pyramid

"""

rows = int(input("Enter number of rows: "))
i=0
while(i<=rows):
  print(" " * (rows - i) +"*" * i) 
  i+=1
  
################################################################################################











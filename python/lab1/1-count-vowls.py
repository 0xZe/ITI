string=input("Enter the string:")
vowels_num=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or 
      i=='I' or i=='O' or i=='U'):
            vowels_num=vowels_num+1
print("Num of vowels is:")
print(vowels_num)
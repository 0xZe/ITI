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

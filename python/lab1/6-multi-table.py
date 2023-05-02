num = int(input("Enter number: "))
result = []
for i in range(1,num+1):
    ele = []
    for j in range(1 , i+1):
        ele.append(i*j)
    result.append(ele)
print(result)



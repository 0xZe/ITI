count = 0
tot = 0.0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try :
        num1 = float(number)
    except:
        print('Invailed Input!!!')
        continue
    count = count+1
    tot = tot + num1

print ("Count of numbers is:" ,count)
print ("Total of numbers is:" ,tot)
print("Average of numbers is:" ,tot/count )
def fizzBuzz(number):
        # If the  number is divisible by 3 and 5, print 'FizzBuzz':
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        # Otherwise the number is divisible by only 3, print 'Fizz':
        elif number % 3 == 0:
            print('Fizz')
        # Otherwise the number is divisible by only 5, print 'Buzz':
        elif number % 5 == 0:
            print('Buzz')
        # Otherwise, print the number:
        else:
            print(number)


fizzBuzz(int(input("Enter the number: ")))
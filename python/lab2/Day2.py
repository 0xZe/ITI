""" 
Q1:
Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start

"""

def arr(start, length):
    id_arr = list(range(start, start+length))
    print(id_arr)

#start=input("Enter start:")
#length=input("Enter length:")

arr(int(input("Enter start: ")),int(input("Enter length: " )))

################################################################################################


""" 
Q2:
write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return "FizzBuzz"

"""

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

################################################################################################


""" 
Q3:
Write a function which has an input of a string from user then it
will return the same string reversed

"""

def reverse(str):   
    string = "".join(reversed(str)) # reversed() function inside the join() function  
    return string   
  
   
print ("The reversed string is:",reverse(input("Enter the string: ")) )  


################################################################################################

""" 
Q4:
Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not

"""

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

################################################################################################

""" 
Q5:
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu

"""

def longest_substring(string):
    longest = ''
    current = ''
    for character in string:
        if current == '' or character >= current[-1]:
            current += character
        else:
            current = character
        longest = max(current, longest, key=len)
    print("Longest substring in alphabetical order is:" ,longest)

longest_substring(input("Enter the string: "))


################################################################################################

""" 
Q6:
Write a program which repeatedly reads numbers until the user
enters “done”.
○ Once “done” is entered, print out the total, count, and
average of the numbers.
○ If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number

"""

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


################################################################################################

""" 
Q7:
Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of
which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word

"""


import random
# library that we use in order to choose
# on random words from a list of words
 
name = input("What is your name? ")
 
# Here the user is asked to enter the name first
 
print("Good Luck ! ", name)
print("=====================") 
 
words = [
         'hang',
         'man', 
         'ze' 
        ]

print ("Available words is: ", words) 

# Function will choose one random
# word from this list of words
word = random.choice(words)
 
print("=====================") 
print("Guess the characters")
 
# characters that user guess
guesses = ''
# number of allowed turns 
turns = 7
 
 
while turns > 0:
 
    # counts the number of times a user fails
    failed = 0
 
    # all characters from the input
    # word taking one at a time
    for char in word:
 
        # comparing that character with
        # the character in guesses
        if char in guesses:
            print(char)

 
        else:
            print("_")
 
            # for every failure 1 will be
            # incremented in failure
            failed += 1
 
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")
 
        # this print the correct word
        print("The word is: ", word)
        break
 
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    print()
    guess = input("guess a character: ")
 
    # every input character will be stored in guesses
    guesses += guess
 
    # check input with the character in word
    if guess not in word:
 
        turns -= 1
 
        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")
 
        # this will print the number of
        # turns left for the user
        print("You have", + turns, 'more guesses')
 
if turns == 0:
    print("You Loose")

################################################################################################
# Task 1:

# inp = int(input("Enter your number: "))

# if (inp % 2 == 0):
#     print(f'{inp} is even number')
# else:
#     print(f'{inp} is odd number')

# Task 2:

# inp = int(input("Enter your number: "))

# if inp > 0:
#     print(f'{inp} is positive number')
# elif inp < 0:
#     print(f'{inp} is negative number')
# else:
#     print("Zero")

# Task 3:
# Voting Eligibility
# Ask for the age
# If the age above or equal 18, they can vote otherwise not

# Age: 18
# Output: You're eligible to vote

# Age: 10
# Output: You're not eligible to vote

# inp = int(input("Enter your age: "))

# if inp >= 18:
#     print("You're eligible to vote")
# else:
#     print("You are not eligible to vote")

# Task 4:

# word = input("Enter a word: ")
# char = input("Enter a character: ")[0]

# if char in word:
#     print(f'The character {char} is inside of the {word}')
# else:
#     print(f'The character {char} is not inside of the {word}')

# Task 5:
# Ask a user for 2 integers
# Check which one is larger, if they're equal then print equal

# inp = int(input("Enter 1st number: "))
# inp1 = int(input("Enter 2nd number: "))

# if inp > inp1:
#     print(f'{inp} is larger than {inp1}')
# elif inp1 > inp:
#     print(f'{inp1} is larger than {inp}')
# else:
#     print("They're equal")

## Task 6:
# Ask for username(string) and password, if the username is equal to 'admin' and password is equal to 'admin123'
# print 'Welcome Admin' otherwise 'Error': unknown User or Incorrect Password'

# usr = input("Enter the username: ")
# psw = input("Enter the password: ")

# if usr == "admin" and psw == "admin123":
#     print("Welcome Admin!")
# else:
#     print("Unknown User or Incorrect Password")

## Task
# Take an integer input, and print everything in between

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     print(i)

# n = int(input("Number: "))

# for i in range(n + 1):
#     if i % 2 == 0:
#         print(i)
   
####                                                    WHILE LOOPs iterates untill the condition is met

# n = int(input("Number: "))

# counter = 0

# if n > 0:
#         while counter != n:
#             print(counter)
#             counter = counter + 1
# elif n < 0:
#     while counter != n:
#          print(counter)
#          counter = counter - 1



## TASK
# Save the above line as a variable
# Ask user for a character input
# Check if the character exists in the sentence
# If yes, print every single character until it finds the character
# If no, print 'No existing character inside of the string'

# Example:
# The weather is great today
# Input: e 
# Output: 
# T 
# h

# Input: a
# Output:
# T
# h
# e 

# w
# e

# Input: x
# Output: No existing character inside of the string

word = "The weather is great today"
inp = input("Enter a character: ")
found = False

if inp not in word:
    print("No existing character inside of the string")

else:
     for c in word:
         if c == inp:
              found == True
              break
         print(c)
    






















# word = "The weather is great today"

# inp = input("Enter the character: ")

# found = False
# for c in word:
#         if c == inp:
#             found = True
#             break
#             print(c)

# if not found:
#      print("No existing character inside of the string")
     



    # else:
    #     print("No existing character inside of the string")
# word = "The weather is great today"

# c = input("Enter character: ")

# for c in word:
#     print(c)

# word = input("Enter a word: ")

# for c in word:
#     if c in "abcd":  
#         print(f'Letters were found: {c}')



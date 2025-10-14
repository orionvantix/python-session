# What is the strings?
# - Text Data Type --> '' or ""
# - Multiline Text --> """""" or ''''''

# word = "Hello"
# word2 = " World"

# print(word + word2)
# pring(f"Hello, {word) {word2}. Hope you are doing well")

# STRINGS have indexing system that starts with 0

# greeting = "Good Morning"
# print(greeting[0:4])
# print(greeting[::-1])

## Task
# sentence = "Hey august batch, our sessions will be on Saturday 10 PM"

## Print the following
## Hey 
## 10 PM
## batch

# print(sentence[0:3])
# print(sentence[11:16])
# print(sentence[-5::])

## Task
## Take 2 integer inputs
## Print which integer is larger

## Example
## num1 = 10 
## num2 = 20
## Output: 20 is larger that 10


## num1 = 30
## num2 = 20

## Output: 30 is larger that 20

## num: 10
## num: 10
## Output: 10 is equal to 10

# num1 = 10
# num2 = 20
# num3 = 30

# num1 = int(input("Enter your number: "))
# num2 = int(input("Enter your second number: "))


# if (num2 > num1):
#     print(f"{num2} is larger than {num1}")
# elif (num1 > num2):
#     print(f"{num1} is larger than {num2}")
# elif (num1 == num1):
#     print(f"{num2} is equal to {num1}")


## Task 2: 
## num1: 6
## divisible_by: 2
## Output: 6 is a positive number and it's divisible by 2

## num1: -5
## divisible_by: 5
## Output: -5 is a negative number and it's divisible by 5

## num1: -10
## divisible_by: 3
## Output: -10 is a negative number and it's not by 3

## Hints:
## combine 2 condtions together


# num1 = int(input("Enter your number:"))
# num2 = int(input("Divisible_by: "))

# if num1 % num2 == 0 and num1 > 0:
#     print(f'{num1} is a positive number and it is divisible by {num2}')
# elif num1 % num2 == 0 and num1 < 0:
#     print(f'{num1} is a negative number and it is divisible by {num2}')
# # elif num1 % 3 == 0 and num1 < 0:
# #     print(f'{num1} is a negative number and it is divisible by 3')
# else:
#     print(f'{num1} is not divisible by {num2}')

    

# word = "Hello, this is the word and can you tell me how many characters are now?"
# print(len(word))

## Task 3: Take an input of the string
## check if the length of the string is larger than 15
## if larger than 15: print ("Text is too big")
## else: print the word

## Example:
## Input: Hello
## Output: Hello

## Input: Hello, this is the august batch
## Output: Text is too big

# word = input("Enter the word: ")

## print(word)
# if len(word) > 15: 
#     print("Text is too big")
# else: 
#     print(word)
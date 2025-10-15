# Task 1: Number info
# Description:
#  Ask the user to enter a number. Your program should:
#       1. Check if the number is positive, negative, or zero
#       2. Check if the number is even or odd
#       3. Print both results
# Example:
# Input: -11  
# Output:
# The number is negative  
# The number is odd



# inp = int(input("Enter a number: "))

# # if inp > 0 and inp % 2 == 0:
# #     print(f'{inp} is positive and even')
# # elif inp > 0 and inp % 2 != 0:
# #     print(f'{inp} is positive and odd')
# # elif inp < 0 and inp % 2 == 0:
# #     print(f'{inp} is negative and even')
# # elif inp < 0 and inp % 2 != 0:
# #     print(f'{inp} is negative and odd')



# if inp > 0:
#     sign = "positive"
# elif inp < 0:
#     sign = "negative"
# else:
#     sign = "zero"

# if inp % 2 == 0:
#     even_odd = "even"
# else:
#     even_odd = "odd"

# if inp == 0:
#     print("The number is zero")
# else:
#     print(f'The number is {sign} and {even_odd}')


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Task 2: Final Decision
# Description:
#  Take two boolean inputs from the user (True or False) and show the result of and, or, and not operations.

# Example:
# Input:
# First Boolean: True  
# Second Boolean: False  
# Output:
# True and False = False  
# True or False = True  
# not True = False

# first = input("First Boolean(True/False): ")
# second = input("Second Boolean(True/False): ")

# if first == "True":
#     first = True
# else:
#     first = False

# if second == "True":
#     second = True
# else:
#     second = False

# print(first, "and", second, "=", first and second)
# print(first, "or", second, "=", first or second)
# print("not", first, "=", not first)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Task 3: Password Validator
# Description:
#  Ask the user to input a password.
#  Check if it meets all of the following conditions:
#       - At least 8 characters long
#       - Contains the letter “@”
#       - Does not contain any spaces
# Print:
# "Strong password" if all conditions are met
# Otherwise, print "Weak password"

# Example:
# Input: hello@123  
# Output: Strong password

# pswd = input("Enter the password: ")

# if len(pswd) >= 8 and "@" in pswd and " " not in pswd:
#     print("Strong password")
# else:
#     print("Weak password")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Task 4: Rock, Paper, Scissors
# Description:
#  Ask for two players to each enter "rock", "paper" or "scissors".
#  Determine who wins:
#       - Rock beats scissors
#       - Scissors beats paper
#       - Paper beats rock
#       - If same → “It’s a tie”

# Example:
# Player 1: rock  
# Player 2: scissors  
# Output: Player 1 wins

# p1 = input("Player 1 :")
# p2 = input("Player 2 :")

# r = "rock"
# p = "paper"
# s = "scissors"

# if p1 == r and p2 == s:
#     print("Player 1 wins")
# elif p1 == r and p2 == p:
#     print("Player 2 wins")
# elif p1 == p and p2 == r:
#     print("Player 1 wins")
# elif p1 == p and p2 == s:
#     print("Player 2 wins")
# elif p1 == s and p2 == r:
#     print("Player 1 wins")
# elif p1 == s and p2 == p:
#     print("Player 1 wins")
# elif p1 == p2:
#     print("It's a tie")

# else:
#     print("Enter paper/rock/scissors please!")


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Task 5: Triangle Type Checker
# Description:
#  Ask the user for 3 side lengths and determine what type of triangle they form:
#       - Equilateral: all sides equal
#       - Isosceles: two sides equal
#       - Scalene: all sides different
#       - Not a triangle: if the sum of any two sides is not greater than the third

# Example:
# Input: 5, 5, 5  
# Output: Equilateral triangle

# a = int(input("Enter first length side of a triangle: "))
# b = int(input("Enter second length side of a triangle: "))
# c = int(input("Enter third length side of a triangle: "))

# if (a+b > c) and (a+c > b) and (b+c > a):
#     if a == b and b == c and a == c:
#         print("Equilateral triangle")
#     elif a == b or a == c or b == c:
#         print("Isosceles triangle")
#     else:
#         print("Scelene triangle")
# else:
#     print("Not a triangle")






















# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if (a+b > c) and (a+c > b) and (b+c > a):
#     if a == b == c:
#         print("Equilateral triangle")
#     elif a == b or a == c or b == c:
#         print("two sides equal")
#     else:
#         print("all sides different")

# else:
#     print("Not a triangle")
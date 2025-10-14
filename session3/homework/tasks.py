# Task1:

# n = int(input("Enter a number: "))

# while n >= 1:
#     print(n)
#     n -= 1

# for i in range(n, 0, -1):   ### range(start, stop, step)
    # print(i)

# --------------------------------------------------------------------------------------

# # Task2:
#  Reverse a Word using for loop (please don’t reverse a string using word[::-1])

# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP



# --> 1st WAY
# inp = input("Enter a word: ")
# reverse = ""

# for i in range(len(inp) - 1, -1, -1):
#     reverse = reverse + inp[i]

# print("Reversed word: ", reverse)



# ---> 2nd WAY
# word = input("Enter a word: ")

# reversed_word = ""

# for ch in word:
#     reversed_word = ch + reversed_word
    

# print("Reversed Word:", reversed_word)

# --------------------------------------------------------------------------------------

# Task 3: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# word = input("Enter a word: ")
# pyramid = ""

# for c in word:
#     pyramid = pyramid + c
#     print(pyramid)
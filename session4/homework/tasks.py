# """
# ## Task 1: Reverse a List
# ## Write a program that reverses a list using a for loop.
# ## Example:

# ## Input:
# ## Enter numbers separated by space: 1 2 3 4 5
# ## Output:
# ## Reversed List: [5, 4, 3, 2, 1] 
# """


# inp = input("Enter numbers seperated by space: ").split()
# inp = [int(n) for n in inp]

# rev_lst = []
# for n in range(len(inp)-1, -1, -1):
#     rev_lst.append(inp[n])

# print(rev_lst)



# ----------------------------------------------------------------------------------------------------------------------------------------------------

"""
# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.

# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']
# """
# word = input("Enter words: ").split()

# filt_lst = []
# for n in range(len(word)-1, -1, -1):
#     if word[n] not in filt_lst:
#         filt_lst.append(word[n])
    

# print(filt_lst)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

"""
# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.

# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  
"""

# word = input("Enter words: ").split()
# lngst_word = word[0]

# for w in word:
#     if len(w) > len(lngst_word):
#         lngst_word = w

# print(lngst_word)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

"""
# Task 4: Find the Second Largest Number in a List (No max() or sort())
# Ask the user to enter a list of numbers. Find and print the second largest number without using max() or sort().

# Example:
# Enter numbers: 10 45 78 23 89 56  
# Second largest number: 78
"""


# inp = (input("Enter numbers: ")).split()
# num = [int(n) for n in inp]


# lrgst = num[0]
# sec_lrgst = num[0]

# for i in num:
#     if i > lrgst:
#         lrgst = i

# for i in num:
#     if i != lrgst:
#         if i > sec_lrgst:
#             sec_lrgst = i
        

# print(sec_lrgst)
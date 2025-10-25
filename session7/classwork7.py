# what is the function? 

# functions is a code that was written already, we just need to call it
# each data type they have their own functions and each function has it's purpose


# Let's get the namigs straight

# Methods - are the built-in functions for specific object  (Objects: int, float, str, list, tuple, boolean, dict, set)
# Functions - are designed to not be dependent on a specific object (They are usually custom written)
# there is a difference in terms syntax as well

# Object
# variable == object_name.<method>
# keys_var = dict.keys()
# lst.append()
# char = string.upper()

# Function
# These functions are already written in the python itself.
# type()
# len()
# input()

# I can create my custom function called greet(), and I can call it from everywhere in my code
# I'll write the greet function once and distribute it

# Functions
# used to make the code readable and reusable

# Syntax 
# def <function name>():
    # <code>

# def greet():
#     # hardcoding 


# what is the parameter?
# parameter is the input for our function
# def <function name>(parameter1, parameter2, paratemeter3):
    # <code>

# def greet(name): #-- python figures out what kind of data type you're using. You can make it explicit as well
#     print(f'Hey {name}, how are you doing?') 
#     # return (f'Hey {name}, how are you doing?')


# def greet2(name): #-- python figures out what kind of data type you're using. You can make it explicit as well
#     return (f'Hey {name}, how are you doing?')

# what does the return keyword do? 
# return ---> returns the data type <object> back

# return should always be used in the function instead of print unless you need to print the data to terminal


# print() is function that returns the data type to terminal to make it visible
# BUT print() always returns None ---> NoneType

# a = greet("Esen")  # print
# b = greet2("Esen")  # return

# return does not print data to terminal to make it visible, you still to use print()


# check for even values that return list of even values


def is_even(not_sorted_list, param2, param3): # its a paramter. This usually does not get changed (value)
    even_list = []

    for i in not_sorted_list:
        if i % 2 == 0:
            even_list.append(i)

    return even_list





# lst = [1,2,3,4,5,6,7,93,32,4,53,636,322,23,41,1,34,65,2]
# even = is_even(lst) # This is called argument


# lst2 = [98,43,123,43,231,331,13,4,2,413,1,4,5345243,2,3424,2]
# even2 = is_even(lst2)


# # * --> data structures and algorithms 
# print(*even)
# print(even2)


# method vs function
# parameter vs argument

# input for the function is called parameter
#

# what this function will do?
# This will take 2 parameters, 1st --> list, 2nd --> will be the digit
# Purpose of the function is to find the digit and return it's index


# default values and order
# if digit is not provided look number 0

# def search(lst_num, digit=0):
#     for index in range(len(lst_num)):
#         if lst_num[index] == digit:
#             found = index
#             return found

#     return 'digit does not exist'



# lst = [1,2,3,4,5,6,7,93,32,5]
# print(search(digit=5, lst_num=lst)) 




# Let's rewrite this as a function

# Will have a single parameter of the word:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# PCEP 
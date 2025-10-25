# what is the functions? 
# -> Custom functions
# -> Takes paramaters (inputs for the function)
# -> It is used to organize the code and for reusability
# len(), input() ....
# -> difference between return, print and none keywords
# ---> return -> return the value (data type/object), but it's not printed to terminal. function should be always using return
# ---> print  -> prints the value to terminal. always returns None --> NoneType
# ---> None   -> None is NoneType. NoneType means nothing. It's not equivalent to any data type. (e.g. 0, "", False .....)


# difference between methods and functions?
# -> method ---> specific for data types (objects/instances)
# -> functions ---> they are customly created and does not depend on an object/data type


# difference between parameters and arguments?
# -> parameter --> it input name when you define the function (e.g. def custom_function(paramter1, parameter2))
# -> argument --> input/value when you call the function. it is provided outside of the function. (e.g. custom_function(argument1, argument2))











# Recursion
# Recursion is not widely used method. 
# It's when a function call itself creating a loop until it stops. Usually it's controlled by if-else condition


# What is the usage:
# It is faster compared to other operations like for loop | while loop | if statement
# It is used for the tasks that are repetitive

# find <file_name>: print the location for each file if the naming is matched


# create a function that creates a list until the number is 0
# parameter = 5
# output: [5,4,3,2,1]

# def minus_one(num):
#     if num == 0:  # break point
#         print(num)  
#     else:
#         print(num)
#         minus_one(num - 1)


# minus_one(3)
# num = 3 ---> if 3 == 0 --> False ---> else ---> print(3) ---> minus_one(3 - 1)
# num = 2 ---> if 2 == 0 --> False ---> else ---> print(2) ---> minus_one(2 - 1)
# num = 1 ---> if 1 == 0 --> False ---> else ---> print(1) ---> minus_one(1 - 1)
# num = 1 ---> if 0 == 0 --> True  ---> print(0) 


# factorial(5)
# 5 * 4 * 3 * 2 * 1 == 120
# factorial(3)
# 3 * 2 * 1 == 6

# def factorial(num):
#     if num == 1:
#         return num
#     else:
#         return num * factorial(num - 1)
    
# factorial(3)
# num = 3 ---> if 3 == 1 --> false ---> else ---> return 3 * 2 * 1

# factorial(2)
# num = 2 ---> if 2 == 1 --> false ---> else ---> return 2 * factorial(2-1) ---- factorial(1)

# factorial(1)
# num = 1 ---> if 1 == 1 --> true ---> return 1


# task using a recursive function:

# def minus_one(num):
#     if num == 0:  # break point
#         print(num)  
#     else:
#         print(num)
#         minus_one(num - 1)


# create a function plus_one
# stops when the number is reached:


# plus_one(4)

# output:
# 0
# 1
# 2
# 3
# 4

# def plus_one(num):
#     if num == 0:
#         print(0)
#     else:
#         plus_one(num - 1)
#         print(num)

# plus_one(10)

# def plus_one(num):
#     if num > 0:
#         plus_one(num - 1)
    
#     print(num)


# plus_one(3)

# print(len(19))

# try:
#     # <code where you think there might an error>
#     inp = int(input("Please provide a number: "))
#     print(inp)
# except BaseException:
#     # code to execute when the try block returns an error
#     print("Not correct input. please provide a number")


# when we handle our program with exception, the program does not stop when there is an error
# print("This is the last line")

# inp = int(input("Please provide a number: "))
# print(inp)


# try:
#     # <code where you think there might an error>
#     lst = [1,2,3]
#     print(lst[2])  # 3  # lookup error --> index error

#     num = 10
#     print(num) # 10    # value error if we remove the num variable

#     print(num / 1) # zero division error
#     # code to execute when the try block returns an error

# except NameError:
#     print("Check you variable names")
# finally:
#     print("This is the finally block")
    # the block that will run always. if the code fails. if the code succeeds, it will run


# Dictionary Lookup with Error HandlingCreate a dictionary with student names as keys and scores as values.
# Prompt the user to enter a student's name.
# Use try-except to handle cases where the entered name does not exist in the dictionary.


# ask for a student name 
# if the student exists, print --> Hey <student_name>, how are you doing?

# if not, print ("unfortunatelly, we don't have this student")


# students = [
#     "S001" : {"name": "Meder"},
#     "S002" : {"name": "Sunatullo"},
#     "S003" : {"name": "Nurik"}
# ]

# students = {
#     "Meder": {"a":"b"},
#     "Sunatullo": {"c":"d"},
#     "Nurik": {"e":"f"}
# }

# try:
#     name = input("Please provide a student name: ")
#     print(students[name])
# except KeyError:
#     print("Student does not exist")
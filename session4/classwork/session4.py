

# for i in range(1, 11):
#     if i == 5:
#         break  # it's a loop keyword that stops the loop
#     print(i)

# else:
#     print('Hey loop is finished')
#     # this block always gets executed when the loop fully finishes


# counter = 0 
# while counter != 10:
#     counter += 1

#     if counter == 5:
#         break
#     print(counter)
# else:
#     print('Hey loop is finished')

# Let's write a program that stops when is sees input character

# word = "this block always gets executed when the loop fully finishes"
# character = input("Please provice a character: ")

# for char in word:
#     if character == char:
#         break
#     else:
#         print(char, end='')

# print()

# for i in range(10):
#     for j in range(1,4):
#         if j == 3:
#             break
#         else:
#             print(j, end='')
#     print()
    
# print()


# range(10) # --> what is the start --> 0, 10, 1 by default
# print("This is just a sentence", end="\nThis is the end \n") # end='\n' --> new line sep=


# word = "this block always gets executed when the loop fully finishes"
# character = input("Please provice a character: ")

# for char in word:
#     if character == char:
#         break
#     else:
#         print(char, end='')

# print()

# sep --> seperator --> default value

# a = "Hello"
# b = "World"

# print(a, b, sep='\n')

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue # skips the iterator
#         print(i) # gets ignored

# # Functionality that needs to be done
# for i in range(10):
#     pass # --> filler

# if 5 != 10:
#     # I don't know what to do here
#     pass


# def testFunction():
#     # This will be developed later and I can still call my function
#     pass

# print(testFunction())



### ---       ---        ---          LISTS           ---         ---         ----

# a = ["Hello", "World", "Esen", "Batch"]
# print(a)

### Lists
### Lists always start with []
### As a best practice, Lists should contain only singular data type

# names = ["Hello", "Meder", "Sunatullo", "Esen", "Hey", "What"]
# lst_int = [1, 10, 40, 34, 12.4]
# # print(names)
# # print(lst_int)

# # word = "Hello"
# print(names[1::2])

### Mutable and Immutabel data type

### mutable data type --> data type that can change it's values
### immutable data type --> data type that cannot change it's values

### srtings - immutable

# word = "hello"
# word[0] = 'H'
# # print(word[0])

# # print(word.title())
# print(word)

# Book
# Contains texts --> string

### List 
### Mutable data type

# names = ["Esen", "Meder", "Sunatullo", "Nurik"]

# # append(), insert()

# # names.append("Bob")   --> only appends to the last 
# # names.append("Eric")

# names.insert(0, "Bob")
# # print(names)
# names.insert(3, "Eric")

# print(names)


### Task:
# print(lst_even)
# input: 10
#lst_number: [2,4,6,8,10]

# input: 6
# lst_number: [2,4,6]

# nums = []
# for i in range(1,11):
#     if i % 2 == 0:
#         nums.append(i)

# print(nums)



### pop(index), remove(value)

# names = ["Esen", "Meder", "Sunatullo", "Nurik", "Bob", "Eric", "Esen"]

# # names.pop()  # --> default index value is -1
# names.remove("Esen")

# print(names)




### Task: 
# Ask for an input of the name to remove from the list
# Remove the names provided by the input

names = ["Esen", "Meder", "Sunatullo", "Nurik", "Bob", "Eric", "Esen"]


# inp = input("Enter a name: ")

# # for name in names:      
# #     if name == inp:
# #         names.remove(name)
# # print(names)

# print(len(names))

# for index in range(len(names) - 1, -1, -1):  # ← backward loop
#     if names[index] == inp:
#         names.pop(index)

# print(names)

### names.sort()

# duplicate_lst = names
# duplicate_lst = names[::] 
# duplicate_lst = names.copy()


# duplicate_lst.pop()
# duplicate_lst.pop()

# print(id(duplicate_lst))
# print(id(names))



### List comprehesion

# input: 10
# lst_number: [2,4,6,8,10]

# create a list 
# for loop
    # if condition
    #     append(i)

    # list = [append_element for loop]

# inp = int(input("Input: "))
# lst_comprehension = [i for i in range(1,inp) if i % 2 == 0]

# print(lst_comprehension)


# Task:
# create a simple list comprehension of the cube values
# 3 = 27
# 4 = 64


inp = int(input("Input: "))
lst_compr = [i**3 for i in range(1,inp)]

print(lst_compr)
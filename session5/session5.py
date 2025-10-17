### Tuple
# List mutable data type
# Tuple is exactly workd like a list, BUT it's immutable

# tpl = (1,2,3,4)
# tpl2 = 1,

# print(type(tpl2)) 

# tpl = (1,2,3,4)
# tpl2 = (1,)

# # print(tpl[0:2])

# for i in tpl:
#     print(i)

### do you think we will have functions like append, insert, pop, remove...?

# tpl = 1,1,2,2,3,3,3,4,4,4,5
# print(tpl.count(1))
# print(tpl.index(4))

# tpl = 1,1,2,2,3,3,3,4,4,4,5
# print(tpl.count(1))
# print(tpl.index(4))

### What would be the use case for tuple?

# bob = ("Bob", "Doe", "20th of December", "Male", "666-555-4444") ## You can't remove and you can't add


### List in tuples 
# user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
# user_data[3].append(79.3)
# print(user_data)

# Answer: ('John', 'American', 1964, [77.0, 78.2, 77.5, 79.3])




### ---         ---    SETS     ---         --- -----------------------------------------------------
### What is the difference between set and list
### Set is a multiple | same as list
### Set can hold multiple data type | same as list
### Set sorts its values
### Set can hold only unique values

# st = {1,2,3,4,5,"Hello"}

# print(type(st))

# st = {1,1,1,1,1,1,1,2,3,4,5,5,"Hello", False}
# print(st)

### 0 --> False
### 1 --> True

# st = {True,1}
# print(st)

# st = {True, 54,45,1,1,1,1,1,1,1,2,3,4,5,5,"Hello", False}
# print(st)


### Dictionary
# Dictionary unlike lists, does not support indexing

### Dictionary is collection data type that holds key-value pairs. Mutable data type
### Dictionary can hold only unique keys
# dictionary = {"key":"value"}
# dictionary --> mutable data type


# info ={"name": "John", "lastname": "Doe", "age":"30", "city":"Chicago"}

# Starbucks
# info["company"]  ="Starbucks"

# # del info['age']
# info.pop('city')

# print(info)

# print the following text:
# Hey John Doe, I aslo live in Chicago

# print(f"Hey {info['name']} {info['lastname']}, I also live in {info['city']}")


# info ={"name": "John", "lastname": "Doe", "age":"30", "city":"Chicago"}
# usage of the dictionaries with for loop

# keys = ["name", "lastname", 'age', "city"]
# values = ["John", "Doe", "30", "Chicago"]
# for i in info.values(): ## we are iterating through the keys list 
#     print(i)

# for i in info.keys(): ## we are iterating through the keys list 
#     print(i)


# items = list of tuple that has only 2 values
# items = [("name", "John"), ("lastname", "Doe"),('age', '30'),('city', 'Chicago') ]
# for key,value in info.items(): ## we are iterating through the keys list 
#     print(key)
#     print(value)




# # Task 4: Rock, Paper, Scissors

# p1 = input("Player 1: ").lower()
# p2 = input("Player 2: ").lower()

# rules = {
#     "rock": "scissors",
#     "scissors": "paper",
#     "paper": "rock"
# }

# if p1 not in rules or p2 not in rules:
#     print("Enter rock, paper, or scissors only!")
# elif p1 == p2:
#     print("It's a tie!")
# elif rules[p1] == p2:
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")




company = {
    "name": "TechVision",
    "location": "Chicago",
    "founded": 2018,
    "departments": ["Engineering", "Marketing", "HR", "Sales"],
    "employees": {
        "E002": {
            "name": "Anna",
            "age": 25,
            "position": "Marketing Manager",
            "skills": ["SEO", "Content Creation", "Analytics"],
            "full_time": True
        },
        "E003": {
            "name": "James",
            "age": 29,
            "position": "HR Specialist",
            "skills": ["Recruiting", "Onboarding", "Communication"],
            "full_time": False
        },
        "E004": {
            "name": "Maria",
            "age": 31,
            "position": "Sales Executive",
            "skills": ["Negotiation", "CRM", "Lead Generation"],
            "full_time": True
        }
    },
    "projects": [
        {
            "id": "P001",
            "name": "Website Revamp",
            "status": "In Progress",
            "team": ["E001", "E002"]
        },
        {
            "id": "P002",
            "name": "Marketing Automation",
            "status": "Completed",
            "team": ["E002", "E004"]
        }
    ]
}

# Print the following values

# Name of the company                                             # print the names of the company
# All the departments                                             # print the list of the deparments 
# What title does Anna have?                                      # print the position for the employee  Anna
# Is James working full time?                                     # print value of the full time of the employee James
# What is the project related to marketing that we are doing?     # marketing automation

print(f'Company Name: {company["name"]}')

print(f'Departments: {company["departments"]}')

print(f'Anna Position: {company["employees"]["E002"]["position"]}')

print(f'Is James working Full-Time?: {company["employees"]["E003"]["full_time"]}')

for project in company["projects"]:
    if "Marketing" in project["name"]:
        print(f'Marketing Project: {project["name"]}')
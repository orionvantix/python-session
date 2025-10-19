data = {
    "company": "FutureTech",
    "location": {
        "city": "San Francisco",
        "country": "USA",
        "offices": [
            {"id": 1, "address": "123 Market St", "employees": 120},
            {"id": 2, "address": "42 Silicon Ave", "employees": 85},
            {"id": 3, "address": "77 Innovation Dr", "employees": 60}
        ]
    },
    "departments": [
        {
            "name": "Engineering",
            "budget": 500000,
            "teams": [
                {
                    "team_name": "Backend",
                    "lead": "E001",
                    "members": ["E001", "E002", "E003"],
                    "projects": [
                        {"id": "P101", "title": "API Upgrade", "status": "Completed"},
                        {"id": "P102", "title": "Microservice Migration", "status": "In Progress"}
                    ]
                },
                {
                    "team_name": "Frontend",
                    "lead": "E004",
                    "members": ["E004", "E005"],
                    "projects": [
                        {"id": "P103", "title": "Dashboard Redesign", "status": "Not Started"}
                    ]
                }
            ]
        },
        {
            "name": "Marketing",
            "budget": 200000,
            "teams": [
                {
                    "team_name": "Content",
                    "lead": "E006",
                    "members": ["E006", "E007", "E008"],
                    "projects": [
                        {"id": "P201", "title": "Blog Launch", "status": "Completed"},
                        {"id": "P202", "title": "Brand Awareness", "status": "In Progress"}
                    ]
                }
            ]
        }
    ],
    "employees": {
        "E002": {"name": "Alice", "role": "Backend Engineer", "age": 25, "location": 1},
        "E003": {"name": "Bob", "role": "DevOps Engineer", "age": 27, "location": 1},
        "E004": {"name": "Clara", "role": "Frontend Engineer", "age": 24, "location": 2},
        "E005": {"name": "David", "role": "Frontend Engineer", "age": 28, "location": 2},
        "E006": {"name": "Emma", "role": "Content Lead", "age": 30, "location": 3},
        "E007": {"name": "Fiona", "role": "Content Writer", "age": 26, "location": 3},
        "E008": {"name": "George", "role": "SEO Specialist", "age": 31, "location": 3}
    },
    "policies": {
        "remote_work": True,
        "vacation_days": 20,
        "bonus_eligibility": ["Engineering", "Marketing"]
    }
}


# HW Tasks
# take user input that will only contain: In progress, Completed, Not Started
# Print all of the projects with the user input including department

# Input: In Progress

# Output: 
# Engineering Department:
# Microservice Migration

# Marketing Department:
# Brand Awareness

# ---- 
# Input: Completed

# Output: 
# Engineering Department:
# API Upgrade

# Marketing Department:
# Blog Launch

# inp = input("In Progress / Completed / Not Started: ")
# valid = "n Progress / Completed / Not Started"

# if inp not in valid:
#     print("Print one of the options")
#     exit()

# for dep in data["departments"]:
#     for team in dep["teams"]:
#         for stats in team["projects"]:
#             if inp == stats["status"]:
#                 print(f'{dep["name"]} Department:\n{stats["title"]}\n')
    


# ------------------------------------------------------------------------------------


# Task: 2
# If you check the employees dictionary it has a key called location. 
# This is the office location that they've been assigned

# Print each employee and addresses of their assigned offices

# Output:
# Alice: 123 Market St, San Francisco, USA
# Bob: 123 Market St, San Francisco, USA
# Clara: 42 Silicon Ave, San Francisco, USA
# David: 42 Silicon Ave, San Francisco, USA
# Emma: 77 Innovation Dr, San Francisco, USA
# Fiona: 77 Innovation Dr, San Francisco, USA
# George: 77 Innovation Dr, San Francisco, USA

location = data["location"]

for office in location["offices"]:
    for key,value in data["employees"].items():
        if value["location"] == office["id"]:
            print(f'{value["name"]}: {office["address"]}, {location["city"]}, {location["country"]}')
   
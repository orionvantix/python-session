# What's Dictionary?
# - Collection of keys and values wrapped in a single variable
# - Collection
#     - Difference between other collection data types:
#         - Mutable
#         - Key-Value store
#         - Only takes unique keys
#         - Cannot be retrieved by indexing instead we should use keys
#         - functions:
#             how to add values to dicionary: var_name['new_key'] = 'new_value'
#             how to remove values: del var_name['key'], var_name.pop('key')


# d = {}

# d['test'] = "test_world"

# d['test2'] = "hello_world"

# d.pop('test')

# print(d)


# product_data = {
#     "store": "TechNova",
#     "location": {
#         "city": "San Francisco",
#         "country": "USA"
#     },
#     "products": [
#         {
#             "id": "P1001",
#             "name": "Wireless Mouse",
#             "brand": "LogiTech",
#             "price": 29.99,
#             "currency": "USD",
#             "stock": 134,
#             "specs": {
#                 "color": "Black",
#                 "connectivity": "Bluetooth",
#                 "battery_life": "12 months"
#             },
#             "ratings": {
#                 "average": 4.5,
#                 "count": 240
#             }
#         },
#         {
#             "id": "P1002",
#             "name": "Mechanical Keyboard",
#             "brand": "KeyChron",
#             "price": 79.99,
#             "currency": "USD",
#             "stock": 57,
#             "specs": {
#                 "color": "White",
#                 "switch_type": "Gateron Brown",
#                 "backlight": "RGB"
#             },
#             "ratings": {
#                 "average": 4.7,
#                 "count": 145
#             }
#         },
#         {
#             "id": "P1003",
#             "name": "Sony Wireless Noise-Canceling Headphones",
#             "brand": "Sony",
#             "price": 199.99,
#             "currency": "USD",
#             "stock": 23,
#             "specs": {
#                 "color": "Black",
#                 "connectivity": "Bluetooth",
#                 "noise_cancellation": "Active",
#                 "battery_life": "30 hours"
#             },
#             "ratings": {
#                 "average": 4.8,
#                 "count": 529
#             }
#         }
#     ]
# }

# --> Print the following:
# 







# print(f'{store["name"]} has following items available: {products[""]}')

# print(f'{product_data["store"]} has following items available:')

# for p in product_data["products"]:
#     print(p["name"])


# for r in product_data["products"]:
#         print(f'{r["name"]}: {r["ratings"]["average"]}')

        
        
# c = input("Color: ")
# available_count = 0 # purpose is to count how many products are available with this color

# for p in product_data["products"]:
#     if c in p["specs"]["color"]:
#         print(f'{p["name"]} by {p["brand"]}')
#         available_count += 1


# if available_count == 0:
#     print("Nothing available")


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


# Print the following
# - department name on which projects each team is working on


# Output:
# Engineering Department:
# Backend Team: API Upgrade, Microservice Migration
# Frontend: Dashboard Redesign

# Marketing Department:
# Content Team: Blog Lunch, Brand Awareness

# for dep in data["departments"]:
#     print(f'{dep["name"]} Department:')
#     for team in dep['teams']:
#         print(f'{team["team_name"]}: ', end="")
#         print(*[p["title"] for p in team["projects"]], sep=", ")
#         # for p in team["projects"]:
#         #     print(p["title"], end=" ")
#     print()


# sep, end
        # print(team["team_name"])
            # print(f'{team["team_name"]}: {team["projects"]["title"]}')
        


# nums = [1,2,3]
# print(*nums)




# Task2:
# Print the following:
# <team_name> team is led by <name of the person> (<role>)

# Output:
# Backend team is led by Alice (Backend Engineer)
# Frontend team is led by Clara (Frontend Engineer)
# Content team is led by Emma (Content Lead)

for dep in data["departments"]:
    for team in dep['teams']:
        for key,value in data["employees"].items():
            if team["team_name"] in value["role"]:
                print(f'{team["team_name"]} team is lead by {value["name"]} ({value["role"]})')



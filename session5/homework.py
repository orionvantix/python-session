
# Task 1: Print this following message by getting values from the dictionary
# Message: Company TechNova is located in San Francisco, USA.

# my_dict = {
#     'company': 'TechNova', 
#     'city': 'San Francisco', 
#     'country': 'USA'
#     }


#           # print("Company", my_dict["company"], " is located in ", my_dict["city"],",", my_dict["country"])
# print(f'Company {my_dict["company"]} is located in {my_dict["city"]}, {my_dict["country"]}')

# ----------------------------------------------------------------------------------------------------------------------------


# Task 2: Print All Out-of-Stock Products
# Use the product_data dictionary and print the names of products that are out of stock (i.e., stock is 0).
# Example Output:
#  Out of stock: Bluetooth Speaker
#  Out of stock: Wireless Charger

# product_data = {
#     'Bluethooth Speaker': 0,
#     'Wireless Charger': 0,
#     'Headphone': 23,
#     'Mouse': 34
#     }

# for key,value in product_data.items():
#     # print(avail)
#     if value == 0:
#         print(f'Out of stock: {key}')


# ----------------------------------------------------------------------------------------------------------------------------



# Task 3: List Products Over $50 with High Rating
# Print the name, price, and average rating of products where
# - the price is greater than $50
# - the average rating is above 4.5.

# Example Output:
#  Mechanical Keyboard - $79.99 - Rating: 4.7
#  Noise-Canceling Headphones - $199.99 - Rating: 4.8

product_lst = {
    'p1': {
        'name': 'Headphones',
        'price': '$125.99',
        'av_rating': '4.5'
    },
    'p2': {
        'name': 'Mechanical Keyboard',
        'price': '$79.99',
        'av_rating': '4.7'
    }, 
    'p3': {
        'name': 'Noise-Cancelling Headphones',
        'price': '$199.99',
        'av_rating': '4.8'
    },
    'p4': {
        'name': 'Wireless Mouse',
        'price': '$59.99',
        'av_rating': '4.3'
    },  
    'p5': {
        'name': 'Laptop Stand',
        'price': '$49.99',
        'av_rating': '4.4'
    }, 
    'p6': {
        'name': 'Wireless Speaker',
        'price': '$29.99',
        'av_rating': '4.9'
    }
}

for key,value in product_lst.items():
    price = float(value["price"].replace("$", ""))
    rating = float(value["av_rating"])
    if price > 50 and rating > 4.5:
        print(f'{value["name"]} - {value["price"]} - Rating: {value["av_rating"]}')
    
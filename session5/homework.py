
# Task 1: Print this following message by getting values from the dictionary
# Message: Company TechNova is located in San Francisco, USA.

my_dict = {
    'company': 'TechNova', 
    'city': 'San Francisco', 
    'country': 'USA'
    }
for 

#           # print("Company", my_dict["company"], " is located in ", my_dict["city"],",", my_dict["country"])
# print(f'Company {my_dict["company"]} is located in {my_dict["city"]}, {my_dict["country"]}')

# ----------------------------------------------------------------------------------------------------------------------------


# Task 2: Print All Out-of-Stock Products
# Use the product_data dictionary and print the names of products that are out of stock (i.e., stock is 0).
# Example Output:
#  Out of stock: Bluetooth Speaker
#  Out of stock: Wireless Charger

product_data = {'product': 'Bluethooth Speaker','product': 'Wireless Charger'}
print(f'Out of stock: {product_data["product"]}')


# ----------------------------------------------------------------------------------------------------------------------------



# Task 3: List Products Over $50 with High Rating
# Print the name, price, and average rating of products where the price is greater than $50 and the average rating is above 4.5.
# Example Output:
#  Mechanical Keyboard - $79.99 - Rating: 4.7
#  Noise-Canceling Headphones - $199.99 - Rating: 4.8
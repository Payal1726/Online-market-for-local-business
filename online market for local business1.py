#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# In[1]:


# Get product details from the user
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter quantity: "))

# Calculate order total
order_total = product_price * product_quantity

# Print order details
print("\nOrder Details:")
print("--------------")
print("Product:", product_name)
print("Price:", product_price)
print("Quantity:", product_quantity)
print("Total:", order_total)



# # Assignment 3

# In[2]:


# Get product details from the user
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter quantity: "))

# Calculate order total
order_total = product_price * product_quantity

# Print order details
print("\nOrder Details:")
print("--------------")
print("Product:", product_name)
print("Price:", product_price)
print("Quantity:", product_quantity)
print("Total:", order_total)

# Track sales
sales_value = float(input("\nEnter the sales value: "))

# Check if the sales value is greater than the order total
if sales_value > order_total:
    print("\nSales value exceeds order total.")
elif sales_value == order_total:
    print("\nSales value matches order total.")
else:
    print("\nSales value is less than order total.")

# Get user review
review = input("\nPlease provide a review of the product: ")

# Print the review
print("\nThank you for your review!")
print("Review:", review)


# # Assignment 4

# In[17]:


# Business information
shop_name = "Dream Mart"
tax_rate = 0.20  # 10% tax rate

# Product details
products = {
    "Laptop - HP": {"unit_price": 80000.0, "quantity_available": 10},
    "Laptop - Dell": {"unit_price": 75000.0, "quantity_available": 15},
    "Fan - Bajaj": {"unit_price": 5000.0, "quantity_available": 30},
    "Fan - Philips": {"unit_price": 4500.0, "quantity_available": 25},
    "Bulb - Syska": {"unit_price": 250.0, "quantity_available": 100},
    "Bulb - Philips": {"unit_price": 270.0, "quantity_available": 80},
    "Switch - Anchor": {"unit_price": 120.0, "quantity_available": 50},
    "Switch - Havells": {"unit_price": 110.0, "quantity_available": 60},
}

# Function to validate phone number
def validate_phone_number(phone_number):
    if len(phone_number) == 10 and phone_number.isdigit():
        return True
    return False

# Function to get review from customer
def get_review():
    review = input("\nPlease provide your review (optional): ")
    return review

# Customer information
customer_name = input("Enter your name: ")
mobile_number = input("Enter your mobile number (10 digits only): ")

# Validate phone number
while not validate_phone_number(mobile_number):
    print("Invalid phone number! Please enter a 10-digit number.")
    mobile_number = input("Enter your mobile number (10 digits only): ")

# Customer orders
order = {}

# Take order from user
for product_name in products.keys():
    quantity = int(input(f"How many {product_name}(s) do you want to order? "))
    order[product_name] = quantity

# Display customer information
print("\nCustomer Information:")
print(f"Name: {customer_name}")
print(f"Mobile Number: {mobile_number}\n")

# Display order details
total_bill = 0
bill_details = []

for product_name, order_quantity in order.items():
    if order_quantity > 0:
        unit_price = products[product_name]["unit_price"]
        quantity_available = products[product_name]["quantity_available"]
        if order_quantity <= quantity_available:
            subtotal = unit_price * order_quantity
            tax_amount = subtotal * tax_rate
            total_price = subtotal + tax_amount
            products[product_name]["quantity_available"] -= order_quantity
            bill_details.append((product_name, order_quantity, subtotal, tax_amount, total_price))
            total_bill += total_price

# Decorative elements for bill section
decor_line = "-" * 40
space = "\n"

# Print bill
if total_bill > 0:
    print(space)
    print(decor_line.center(40))
    print("***** Electro_Mart*****".center(40))
    print(decor_line.center(40))
    print(space)
    print("Item                     Quantity     Subtotal")
    print(decor_line.center(40))
    for item, quantity, subtotal, _, total_price in bill_details:
        print(f"{item.ljust(24)}{str(quantity).center(10)}₹{subtotal:.2f}".center(40))
    print(space)
    print(decor_line.center(40))
    print(f"Total Bill (including taxes): ₹{total_bill:.2f}".center(40))
    print(decor_line.center(40))
else:
    print("No items purchased. Total bill is ₹0.00".center(40))

# Take a review from the customer
review = get_review()
if review:
    print("Thank you for your review!")
else:
    print("No review provided. Thank you for shopping with us!")


# # Assignment 5

# In[1]:


# Business information
business_info = {
    "shop_name": "Dream Mart",
    "tax_rate": 0.20,  # 10% tax rate
}

# Product catalog using tuples
products = [
    ("Laptop - HP", 80000.0, 100),
    ("Laptop - Dell", 75000.0, 150),
    ("Fan - Bajaj", 5000.0, 130),
    ("Fan - Philips", 4500.0, 225),
    ("Bulb - Syska", 250.0, 1000),
    ("Bulb - Philips", 270.0, 280),
    ("Switch - Anchor", 120.0, 350),
    ("Switch - Havells", 110.0, 660),
]

# Function to validate phone number
def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to calculate order total
def calculate_order_total(order):
    total = 0
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  # Check if the product name matches
                total += product[1] * quantity  # Add price * quantity to the total
                break
    return total

# Function to process customer order
def process_order(order):
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  # Check if the product name matches
                if quantity > product[2]:  # Check if the quantity exceeds available stock
                    print(f"Sorry, {item} is out of stock.")
                    return
                break
    total = calculate_order_total(order)
    print(f"Total order amount: {total:.2f}")
    return total

# Function to get customer review and rating
def get_review_and_rating():
    review = input("Please provide your review: ")
    rating = int(input("Please provide your rating (1-5): "))
    return review, rating

# Sample usage
if __name__ == "__main__":
    customer_name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number (10 digits only): ")

    while not validate_phone_number(mobile_number):
        print("Invalid phone number! Please enter a 10-digit number.")
        mobile_number = input("Enter your mobile number (10 digits only): ")

    # Display product catalog
    print("\nProduct Catalog:")
    for i, (name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

    # Take order from user
    order = {}
    while True:
        choice = input("Enter the number of the product you want to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                item = products[choice - 1][0]
                quantity = int(input(f"How many {item}s do you want to order? "))
                order[item] = quantity
            else:
                print("Invalid choice. Please select a valid product.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process order
    if order:
        total_amount = process_order(order)
        if total_amount:
            # Get review and rating
            review, rating = get_review_and_rating()
            print("Thank you for your review and rating!")
    else:
        print("No items ordered. Thank you for visiting Dream Mart!")


# In[1]:


# Business information
business_info = {
    "shop_name": "Dreamstore",
    "tax_rate": 0.20,  # 10% tax rate
}

# Product catalog using tuples
products = [
    ("Laptop - HP", 80000.0, 100),
    ("Laptop - Dell", 75000.0, 150),
    ("Laptop - Lenovo", 70000.0, 120),  # New laptop brand
    ("Laptop - Asus", 85000.0, 80),     # New laptop brand
    ("AirPods - Apple", 12000.0, 200),  # New product: AirPods
    ("Bluetooth Earphones - Sony", 3000.0, 300),  # New product: Bluetooth earphones
    ("Alexa Echo Dot", 4000.0, 150),    # New product: Alexa Echo Dot
    ("Alexa Echo Show", 8000.0, 100),   # New product: Alexa Echo Show
    ("Smartwatch - Apple Watch Series 7", 40000.0, 80),  # New product: Apple Watch
    ("Smartwatch - Samsung Galaxy Watch 4", 35000.0, 100),  # New product: Samsung Watch
    ("Smartphone - iPhone 13 Pro", 99999.0, 50),  # New product: iPhone 13 Pro
    ("Smartphone - Samsung Galaxy S21", 89999.0, 70),  # New product: Samsung Galaxy S21
    ("Tablet - iPad Pro", 70000.0, 90),  # New product: iPad Pro
    ("Tablet - Samsung Galaxy Tab S8", 65000.0, 60),  # New product: Samsung Galaxy Tab S8
    ("Headphones - Bose QuietComfort 45", 35000.0, 120),  # New product: Bose Headphones
    ("Headphones - Sony WH-1000XM4", 30000.0, 150),  # New product: Sony Headphones
    ("Speaker - Sonos One", 20000.0, 80),  # New product: Sonos Speaker
    ("Speaker - JBL Flip 5", 10000.0, 200),  # New product: JBL Speaker
]

# Function to validate phone number
def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to calculate order total
def calculate_order_total(order):
    total = 0
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  # Check if the product name matches
                total += product[1] * quantity  # Add price * quantity to the total
                break
    return total

# Function to process customer order
def process_order(order):
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  # Check if the product name matches
                if quantity > product[2]:  # Check if the quantity exceeds available stock
                    print(f"Sorry, {item} is out of stock.")
                    return
                break
    total = calculate_order_total(order)
    print(f"Total order amount: {total:.2f}")
    return total

# Function to get customer review and rating
def get_review_and_rating():
    review = input("Please provide your review: ")
    rating = int(input("Please provide your rating (1-5): "))
    return review, rating

# Sample usage
if __name__ == "__main__":
    customer_name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number (10 digits only): ")

    while not validate_phone_number(mobile_number):
        print("Invalid phone number! Please enter a 10-digit number.")
        mobile_number = input("Enter your mobile number (10 digits only): ")

    # Display product catalog
    print("\nProduct Catalog:")
    for i, (name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

    # Take order from user
    order = {}
    while True:
        choice = input("Enter the number of the product you want to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                item = products[choice - 1][0]
                quantity = int(input(f"How many {item}s do you want to order? "))
                order[item] = quantity
            else:
                print("Invalid choice. Please select a valid product.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process order
    if order:
        total_amount = process_order(order)
        if total_amount:
            # Get review and rating
            review, rating = get_review_and_rating()
            print("Thank you for your review and rating!")
    else:
        print("No items ordered. Thank you for visiting ElectroMart!")


# In[ ]:


# Business information
business_info = {
    "shop_name": "Dreamstore",
    "tax_rate": 0.20,  # 10% tax rate
}

# Product catalog using tuples
products = [
    ("Laptop - HP", 80000.0, 100),
    ("Laptop - Dell", 75000.0, 150),
    ("Laptop - Lenovo", 70000.0, 120),  # New laptop brand
    ("Laptop - Asus", 85000.0, 80),     # New laptop brand
    ("AirPods - Apple", 12000.0, 200),  # New product: AirPods
    ("Bluetooth Earphones - Sony", 3000.0, 300),  # New product: Bluetooth earphones
    ("Alexa Echo Dot", 4000.0, 150),    # New product: Alexa Echo Dot
    ("Alexa Echo Show", 8000.0, 100),   # New product: Alexa Echo Show
    ("Smartwatch - Apple Watch Series 7", 40000.0, 80),  # New product: Apple Watch
    ("Smartwatch - Samsung Galaxy Watch 4", 35000.0, 100),  # New product: Samsung Watch
    ("Smartphone - iPhone 13 Pro", 99999.0, 50),  # New product: iPhone 13 Pro
    ("Smartphone - Samsung Galaxy S21", 89999.0, 70),  # New product: Samsung Galaxy S21
    ("Tablet - iPad Pro", 70000.0, 90),  # New product: iPad Pro
    ("Tablet - Samsung Galaxy Tab S8", 65000.0, 60),  # New product: Samsung Galaxy Tab S8
    ("Headphones - Bose QuietComfort 45", 35000.0, 120),  # New product: Bose Headphones
    ("Headphones - Sony WH-1000XM4", 30000.0, 150),  # New product: Sony Headphones
    ("Speaker - Sonos One", 20000.0, 80),  # New product: Sonos Speaker
    ("Speaker - JBL Flip 5", 10000.0, 200),  # New product: JBL Speaker
]

# Function to validate phone number
def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to calculate order total
def calculate_order_total(order):
    total = 0
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  # Check if the product name matches
                total += product[1] * quantity  # Add price * quantity to the total
                break
    return total

# Function to process customer order
def process_order(order):
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  # Check if the product name matches
                if quantity > product[2]:  # Check if the quantity exceeds available stock
                    print(f"Sorry, {item} is out of stock.")
                    return
                break
    total = calculate_order_total(order)
    print(f"Total order amount: {total:.2f}")
    return total

# Function to get customer review and rating
def get_review_and_rating():
    rating = int(input("Please provide your rating (1-5 stars): "))
    while rating < 1 or rating > 5:
        print("Invalid rating! Please provide a rating between 1 and 5.")
        rating = int(input("Please provide your rating (1-5 stars): "))
    review = input("Please provide your review: ")
    return review, rating

# Sample usage
if __name__ == "__main__":
    customer_name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number (10 digits only): ")

    while not validate_phone_number(mobile_number):
        print("Invalid phone number! Please enter a 10-digit number.")
        mobile_number = input("Enter your mobile number (10 digits only): ")

    # Display product catalog
    print("\nProduct Catalog:")
    for i, (name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

    # Take order from user
    order = {}
    while True:
        choice = input("Enter the number of the product you want to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                item = products[choice - 1][0]
                quantity = int(input(f"How many {item}s do you want to order? "))
                order[item] = quantity
            else:
                print("Invalid choice. Please select a valid product.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Process order
    if order:
        total_amount = process_order(order)
        if total_amount:
            # Get review and rating
            review, rating = get_review_and_rating()
            print("Thank you for your review and rating!")
    else:
        print("No items ordered. Thank you for visiting Dreamstore!")

        


# In[2]:


# Business information
business_info = {
    "shop_name": "Dreamstore",
    "tax_rate": 0.20,  # 10% tax rate
}

# Product catalog using tuples
products = [
    ("Laptop - HP", 80000.0, 100),
    ("Laptop - Dell", 75000.0, 150),
    ("Laptop - Lenovo", 70000.0, 120),  
    ("Laptop - Asus", 85000.0, 80),     
    ("AirPods - Apple", 12000.0, 200), 
    ("Bluetooth Earphones - Sony", 3000.0, 300), 
    ("Alexa Echo Dot", 4000.0, 150),    
    ("Alexa Echo Show", 8000.0, 100),   
    ("Smartwatch - Apple Watch Series 7", 40000.0, 80),  
    ("Smartwatch - Samsung Galaxy Watch 4", 35000.0, 100),  
    ("Smartphone - iPhone 13 Pro", 99999.0, 50),  
    ("Smartphone - Samsung Galaxy S21", 89999.0, 70),  
    ("Tablet - iPad Pro", 70000.0, 90), 
    ("Tablet - Samsung Galaxy Tab S8", 65000.0, 60),  
    ("Headphones - Bose QuietComfort 45", 35000.0, 120),  
    ("Headphones - Sony WH-1000XM4", 30000.0, 150),  
    ("Speaker - Sonos One", 20000.0, 80),  
    ("Speaker - JBL Flip 5", 10000.0, 200),  
]


def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to calculate order total
def calculate_order_total(order):
    total = 0
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  
                total += product[1] * quantity  
                break
    return total

# Function to process customer order
def process_order(order):
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  
                if quantity > product[2]:  
                    print(f"Sorry, {item} is out of stock.")
                    return
                break
    total = calculate_order_total(order)
    print(f"Total order amount: {total:.2f}")
    return total


def get_review_and_rating():
    rating = int(input("Please provide your rating (1-5 stars): "))
    while rating < 1 or rating > 5:
        print("Invalid rating! Please provide a rating between 1 and 5.")
        rating = int(input("Please provide your rating (1-5 stars): "))
    review = input("Please provide your review: ")
    return review, rating


def display_review_stars(rating):
    stars = '★' * rating + '☆' * (5 - rating)
    print("Rating:", stars)


if __name__ == "__main__":
    customer_name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number (10 digits only): ")

    while not validate_phone_number(mobile_number):
        print("Invalid phone number! Please enter a 10-digit number.")
        mobile_number = input("Enter your mobile number (10 digits only): ")


    print("\nProduct Catalog:")
    for i, (name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

   
    order = {}
    while True:
        choice = input("Enter the number of the product you want to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                item = products[choice - 1][0]
                quantity = int(input(f"How many {item}s do you want to order? "))
                order[item] = quantity
            else:
                print("Invalid choice. Please select a valid product.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    if order:
        total_amount = process_order(order)
        if total_amount:
           
            review, rating = get_review_and_rating()
            display_review_stars(rating)
            print("Thank you for your review and rating!")
    else:
        print("No items ordered. Thank you for visiting Dreamstore!")


# In[1]:


# Business information
business_info = {
    "shop_name": "Dreamstore",
    "tax_rate": 0.20,  # 10% tax rate
}

# Product catalog using tuples
products = [
    ("Laptop - HP", 80000.0, 100),
    ("Laptop - Dell", 75000.0, 150),
    ("Laptop - Lenovo", 70000.0, 120),  
    ("Laptop - Asus", 85000.0, 80),     
    ("AirPods - Apple", 12000.0, 200), 
    ("Bluetooth Earphones - Sony", 3000.0, 300), 
    ("Alexa Echo Dot", 4000.0, 150),    
    ("Alexa Echo Show", 8000.0, 100),   
    ("Smartwatch - Apple Watch Series 7", 40000.0, 80),  
    ("Smartwatch - Samsung Galaxy Watch 4", 35000.0, 100),  
    ("Smartphone - iPhone 13 Pro", 99999.0, 50),  
    ("Smartphone - Samsung Galaxy S21", 89999.0, 70),  
    ("Tablet - iPad Pro", 70000.0, 90), 
    ("Tablet - Samsung Galaxy Tab S8", 65000.0, 60),  
    ("Headphones - Bose QuietComfort 45", 35000.0, 120),  
    ("Headphones - Sony WH-1000XM4", 30000.0, 150),  
    ("Speaker - Sonos One", 20000.0, 80),  
    ("Speaker - JBL Flip 5", 10000.0, 200),  
]


def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to calculate order total
def calculate_order_total(order):
    total = 0
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  
                total += product[1] * quantity  
                break
    return total

# Function to process customer order
def process_order(order):
    for item, quantity in order.items():
        for product in products:
            if product[0] == item:  
                if quantity > product[2]:  
                    print(f"Sorry, {item} is out of stock.")
                    return
                break
    total = calculate_order_total(order)
    print(f"Total order amount: {total:.2f}")
    return total


def get_review_and_rating():
    rating = int(input("Please provide your rating (1-5 stars): "))
    while rating < 1 or rating > 5:
        print("Invalid rating! Please provide a rating between 1 and 5.")
        rating = int(input("Please provide your rating (1-5 stars): "))
    review = input("Please provide your review: ")
    return review, rating


def display_review_stars(rating):
    stars = '★' * rating + '☆' * (5 - rating)
    print("Rating:", stars)


if __name__ == "__main__":
    customer_name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number (10 digits only): ")
    email = input("Enter your email address: ")

    while not validate_phone_number(mobile_number):
        print("Invalid phone number! Please enter a 10-digit number.")
        mobile_number = input("Enter your mobile number (10 digits only): ")


    print("\nProduct Catalog:")
    for i, (name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

   
    order = {}
    while True:
        choice = input("Enter the number of the product you want to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                item = products[choice - 1][0]
                quantity = int(input(f"How many {item}s do you want to order? "))
                order[item] = quantity
            else:
                print("Invalid choice. Please select a valid product.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    if order:
        total_amount = process_order(order)
        if total_amount:
           
            review, rating = get_review_and_rating()
            display_review_stars(rating)
            print("Thank you for your review and rating!")
    else:
        print("No items ordered. Thank you for visiting Dreamstore!")


# In[ ]:


Enter your name: Payal
Enter your mobile number (10 digits only): 1234567890
Enter your email address: payal@gmail.com

Product Catalog:
1. Laptop - HP - ₹80000.0 (100 available)
2. Laptop - Dell - ₹75000.0 (150 available)
3. Laptop - Lenovo - ₹70000.0 (120 available)
4. Laptop - Asus - ₹85000.0 (80 available)
5. AirPods - Apple - ₹12000.0 (200 available)
6. Bluetooth Earphones - Sony - ₹3000.0 (300 available)
7. Alexa Echo Dot - ₹4000.0 (150 available)
8. Alexa Echo Show - ₹8000.0 (100 available)
9. Smartwatch - Apple Watch Series 7 - ₹40000.0 (80 available)
10. Smartwatch - Samsung Galaxy Watch 4 - ₹35000.0 (100 available)
11. Smartphone - iPhone 13 Pro - ₹99999.0 (50 available)
12. Smartphone - Samsung Galaxy S21 - ₹89999.0 (70 available)
13. Tablet - iPad Pro - ₹70000.0 (90 available)
14. Tablet - Samsung Galaxy Tab S8 - ₹65000.0 (60 available)
15. Headphones - Bose QuietComfort 45 - ₹35000.0 (120 available)
16. Headphones - Sony WH-1000XM4 - ₹30000.0 (150 available)
17. Speaker - Sonos One - ₹20000.0 (80 available)
18. Speaker - JBL Flip 5 - ₹10000.0 (200 available)
Enter the number of the product you want to order (0 to finish): 4
How many Laptop - Asuss do you want to order? 2
Enter the number of the product you want to order (0 to finish): 5
How many AirPods - Apples do you want to order? 1
Enter the number of the product you want to order (0 to finish): 0
Total order amount: 182000.00
Please provide your rating (1-5 stars): 4
Please provide your review: nice
Rating: ★★★★☆
Thank you for your review and rating!


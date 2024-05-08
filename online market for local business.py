#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="payal@123456789",
    database="marketplace",
    auth_plugin='mysql_native_password'
)

# Function to create user table
def create_user_table():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255), role ENUM('customer', 'seller'))")

# Function to create product table
def create_product_table():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2), stock INT)")

# Function to allow user signup
def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (customer/seller): ").lower()
    if role not in ('customer', 'seller'):
        print("Invalid role!")
        return
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    db.commit()
    print("User signed up successfully!")

# Function to allow user login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor = db.cursor()
    cursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        role = result[0]
        print(f"Welcome, {role}!")
        return role
    else:
        print("Invalid username or password")
        return None

# Function to fetch products from the database
def fetch_products():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

# Function to add a product to the database
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    cursor = db.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    db.commit()
    print("Product added successfully!")

# Function to delete product
def delete_product():
    view_product_catalog()
    product_id = int(input("Enter the ID of the product you want to delete: "))
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    db.commit()
    print("Product deleted successfully!")

# Function to update product details
def update_product():
    view_product_catalog()
    product_id = int(input("Enter the ID of the product you want to update: "))
    new_price = float(input("Enter the new price: "))
    new_stock = int(input("Enter the new stock: "))
    cursor = db.cursor()
    cursor.execute("UPDATE products SET price = %s, stock = %s WHERE id = %s", (new_price, new_stock, product_id))
    db.commit()
    print("Product details updated successfully!")

# Function to validate phone number
def validate_phone_number(phone_number):
    return len(phone_number) == 10 and phone_number.isdigit()

# Function to calculate order total
def calculate_order_total(order):
    total = 0
    for item, quantity in order.items():
        for product in fetch_products():
            if product[1] == item:  
                total += product[2] * quantity  
                break
    return total

# Function to process customer order
def process_order(order):
    total = 0
    for item, quantity in order.items():
        for product in fetch_products():
            if product[1] == item:  
                if quantity > product[3]:  
                    print(f"Sorry, {item} is out of stock.")
                    return 0
                total += product[2] * quantity  
                break
    return total

# Function to get review and rating
def get_review_and_rating():
    rating = int(input("Please provide your rating (1-5 stars): "))
    while rating < 1 or rating > 5:
        print("Invalid rating! Please provide a rating between 1 and 5.")
        rating = int(input("Please provide your rating (1-5 stars): "))
    review = input("Please provide your review: ")
    return review, rating

# Function to display review stars
def display_review_stars(rating):
    stars = '★' * rating + '☆' * (5 - rating)
    print("Rating:", stars)

# Function for customer mode
def customer_mode():
    customer_name = input("Enter your name: ")
    mobile_number = input("Enter your mobile number (10 digits only): ")
    email = input("Enter your email address: ")

    while not validate_phone_number(mobile_number):
        print("Invalid phone number! Please enter a 10-digit number.")
        mobile_number = input("Enter your mobile number (10 digits only): ")

    print("\nProduct Catalog:")
    products = fetch_products()
    for i, (id, name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

    order = {}
    while True:
        choice = input("Enter the number of the product you want to order (0 to finish): ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(products):
                item = products[choice - 1][1]
                quantity = int(input(f"How many {item}s do you want to order? "))
                if quantity <= products[choice - 1][3]:
                    order[item] = quantity
                else:
                    print(f"Sorry, {item} is out of stock.")
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
            generate_bill(order, total_amount)  # Call generate_bill() here
    else:
        print("No items ordered. Thank you for visiting Dreamstore!")

# Function for seller mode
def seller_mode():
    username = input("Enter seller username: ")
    password = input("Enter seller password: ")
    
    if username == "seller" and password == "password":
        print("Welcome, seller!")
        while True:
            print("\nSeller Menu:")
            print("1. Add Product")
            print("2. View Product Catalog")
            print("3. Delete Product")
            print("4. Update Product Details")
            print("5. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                add_product()
            elif choice == '2':
                view_product_catalog()
            elif choice == '3':
                delete_product()
            elif choice == '4':
                update_product()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password")

# Function to view product catalog
def view_product_catalog():
    print("\nProduct Catalog:")
    products = fetch_products()
    for i, (id, name, price, stock) in enumerate(products, start=1):
        print(f"{i}. {name} - ₹{price} ({stock} available)")

# Function to generate bill
def generate_bill(order, total_amount):
    print("\n************** Bill **************")
    print("Shop Name: Dreamstore")
    print("----------------------------------")
    print("Item\t\t\tPrice\t\tQuantity\tTotal")
    print("----------------------------------")
    for item, quantity in order.items():
        for product in fetch_products():
            if product[1] == item:
                item_price = product[2]
                total_item_price = item_price * quantity
                print(f"{item}\t\t{item_price:.2f}\t\t{quantity}\t\t{total_item_price:.2f}")
    print("----------------------------------")
    tax_amount = total_amount * 0.20  # Assuming fixed tax rate
    total_with_tax = total_amount + tax_amount
    print(f"Subtotal: \t\t\t\t{total_amount:.2f}")
    print(f"Tax (20%): \t\t\t{tax_amount:.2f}")
    print("----------------------------------")
    print(f"Total: \t\t\t\t{total_with_tax:.2f}")
    print("")

# Main function
def main():
    create_user_table()
    create_product_table()

    while True:
        mode = input("Enter 'customer' for customer mode, 'seller' for seller mode, 'signup' to signup, or 'exit' to quit: ")
        if mode.lower() == 'customer':
            customer_mode()
        elif mode.lower() == 'seller':
            seller_mode()
        elif mode.lower() == 'signup':
            signup()
        elif mode.lower() == 'exit':
            break
        else:
            print("Invalid mode. Please try again.")

if _name_ == "_main_":
    main()


# In[ ]:


import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abhi@123456789",
    database="marketplace",
    auth_plugin='mysql_native_password'
)

def create_user_table():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255), role ENUM('customer', 'seller'))")

def create_product_table():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2), stock INT)")

def create_review_table():
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS reviews (id INT AUTO_INCREMENT PRIMARY KEY, product_id INT, username VARCHAR(255), review TEXT, rating INT)")

def signup():
    username = new_username_entry.get()
    password = new_password_entry.get()
    role = role_var.get()
    if role not in ('customer', 'seller'):
        messagebox.showerror("Error", "Invalid role!")
        return
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    db.commit()
    messagebox.showinfo("Success", "User signed up successfully!")

def login():
    username = username_entry.get()
    password = password_entry.get()
    cursor = db.cursor()
    cursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        role = result[0]
        messagebox.showinfo("Welcome", f"Welcome, {role}!")
        if role == 'seller':
            seller_mode()
        elif role == 'customer':
            customer_mode()
    else:
        messagebox.showerror("Error", "Invalid username or password")

def seller_mode():
    seller_window = tk.Toplevel(root)
    seller_window.title("Seller Mode")

    def add_product():
        name = product_name_entry.get()
        price = float(product_price_entry.get())
        stock = int(product_stock_entry.get())
        cursor = db.cursor()
        cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
        db.commit()
        messagebox.showinfo("Success", "Product added successfully!")
        fetch_products()

    def view_product_catalog():
        product_catalog_window = tk.Toplevel(seller_window)
        product_catalog_window.title("Product Catalog")

        products_frame = tk.Frame(product_catalog_window)
        products_frame.pack(padx=10, pady=10)

        cursor = db.cursor()
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        for i, (id, name, price, stock) in enumerate(products, start=1):
            product_label = tk.Label(products_frame, text=f"{i}. {name} - ₹{price} ({stock} available)")
            product_label.pack(anchor="w")

    def delete_product():
        def delete():
            product_id = int(product_id_entry.get())
            cursor = db.cursor()
            cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
            db.commit()
            messagebox.showinfo("Success", "Product deleted successfully!")
            fetch_products()

        delete_product_window = tk.Toplevel(seller_window)
        delete_product_window.title("Delete Product")

        tk.Label(delete_product_window, text="Enter Product ID to delete:").pack()
        product_id_entry = tk.Entry(delete_product_window)
        product_id_entry.pack()
        tk.Button(delete_product_window, text="Delete", command=delete).pack()

    def update_product():
        def update():
            product_id = int(product_id_entry.get())
            new_price = float(new_price_entry.get())
            new_stock = int(new_stock_entry.get())
            cursor = db.cursor()
            cursor.execute("UPDATE products SET price = %s, stock = %s WHERE id = %s", (new_price, new_stock, product_id))
            db.commit()
            messagebox.showinfo("Success", "Product details updated successfully!")
            fetch_products()

        update_product_window = tk.Toplevel(seller_window)
        update_product_window.title("Update Product")

        tk.Label(update_product_window, text="Enter Product ID to update:").pack()
        product_id_entry = tk.Entry(update_product_window)
        product_id_entry.pack()

        tk.Label(update_product_window, text="Enter New Price:").pack()
        new_price_entry = tk.Entry(update_product_window)
        new_price_entry.pack()

        tk.Label(update_product_window, text="Enter New Stock:").pack()
        new_stock_entry = tk.Entry(update_product_window)
        new_stock_entry.pack()

        tk.Button(update_product_window, text="Update", command=update).pack()

    add_product_frame = tk.LabelFrame(seller_window, text="Add Product")
    add_product_frame.pack(padx=10, pady=10)

    product_name_label = tk.Label(add_product_frame, text="Product Name:")
    product_name_label.grid(row=0, column=0, sticky="w")
    product_name_entry = tk.Entry(add_product_frame)
    product_name_entry.grid(row=0, column=1)

    product_price_label = tk.Label(add_product_frame, text="Product Price:")
    product_price_label.grid(row=1, column=0, sticky="w")
    product_price_entry = tk.Entry(add_product_frame)
    product_price_entry.grid(row=1, column=1)

    product_stock_label = tk.Label(add_product_frame, text="Product Stock:")
    product_stock_label.grid(row=2, column=0, sticky="w")
    product_stock_entry = tk.Entry(add_product_frame)
    product_stock_entry.grid(row=2, column=1)

    add_product_button = tk.Button(add_product_frame, text="Add Product", command=add_product)
    add_product_button.grid(row=3, columnspan=2, pady=5)

    view_products_button = tk.Button(seller_window, text="View Product Catalog", command=view_product_catalog)
    view_products_button.pack(pady=10)

    delete_product_button = tk.Button(seller_window, text="Delete Product", command=delete_product)
    delete_product_button.pack(pady=5)

    update_product_button = tk.Button(seller_window, text="Update Product", command=update_product)
    update_product_button.pack(pady=5)

def customer_mode():
    customer_window = tk.Toplevel(root)
    customer_window.title("Customer Mode")

    def process_order():
        def generate_bill(order, total_amount):
            def submit_review():
                rating = rating_var.get()
                review_text = review_text_entry.get("1.0", tk.END)
                cursor = db.cursor()
                for item in order:
                    product_id, name, price, quantity = item
                    cursor.execute("INSERT INTO reviews (product_id, username, review, rating) VALUES (%s, %s, %s, %s)", (product_id, username_entry.get(), review_text, rating))
                    db.commit()
                messagebox.showinfo("Review Submitted", "Thank you for your review and rating!")
                bill_window.destroy()

            bill_window = tk.Toplevel(customer_window)
            bill_window.title("Bill and Review")

            bill_frame = tk.Frame(bill_window)
            bill_frame.pack(padx=10, pady=10)

            tk.Label(bill_frame, text="************** Bill **************").pack()
            tk.Label(bill_frame, text="Shop Name: Dreamstore").pack()
            tk.Label(bill_frame, text="----------------------------------").pack()
            tk.Label(bill_frame, text="Item\t\t\tPrice\t\tQuantity\tTotal").pack()
            tk.Label(bill_frame, text="----------------------------------").pack()

            for item in order:
                product_id, name, price, quantity = item
                total_item_price = price * quantity
                tk.Label(bill_frame, text=f"{name}\t\t{price:.2f}\t\t{quantity}\t\t{total_item_price:.2f}").pack()

            tk.Label(bill_frame, text="----------------------------------").pack()
            tax_amount = total_amount * 0.20  # Assuming fixed tax rate
            total_with_tax = total_amount + tax_amount
            tk.Label(bill_frame, text=f"Subtotal: \t\t\t\t{total_amount:.2f}").pack()
            tk.Label(bill_frame, text=f"Tax (20%): \t\t\t{tax_amount:.2f}").pack()
            tk.Label(bill_frame, text="----------------------------------").pack()
            tk.Label(bill_frame, text=f"Total: \t\t\t\t{total_with_tax:.2f}").pack()
            tk.Label(bill_frame, text="").pack()

            review_frame = tk.Frame(bill_window)
            review_frame.pack(padx=10, pady=10)

            ttk.Label(review_frame, text="Rate the product (1-5 stars):").grid(row=0, column=0, sticky="w")
            rating_var = tk.IntVar()
            rating_entry = ttk.Combobox(review_frame, width=5, textvariable=rating_var, values=[1, 2, 3, 4, 5])
            rating_entry.grid(row=0, column=1)
            rating_entry.current(0)

            ttk.Label(review_frame, text="Write your review:").grid(row=1, column=0, sticky="w")
            review_text_entry = tk.Text(review_frame, height=5, width=30)
            review_text_entry.grid(row=1, column=1)

            submit_button = ttk.Button(review_frame, text="Submit", command=submit_review)
            submit_button.grid(row=2, columnspan=2, pady=5)


        order = []
        for i, (id, name, price, stock) in enumerate(fetch_products(), start=1):
            product_quantity = product_quantity_entries[i - 1].get()
            if product_quantity:
                product_quantity = int(product_quantity)
                if product_quantity <= stock:
                    order.append((id, name, price, product_quantity))
                else:
                    messagebox.showerror("Error", f"Sorry, {name} is out of stock.")
                    return
        if order:
            total_amount = calculate_order_total(order)
            if total_amount:
                generate_bill(order, total_amount)

    products_frame = tk.Frame(customer_window)
    products_frame.pack(padx=10, pady=10)

    fetch_products()

    product_quantity_entries = []

    for i, (id, name, price, stock) in enumerate(fetch_products(), start=1):
        tk.Label(products_frame, text=f"{i}. {name} - ₹{price} ({stock} available)").grid(row=i, column=0, sticky="w")
        product_quantity_label = tk.Label(products_frame, text="Quantity:")
        product_quantity_label.grid(row=i, column=1)
        product_quantity_entry = tk.Entry(products_frame, width=5)
        product_quantity_entry.grid(row=i, column=2)
        product_quantity_entries.append(product_quantity_entry)

    process_order_button = tk.Button(customer_window, text="Process Order", command=process_order)
    process_order_button.pack(pady=10)

def fetch_products():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    return cursor.fetchall()

def calculate_order_total(order):
    total = 0
    for item in order:
        id, name, price, quantity = item
        total += price * quantity
    return total

root = tk.Tk()
root.title("Marketplace")
root.attributes('-fullscreen', True)  # Set fullscreen mode

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

login_frame = tk.LabelFrame(frame, text="Login")
login_frame.grid(row=0, column=0, padx=10, pady=10)

username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2, pady=5)

signup_frame = tk.LabelFrame(frame, text="Signup")
signup_frame.grid(row=0, column=1, padx=10, pady=10)

role_var = tk.StringVar()
role_var.set("customer")

role_label = tk.Label(signup_frame, text="Role:")
role_label.grid(row=0, column=0, sticky="w")
role_menu = tk.OptionMenu(signup_frame, role_var, "customer", "seller")
role_menu.grid(row=0, column=1)

new_username_label = tk.Label(signup_frame, text="Username:")
new_username_label.grid(row=1, column=0, sticky="w")
new_username_entry = tk.Entry(signup_frame)
new_username_entry.grid(row=1, column=1)

new_password_label = tk.Label(signup_frame, text="Password:")
new_password_label.grid(row=2, column=0, sticky="w")
new_password_entry = tk.Entry(signup_frame, show="*")
new_password_entry.grid(row=2, column=1)

signup_button = tk.Button(signup_frame, text="Signup", command=signup)
signup_button.grid(row=3, columnspan=2, pady=5)

root.mainloop()


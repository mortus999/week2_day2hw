# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".

restaurant_menu['Beverages'] = {"dr pepper": "1.00", "milk": "1.25"}
restaurant_menu["Main Course"]["Steak"]="17.99"
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

# 2. Python Programming Challenges for Customer Service Data Handling
#     Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(ticket_number, name, issue, status):
    if ticket_number not in service_tickets:
        service_tickets[ticket_number] = {"Customer": name, "Issue": issue, "Status": status}
    else:
        print("that ticket already exists")

    return "ticket succesfully Opened"
add_ticket("Ticket003", "Linda", "Dirty Hardrive", "open")

print(service_tickets)
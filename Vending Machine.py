import time
from collections import defaultdict

# Stock of Items 
inventory = {
    "b3": {  # Hot Drinks
        "Latte": {"code": "1A", "price": 6, "stock": 5},
        "Americano": {"code": "1B", "price": 5, "stock": 5},
        "Cappuccino": {"code": "1C", "price": 6, "stock": 5},
        "Green Tea": {"code": "1D", "price": 4, "stock": 5},
        "Raspberry Tea": {"code": "1E", "price": 4, "stock": 5},
        "Black Tea": {"code": "1F", "price": 3, "stock": 5},
    },
    "b2": {  # Cold Drinks
        "Coke": {"code": "2A", "price": 4, "stock": 5},
        "Sprite": {"code": "2B", "price": 4, "stock": 5},
        "Dr Pepper": {"code": "2C", "price": 4, "stock": 5},
        "Canada Dry": {"code": "2D", "price": 4, "stock": 5},
    },
    "b1": {  # Healthy Snacks
        "Nuts": {"code": "3A", "price": 3, "stock": 5},
        "Protein Bar": {"code": "3B", "price": 4, "stock": 5},
        "Chocolate Protein Bar": {"code": "3C", "price": 5, "stock": 5},
        "Nut Protein Bar": {"code": "3D", "price": 5, "stock": 5},
        "Nestle Protein Bar": {"code": "3E", "price": 5, "stock": 5},
        "Dried Berries Mix": {"code": "3F", "price": 4, "stock": 5},
        "Granola Bites": {"code": "3G", "price": 4, "stock": 5},
        "Rice Cakes": {"code": "3H", "price": 3, "stock": 5},
        "Oat Cookies": {"code": "3I", "price": 3, "stock": 5},
        "Fiber Bar": {"code": "3J", "price": 4, "stock": 5},
    },
    "b4": {  # Sweets
        "Biscuits": {"code": "4A", "price": 2, "stock": 5},
        "Chocolate": {"code": "4B", "price": 3, "stock": 5},
        "Hershey's": {"code": "4C", "price": 4, "stock": 5},
        "Dark Chocolate": {"code": "4D", "price": 4, "stock": 5},
        "Milk Chocolate": {"code": "4E", "price": 4, "stock": 5},
    },
    "b5": {  # Snacks
        "Oreos": {"code": "5A", "price": 3, "stock": 5},
        "Lays": {"code": "5B", "price": 3, "stock": 5},
        "Cheetos": {"code": "5C", "price": 3, "stock": 5},
        "Doritos": {"code": "5D", "price": 3, "stock": 5},
        "Cheeseballs": {"code": "5E", "price": 3, "stock": 5},
        "Oman Chips": {"code": "5F", "price": 3, "stock": 5},
        "Takis": {"code": "5G", "price": 3, "stock": 5},
        "Pringles": {"code": "5H", "price": 4, "stock": 5},
        "Bugles": {"code": "5I", "price": 3, "stock": 5},
        "Tortilla Chips": {"code": "5J", "price": 3, "stock": 5},
    },
    "b6": {  # Fresh Juices
        "Orange Juice": {"code": "6A", "price": 5, "stock": 5},
        "Apple Juice": {"code": "6B", "price": 5, "stock": 5},
        "Mango Juice": {"code": "6C", "price": 5, "stock": 5},
        "Pineapple Juice": {"code": "6D", "price": 5, "stock": 5},
        "Strawberry Juice": {"code": "6E", "price": 5, "stock": 5},
        "Watermelon Juice": {"code": "6F", "price": 5, "stock": 5},
        "Carrot Juice": {"code": "6G", "price": 5, "stock": 5},
        "Beetroot Juice": {"code": "6H", "price": 5, "stock": 5},
        "Lemon Mint Juice": {"code": "6I", "price": 5, "stock": 5},
        "Mixed Fruit Juice": {"code": "6J", "price": 6, "stock": 5},
    }
}

# Welcome and goodbye messages
welcome_message = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

░██████╗███╗░░██╗░█████╗░░█████╗░██╗░░██╗  ░██████╗██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔════╝████╗░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗██║░██╔╝
╚█████╗░██╔██╗██║███████║██║░░╚═╝█████═╝░  ╚█████╗░███████║███████║██║░░╚═╝█████═╝░
░╚═══██╗██║╚████║██╔══██║██║░░██╗██╔═██╗░  ░╚═══██╗██╔══██║██╔══██║██║░░██╗██╔═██╗░
██████╔╝██║░╚███║██║░░██║╚█████╔╝██║░╚██╗  ██████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""

goodbye_message = """
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  ░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

░██████╗██╗░░██╗░█████╗░██████╗░██████╗░██╗███╗░░██╗░██████╗░
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
╚█████╗░███████║██║░░██║██████╔╝██████╔╝██║██╔██╗██║██║░░██╗░
░╚═══██╗██╔══██║██║░░██║██╔═══╝░██╔═══╝░██║██║╚████║██║░░╚██╗
██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░░░░░██║██║░╚███║╚██████╔╝
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░

"""

# Global variables
cart = defaultdict(int)  # Tracks the item quantities
user_change = 0 #Default vlaue for thr change 
bottle_deposit_count = 0
sales_count = defaultdict(int)

# Category codes 
category_codes = {
    "B1": "b1",
    "B2": "b2",
    "B3": "b3",
    "B4": "b4",
    "B5": "b5",
    "B6": "b6"
}

#function defined and the mainmenu categories
def display_main_menu():
    print("\nWhat would you like today?")
    print("Healthy Snacks  code: B1")
    print("Cold Drinks    code: B2")
    print("Hot Drinks     code: B3")
    print("Sweets         code: B4")
    print("Snacks         code: B5")
    print("Fresh Juices   code: B6")

# Display items in a category
def display_category(category):
    print(f"\nItems in {category_codes[category.upper()].replace('b', 'Category ').title()}:")
    for item, data in inventory[category_codes[category.upper()]].items():  # Loops through each item in the selected category
        if data["stock"] > 0:
            print(f" - {item}: AED {data['price']} (Code: {data['code']})") # If in stock this shows the item name, price, and code of the item
        else:
            print(f" - {item}: Out of Stock (Code: {data['code']})")  # If out of stock this will show that it's unavailable but still display the code

#Enables user to find item by code (accepts input like '3b5' or '3B')
def find_item_by_code(code):
    code = code.upper().replace('B', 'B').replace('b', 'B')  # Normalize input
    for cat, items in inventory.items():
        for name, info in items.items():
            if info["code"] == code:
                return cat, name, info
    return None, None, None

# Suggests a complementary items
def suggest_item(category, item):
    suggestions = {
        "b3": ["Biscuits", "Chocolate"],  # Hot Drinks
        "b2": ["Lays", "Doritos"],       # Cold Drinks
        "b6": ["Nuts", "Protein Bar"],   # Fresh Juices
        "b1": ["Orange Juice"],          # Healthy Snacks
        "b4": ["Coke"],                  # Sweets
        "b5": ["Sprite"]                 # Snacks
    }
    if category in suggestions:  # Checks if the current category has suggestions
        print("\nSuggested items:")
        for suggestion in suggestions[category]:  # Suggests items that are NOT the one the user already picked
            for cat, items in inventory.items():
                if suggestion in items and items[suggestion]["stock"] > 0:
                    print(f" - {suggestion}: AED {items[suggestion]['price']} (Code: {items[suggestion]['code']})")
                    return suggestion
    return None

## Handles the payment process and calculates change
def process_payment(total):
    global user_change
    print(f"\nTotal: AED {total}")
    while True:
        try:
            paid = float(input("Insert money: AED "))
            if paid < total:
                print("Not enough money. Try again.")
            else:
                user_change = round(paid - total, 2)
                print(f"Change returned: AED {user_change}")
                break
        except ValueError:
            print("Invalid input. Enter a valid number.") # Handles the non numeric input instead of a error in code

# Deliver of items
def deliver_items():
    print("\nDispensing items...")
    time.sleep(1)  # Short delay to mimic real machine behavior this if for improving user exp
    for item, quantity in cart.items():
        print(f"{item} (x{quantity}) delivered.")
    print("Delivery complete. Thank you!")

# Recycling of  bottles
def recycle_bottle():
    global bottle_deposit_count  # Tracks the  total number of bottles recycled
    print("\nInsert empty glass bottle...")
    time.sleep(1)
    bottle_deposit_count += 1
    print(f"Bottle recycled. Total recycled: {bottle_deposit_count}")

# Provides access to admin  menu after verifying a secret code which is "AdminAccess123"
def admin_menu():
    secret_code = "AdminAccess123"  #Variable that stores the  admin access code
    code = input("\nEnter admin code: ")
    if code != secret_code:
        print("Invalid admin code!")
        return #Exit function if access is denied
    
    while True:
        print("\n=== Admin Menu ===")
        print("1. View Stock")
        print("2. Restock All Items")
        print("3. View Sales Report")
        print("4. Exit")
        choice = input("Select option: ")
        
        if choice == "1":
            for cat, items in inventory.items():  #Shows stock levels for each category and item
                print(f"\n{cat.replace('b', 'Category ').title()}:")
                for item, data in items.items():
                    print(f" - {item}: {data['stock']} in stock")
        
        elif choice == "2":
            for cat, items in inventory.items(): #Restock every item to full (5 items = full)
                for item in items:
                    inventory[cat][item]["stock"] = 5
            print("All items restocked.")
        
        elif choice == "3":
            print("\nSales Report:")
            if not sales_count:
                print("No sales recorded.")
            else:
                total_revenue = 0
                for item, count in sales_count.items():
                    for cat, items in inventory.items():
                        if item in items:
                            price = items[item]["price"]
                            total_revenue += price * count
                            print(f" - {item}: {count} sold (AED {price * count})") #Calculates the total rev over the previous orders to produce a report 
                print(f"Total Revenue: AED {total_revenue}")
        
        elif choice == "4":
            break
        else:
            print("Invalid option.")

#This function manages the item selection and purchasing process
def select_items():
    global user_change  # Refer to the global variable for tracking leftover change
    total = 0  #Initialize the total amount to be paid for selected items
    
    while True:  #Loop to allow the user to select multiple items/categories
        display_main_menu()  #Show the available categories
        action = input("\nEnter category code (B1-B6), 'recycle', 'admin', or 'exit': ").lower()  #Get user input
        
        if action == "exit": 
            return None, 0
        elif action == "recycle":  #User chooses to recycle bottles
            recycle_bottle()
            continue  #Restart the loop after recycling
        elif action == "admin":  #User accesses the admin panel
            admin_menu()
            continue  # Restart the loop after admin actions
        elif action.upper() not in category_codes:  #Invalid category code entered
            print("Invalid category code.")
            continue  #Ask for input again
        
        display_category(action.upper())  #Display items inside the selected category
        
        code = input("\nEnter item code (or 'back' to return): ").strip() 
        if code.lower() == "back":  #User decides to return to main menu
            continue
        
        cat, name, item = find_item_by_code(code)  #Find the item details based on the code provided
        
        if not item:  #If no matching item was found
            print("Invalid code.")
            continue
        if item["stock"] <= 0:  #Check if the selected item is available
            print(f"{name} is out of stock.")
            continue
        
        cart[name] += 1  #Add the item to the  cart
        item["stock"] -= 1  
        sales_count[name] += 1  #Record the sale
        total += item["price"]  
        print(f"{name} added to cart. Current total: AED {total}")
        
        suggested = suggest_item(cat, name)  #Suggest a related item for upselling
        if suggested:
            add = input(f"Add {suggested}? (y/n): ").lower()  #Ask if user wants the suggested item
            if add == "y":
                for c, items in inventory.items():  # Search through all categories to find the suggested item
                    if suggested in items and items[suggested]["stock"] > 0:
                        cart[suggested] += 1  
                        items[suggested]["stock"] -= 1  
                        sales_count[suggested] += 1  
                        total += items[suggested]["price"]  
                        print(f"{suggested} added. Current total: AED {total}")
                        break  #Stop searching after adding the suggested item
        
        more = input("Add another item? (y/n): ").lower()  #Ask if user wants to add more items
        if more != "y":
            break  #Exit item selection if user is done
    
    return cart, total  #Return the filled cart and the total amount to be paid


#This is the main driver function that manages the overall program flow
def main():
    global user_change  #Access the global variable tracking leftover change
    print(welcome_message)  #Display a welcome message 
    
    while True:  #Main loop to handle multiple purchase sessions
        cart.clear()  #Clear the cart before starting a new session
        cart_dict, total = select_items()  # Begin item selection
        
        if total == 0 and cart_dict is None:  #Check if user exited without buying anything
            print(goodbye_message)  #Say goodbye and terminate the program
            break
        
        if total > 0:  
            if user_change > 0:  #Check if there's previous leftover change
                print(f"You have AED {user_change} in change. Applying to purchase.")
                if user_change >= total:  
                    user_change -= total  #Deduct total from the change
                    total = 0
                    print("Purchase covered by change.")
                else: 
                    total -= user_change  #Deduct the change amount from the total
                    user_change = 0
                    print(f"Remaining total: AED {total}")
            
            if total > 0:
                process_payment(total)  #Processes the remaining payment if needed
        
            deliver_items()  #Dispense the purchased items
            print(f"Remaining change: AED {user_change}")
            
            if user_change > 0:  #Ask if user wants to use leftover change
                reuse = input("Use change for another purchase? (y/n): ").lower()
                if reuse == "y":
                    continue  #Restart the purchase session with the leftover change
            
            recycle = input("Deposit glass bottles for recycling? (y/n): ").lower()
            if recycle == "y":
                recycle_bottle()  
        
        cart.clear()  #Clears the cart after the purchase is completed


#Runs the main function when the script is executed
if __name__ == "__main__":
    main()
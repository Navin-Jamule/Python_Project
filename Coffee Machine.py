# Menu dictionary contains each drink with its required ingredients and cost
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Logo for the machine
logo = """

            __  __                                 _     _            
           / _|/ _|                               | |   (_)           
  ___ ___ | |_| |_ ___  ___   _ __ ___   __ _  ___| |__  _ _ __   ___ 
 / __/ _ \|  _|  _/ _ \/ _ \ | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ \
| (_| (_) | | | ||  __/  __/ | | | | | | (_| | (__| | | | | | | |  __/
 \___\___/|_| |_| \___|\___| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                      
"""

# Initial profit and resource stock
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Step 1: Check if enough resources are available to make the drink
def resources_sufficent(want):
    possible = 0
    iteam = menu[want]['ingredients']
    
    # Check for each resource if it's sufficient
    if resources["water"] >= iteam['water'] and resources['milk'] >= iteam['milk'] and resources['coffee'] >= iteam['coffee']:
        possible = 1  # Enough resources
    return possible

# Step 4: Deduct used ingredients and add profit
def make_coffee(want):
    global profit 
    iteam = menu[want]['ingredients']
    value = menu[want]['cost']
    
    profit += value  # Add price to total profit
    
    # Deduct used ingredients from resources
    resources['water'] -= iteam['water']
    resources['milk']  -= iteam['milk']
    resources['coffee'] -= iteam['coffee']

# Step 3: Handle coin input and check if user paid enough
def process_coin(want, quarters, dimes, nickles, pennies):
    value = 0
    change = 0
    iteam = menu[want]
    price = iteam['cost']
    
    # Calculate total value inserted
    value += 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    
    # Check if enough money is provided
    if value >= price:
        change = value - price
        return round(change, 2)  # Return rounded change
    else:
        return change  # 0 implies not enough money

# Step 2: Main machine loop to take orders
def machine():
    print(logo)
    exit = False
    
    while not exit:
        # Ask for user input
        want = str(input('What would you like to order (cappuccino/latte/espresso)? '))
        
        # Step 1: Check resource sufficiency
        check_possible = resources_sufficent(want)
        if check_possible == 0:
            return "We are out of resources"
        else:
            # Step 2: Ask for coin input
            print('Make payment:')
            quarters = float(input('quarters: '))
            dimes = float(input('dimes: '))
            nickles = float(input('nickles: '))
            pennies = float(input('pennies: '))
            
            # Step 3: Process the coins and get change
            change = process_coin(want, quarters, dimes, nickles, pennies)
            
            # Step 4: If payment is not enough
            if change == 0:
                print('You don’t have enough money.')
                exit = True
            else:
                # Step 5: Make coffee and give change
                make_coffee(want)
                print(f"Here is your {want} and remaining change: ${change}")
                
                # Ask if the user wants more coffee
                ask = input('Do you want anything else? (yes/no): ').lower()
                check_report = input('Do you want to check the report? (yes/no): ')
                
                # Optional: Show resources and profit report
                if check_report == 'yes':
                    print(resources)
                    print(f'Total profit: ${profit}')
                    
                # Exit if user doesn't want more
                if ask == 'no':
                    print('Thank you!!')
                    exit = True

# Call the main function to start the machine
machine()

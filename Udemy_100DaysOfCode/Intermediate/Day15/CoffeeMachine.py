def checkresources(coffee_type):
    """ checks if the required coffee_type has all the needed resources."""
    for ingridient in menu[coffee_type]["ingridients"]:
        if menu[coffee_type]["ingridients"][ingridient] <= resources[ingridient]:
            pass
        else : 
            print(f"Sorry, there isn't enough {str(ingridient).split(' ')[0]}.")
            return False
    return True
    
def makecoffee(coffee_type):    
    for ingridient in menu[coffee_type]["ingridients"]:
        resources[ingridient] -= menu[coffee_type]["ingridients"][ingridient]
    resources["Money (Rs)"] += menu[coffee_type]["price"]

def checkmoney(coffee_type, amount):
    """ checks if the amount of money given is sufficient, if yes, if there is any change to be returned"""
    if(menu[coffee_type]["price"]<=amount):
        if(menu[coffee_type]["price"]<amount):
            amt = menu[coffee_type]["price"]
            print(f"Here is Rs{amount-amt} change.")
        return True
    else : 
        print("Sorry that's not enough money. Money refunded.")
        return False


coffee_type = " "

resources = {
    "Water (ml)" : 700,
    "Milk (ml)" : 450,
    "Coffee (g)" : 176,
    "Money (Rs)" : 0,
}

menu = {
    "espresso" : {
        "ingridients" : {
            "Water (ml)" : 50,
            "Coffee (g)" : 18,
            },
        "price" : 1.50 ,
        },
    "latte" : {
        "ingridients" : {
            "Water (ml)" : 200,
            "Milk (ml)" : 150,
            "Coffee (g)" : 24,
            },
        "price" : 2.50,
        },
    "cappuccino" : {
        "ingridients" : {
            "Water (ml)" : 250,
            "Milk (ml)" : 100,
            "Coffee (g)" : 24,
            },
        "price" : 3.0,
        },
}

sufficient_money = False
sufficient_resources = False


print("Welcome to Cyber Coffee cafe!")
while coffee_type != "off":
    coffee_type = input("What would you like? (espresso/latte/cappuccino) : ")
    if coffee_type == "report":
        #prints all the list of available resouces 
        for resource in resources:
            print(f"{resource} : {resources[resource]}")
    
    elif coffee_type == "off":
        print("GOodByE!")
    
    elif coffee_type in menu.keys() :
        if(checkresources(coffee_type)):
            print("Please insert coins :")
            quaters = int(input("How many quaters : "))
            dimes = int(input("How many dimes : "))
            nickels = int(input("How many nickels : "))
            pennies = int(input("How many pennies : "))
            amount = pennies * 0.01 + dimes * 0.10 + nickels * 0.05 + quaters * 0.25
            if(checkmoney(coffee_type,amount)):
                makecoffee(coffee_type)
                print(f"Here is your {coffee_type} ☕. Enjoy!")
    
    else :
        print("Invalid option!")          

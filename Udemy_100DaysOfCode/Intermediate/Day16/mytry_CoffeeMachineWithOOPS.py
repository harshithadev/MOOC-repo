class MenuItem:
    """Modals each menu item."""
    def __init__(self,name,cost,coffee,milk,water):
        self.name = name
        self.cost = cost
        self.ingridients = {
            "water":water,
            "coffee":coffee,
            "milk":milk
        }

class Menu:
    def get_items():
        """Returns all the names of the available menu items as a concatenated string."""
        pass
    
    def find_drink(order_name):
        """Parameter order_name: (str) The name of the drinks order.
        Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,
        otherwise returns None."""
        pass

class CoffeeMaker:
    def report():
        """Prints a report of all resources."""
        pass
    
    def is_resource_sufficient(drink):
        """Parameter drink: (MenuItem) The MenuItem object to make.
        Returns True when the drink order can be made, False if ingredients are insufficient"""
        pass
    
    def make_coffee(order):
        """ Parameter order: (MenuItem) The MenuItem object to make.
        Deducts the required ingredients from the resources."""
        pass

class MoneyMachine:
    def report():
        """Prints the current profit"""
        pass
    
    def make_payment(cost):
        """Parameter cost: (float) The cost of the drink.
            Returns True when payment is accepted, or False if insufficient."""
        pass

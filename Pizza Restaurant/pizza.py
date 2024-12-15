# Base Pizza Classes
class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita"
        self.cost = 5


class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Pepperoni"
        self.cost = 6


# Topping Decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()


class Cheese(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return f"{self.pizza.get_description()}, Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 1


class Olives(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return f"{self.pizza.get_description()}, Olives"

    def get_cost(self):
        return self.pizza.get_cost() + 0.5


class Mushrooms(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return f"{self.pizza.get_description()}, Mushrooms"

    def get_cost(self):
        return self.pizza.get_cost() + 0.7


# Inventory Manager Singleton
class InventoryManager:
    _instance = None

    def __init__(self):
        if InventoryManager._instance is not None:
            raise Exception("InventoryManager is a singleton!")
        self.inventory = {
            "Cheese": 10,
            "Olives": 10,
            "Mushrooms": 10,
        }
        InventoryManager._instance = self

    @staticmethod
    def get_instance():
        if InventoryManager._instance is None:
            InventoryManager()
        return InventoryManager._instance

    def check_availability(self, topping):
        return self.inventory.get(topping, 0) > 0

    def use_ingredient(self, topping):
        if self.check_availability(topping):
            self.inventory[topping] -= 1
        else:
            raise Exception(f"{topping} is out of stock!")


# Payment Methods
class Payment:
    def pay(self, amount):
        pass


class PayPal(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal."


class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card."


# Main Demonstration
if __name__ == "__main__":
    # Step 1: Create Pizza
    pizza = Margherita()
    print(f"Base Pizza: {pizza.get_description()}, Cost: ${pizza.get_cost()}")

    # Step 2: Add Toppings
    inventory = InventoryManager.get_instance()
    pizza = Cheese(pizza)
    inventory.use_ingredient("Cheese")
    pizza = Olives(pizza)
    inventory.use_ingredient("Olives")
    print(f"Final Pizza: {pizza.get_description()}, Total Cost: ${pizza.get_cost()}")

    # Step 3: Payment
    payment_method = PayPal()
    print(payment_method.pay(pizza.get_cost()))

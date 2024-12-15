# Design Patterns in Pizza Restaurant Ordering System

## 1. Decorator Pattern

### What It Is:
The Decorator Pattern lets you add features to an object without changing its original code.

### How It Works:
- Each topping, like Cheese, Olives, or Mushrooms, is a decorator.
- Toppings "wrap" around a pizza to add their description and cost.

### Example Code:
```python
pizza = Margherita()
pizza = Cheese(pizza)
pizza = Olives(pizza)
print(pizza.get_description())  # Outputs: "Margherita, Cheese, Olives"
print(pizza.get_cost())         # Outputs: 6.5
```

### Why It's Useful:
- You can add new toppings without changing the pizza classes.
- Makes the system flexible and reusable.

---

## 2. Singleton Pattern

### What It Is:
The Singleton Pattern makes sure there is only one instance of a class.

### How It Works:
- The `InventoryManager` class uses this pattern to ensure only one inventory controller exists.

### Example Code:
```python
inventory1 = InventoryManager.get_instance()
inventory2 = InventoryManager.get_instance()
print(inventory1 is inventory2)  # Outputs: True
```

### Why It's Useful:
- Keeps inventory management centralized.
- Prevents problems caused by having multiple instances of the same class.

---

## 3. Factory Pattern

### What It Is:
The Factory Pattern helps create objects without needing to know their exact class.

### How It Works:
- A function is used to create either a `Margherita` or `Pepperoni` pizza, based on input.

### Example Code:
```python
def create_pizza(pizza_type):
    if pizza_type == "Margherita":
        return Margherita()
    elif pizza_type == "Pepperoni":
        return Pepperoni()

pizza = create_pizza("Margherita")
print(pizza.get_description())  # Outputs: "Margherita"
```

### Why It's Useful:
- Makes creating new pizzas simple.
- Adding new pizza types in the future is easy.

---

## Overengineering in the Pizza System

### What It Means:
Overengineering happens when you make the system too complex for no good reason.

### Example of Overengineering:
```python
class VeganPizza(Margherita):
    def __init__(self):
        super().__init__()
        self.description = "Vegan Margherita"
        self.cost = 7
```
- This class is unnecessary. You could just add a "vegan" flag or modify the description.

### Why Avoid It:
- Makes the code harder to understand and update.
- Adds extra work without real benefits.

---

## Summary of Patterns
| **Design Pattern**    | **What It Does**                              |
| --------------------- | --------------------------------------------- |
| **Decorator Pattern** | Add toppings to pizzas dynamically.           |
| **Singleton Pattern** | Ensure there is one `InventoryManager`.        |
| **Factory Pattern**   | Simplify creating pizza objects.              |

Using these patterns makes the system simple, flexible, and easy to maintain.

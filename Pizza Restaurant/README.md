# Pizza Restaurant Ordering System

## Overview
This is a simple pizza restaurant ordering system built using Python. The system demonstrates the use of design patterns like **Decorator**, **Singleton**, and **Factory** to make the code easy to maintain, extend, and reuse.

## Features
1. **Base Pizzas**:
   - Margherita ($5)
   - Pepperoni ($6)
2. **Toppings**:
   - Cheese (+$1)
   - Olives (+$0.5)
   - Mushrooms (+$0.7)
3. **Inventory Management**:
   - Ensures ingredient availability using a Singleton design pattern.
4. **Flexible Payment**:
   - Supports PayPal and Credit Card payments.
5. **Output**:
   - Displays the final pizza description and total cost.
   - Confirms the payment method and displays a success message.

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/PizzaOrderingSystem.git
   cd PizzaOrderingSystem
   ```
2. **Run the Script**:
   ```bash
   python pizza_restaurant.py
   ```

## Example Output
### Creating a Pizza:
1. Start with a Margherita pizza.
2. Add Cheese and Olives as toppings.
3. Calculate the total cost.

**Output**:
```
Base Pizza: Margherita, Cost: $5
Final Pizza: Margherita, Cheese, Olives, Total Cost: $6.5
Paid $6.5 using PayPal.
```

## Design Patterns in the System
1. **Decorator Pattern**:
   - Adds toppings dynamically to the base pizza.
2. **Singleton Pattern**:
   - Ensures only one instance of `InventoryManager` exists.
3. **Factory Pattern**:
   - Simplifies the creation of pizza objects.

## Contributions
Feel free to submit issues or pull requests to improve the system.

## License
This project is open-source and free to use.

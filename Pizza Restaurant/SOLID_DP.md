# SOLID Principles and Design Patterns in Pizza Restaurant Ordering System

## 1. Single Responsibility Principle (SRP)

### Definition:

A class should do only one specific job.

### How It Works in the System:

- **Pizza Classes (`Pizza`, `Margherita`, `Pepperoni`)**:
  - These classes only handle the type of pizza and its basic details like cost and description.
- **Topping Classes (`Cheese`, `Olives`, `Mushrooms`)**:
  - Each topping class only adds its specific topping to a pizza.
- **`InventoryManager`**:
  - This is only responsible for checking and managing ingredient availability.
- **Payment Classes (`PayPal`, `CreditCard`)**:
  - Each class only handles one type of payment method.

### Why This Helps:

This way, changing one part of the system (like inventory) doesn’t affect other parts (like payments).

---

## 2. Open/Closed Principle (OCP)

### Definition:

The system should allow adding new features without changing existing code.

### How It Works in the System:

- **Pizza and Toppings**:
  - New toppings can be added by creating new classes without modifying existing pizza or topping classes.
- **Payment Methods**:
  - Adding a new payment method only requires creating a new class for it.

### Why This Helps:

You can expand the system (add toppings or payment methods) without breaking or changing the existing features.

---

## 3. Liskov Substitution Principle (LSP)

### Definition:

You should be able to replace a parent class with a child class without issues.

### How It Works in the System:

- **Pizza Types**:
  - `Margherita` and `Pepperoni` are child classes of `Pizza` and can be used anywhere a `Pizza` is needed.
- **Topping Classes**:
  - Topping classes like `Cheese`, `Olives`, and `Mushrooms` act like pizzas, keeping the behavior consistent.

### Why This Helps:

This makes the system flexible and ensures adding features doesn’t create errors.

---

## 4. Interface Segregation Principle (ISP)

### Definition:

Classes should not have to use methods they don’t need.

### How It Works in the System:

- **Payment Interface**:
  - The `Payment` class has only one method (`pay`), and each payment type (like `PayPal` or `CreditCard`) only implements what it needs.
- **Inventory Manager**:
  - Only has methods like `check_availability` and `use_ingredient`, so it’s simple and focused.

### Why This Helps:

This keeps the system easy to use and avoids unnecessary complexity.

---

## 5. Dependency Inversion Principle (DIP)

### Definition:

The system should depend on general ideas (abstractions) instead of specific details.

### How It Works in the System:

- **Payment System**:
  - The system uses the `Payment` class instead of directly using `PayPal` or `CreditCard`.
- **Pizza and Toppings**:
  - The system works with the general `Pizza` class, so adding new pizza types or toppings is easy.

### Why This Helps:

It makes the system flexible and easy to test or change.

---

## Summary of Design Patterns and SOLID Principles

| **Design Pattern**    | **SOLID Principles Followed** |
| --------------------- | ----------------------------- |
| **Decorator Pattern** | SRP, OCP, LSP                 |
| **Singleton Pattern** | SRP                           |
| **Factory Pattern**   | SRP, OCP                      |

By following these principles and patterns, the system is easy to maintain, update, and expand, while reducing bugs and problems.

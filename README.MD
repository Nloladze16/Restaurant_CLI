# Restaurant Menu & Order System

A simple **command-line restaurant management system** in Python that allows you to manage a menu and handle customer orders. The system supports adding, removing, editing menu items, creating orders, and viewing order summaries.  

---

## Features

### Menu Management
- Add items to the menu with a price.  
- Remove items from the menu.  
- Edit prices of existing items.  
- View the full menu with all items and prices.  
- Persist menu data using `menu.json`.  

### Order Management
- Add items to customer orders with quantities.  
- Remove items from orders.  
- View current order with total price calculation.  
- Handles invalid inputs like non-existing menu items or invalid quantities.  

### User-Friendly CLI
- Interactive command-line interface with numbered menu options.  
- Success and error messages displayed for user feedback.  
- Keeps menu and orders consistent across program runs.  

---

## Installation

1. Clone this repository or download the code:
```bash
git clone <your-repo-url>
Make sure you have Python 3 installed.

Navigate to the project directory:

bash
Copy code
cd restaurant-system
Run the program:

bash
Copy code
python main.py
Usage
Run the program with python main.py.

The menu options will be displayed:

mathematica
Copy code
==== Restaurant ====
1) View Menu
2) Add Item To Menu
3) Remove Item From Menu
4) Change Item Price In Menu
5) View Order
6) Add Item To Order
7) Remove Item From Order
8) Exit
====================
Enter the number corresponding to the action you want to perform.

Follow the prompts to add items, edit prices, or manage orders.

Example Workflow
Add menu items like "Pizza" or "Burger".

Place an order by specifying item and quantity.

View the current order with total price.

Remove items from the order or update quantities.

Exit the system when done.

Project Structure
css
Copy code
main.py          # Main program with Menu & Order classes
menu.json        # JSON file storing the menu data
README.md        # Project documentation
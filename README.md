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

## Requirements
- Python 3.x
- Core development and test dependencies are installed via `requirements.txt`
```bash
 pip install -r requirements.txt
```
- No external libraries are required to run the main script; tests use `pytest` (already included in `requirements.txt`).

## Usage
1. (Recommended) Install dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```
2. Save the main script as `main.py`.
3. Run the script from your terminal:
```bash
python main.py
```

4. The menu options will be displayed:

```python
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
```
Enter the number corresponding to the action you want to perform.


## Running Tests

This project includes test suite using `pytest` to verify script's functionality.
1. Install dependencies (includes pytest):
```bash
pip install -r requirements.txt
```
2. Save the code as `test_main.py`.
3. Run the tests from the terminal:
```bash
pytest
```
You should see output indicating that the tests have passed.


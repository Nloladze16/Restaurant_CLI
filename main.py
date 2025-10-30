import json
import os


class Menu:
    def __init__(self):
        self.menu = {}
        self.load_data()

    def add_menu(self, item, price):
        try:
            price = float(price)
            itemm = item.strip().capitalize()
            if not itemm:
                print(f"Item Can Not Be Empty String!\n")
                return
            if price < 0:
                print("Price Can't Be Lower Than 0.\n")
                return
            if itemm in self.menu:
                print(f"{itemm} Already Exists With The Price Of: ${price:.2f}.\n")
                return
            self.menu[itemm] = price
            self.save_data()
            print(f"{itemm} Was Added With Price ${price:.2f}.\n")
        except ValueError:
            print("Invalid Price! Please Enter A Valid Number.\n")

    def remove_menu(self, item):
        itemm = item.strip().capitalize()
        if itemm not in self.menu:
            print(f"{itemm} Was Not Found In The Menu!\n")
            return
        self.menu.pop(itemm)
        self.save_data()
        print(f"Removed {itemm} From The Menu.\n")

    def view_menu(self):
        if not self.menu:
            print("Menu Is Empty.\n")
            return
        i = 1

        for item, price in self.menu.items():

            print(f"{i}. {item} - {price:.2f}")
            i += 1

    def edit_price(self, item, price):
        try:
            item = item.strip().capitalize()
            price = float(price)
            if item not in self.menu:
                print(f"{item} Was Not Found In The Menu.\n")
                return
            if price < 0:
                print("Price Cant Be Lower Than 0!\n")
                return
            else:
                self.menu[item] = price
                self.save_data()
                print(f"{item} Price Was Changed To {price:.2f}\n")
        except ValueError:
            print("Invalid Price, Please Enter A Valid Number!\n")

    def save_data(self):
        with open("menu.json", "w") as f:
            json.dump(self.menu, f)

    def load_data(self):
        if not os.path.exists("menu.json"):
            return

        with open("menu.json", "r") as f:
            self.menu = json.load(f)


class Order:
    def __init__(self, menu):
        self.order = {}
        self.menu = menu

    def add_order(self, item, quantity):
        try:
            item = item.strip().capitalize()
            quantity = int(quantity.strip())

            if item not in self.menu:
                print(f"{item} Is Not In The Menu!")
            elif quantity <= 0:
                print("Quantity Cant Be Lower Than 1!")
            elif item in self.order:
                self.order[item] += quantity
                print(f"{item} Was Succsesfuly Added To Order.")
            else:
                self.order[item] = quantity
                print(f"{item} Was Succesfuly Added To Order.")

            print("\n")

        except ValueError:
            print(f"Quantity Should Be A Number!\n")

    def view_order(self):
        total = 0
        number = 1
        if self.order == {}:
            print(f"Order Is Empty.")
        else:
            for i in self.order.keys():
                i = i
                if i in self.menu.keys():
                    print(
                        f"{number}) {i}, Qty:{self.order[i]}, Price:{self.menu[i]*self.order[i]}"
                    )
                    total += self.menu[i] * self.order[i]
                    number += 1
            print(f"Total: {total}")
        print("\n")

    def remove_order(self, item):
        item = item.strip().capitalize()

        if item not in self.order:
            print(f"{item} Is Not In The Order.")
        else:
            self.order.pop(item)
            print(f"{item} Was Succsesfuly Removed From Order.")
        print("\n")


def menu_show():
    print("==== Restaurant ====")
    print("1) View Menu")
    print("2) Add Item To Menu")
    print("3) Remove Item From Menu")
    print("4) Change Item Price In Menu")
    print("5) View Order")
    print("6) Add Item To Order")
    print("7) Remove Item From Order")
    print("8) Exit")
    print("=" * 20)


if __name__ == "__main__":
    menu = Menu()
    order = Order(menu.menu)
    while True:
        menu_show()
        choice = input("Enter Your Choice (1-7): ").strip()

        if choice == "1":
            print("==== Restaurant Menu ====")
            menu.view_menu()
            print("\n")
        elif choice == "2":
            item = input(("Enter Item You Want To Add To Menu: "))
            price = input(("Enter The Price Of The Item: "))
            menu.add_menu(item, price)
            print("\n")
        elif choice == "3":
            if not menu.menu:
                print("Menu Is Empty.\n")
                continue
            item = input(("Enter Item You Want To Remove: "))
            menu.remove_menu(item)
            print("\n")
        elif choice == "4":
            if not menu.menu:
                print("Menu Is Empty.\n")
                continue
            item = input(f"Enter The Item You Want To Change Price To: ")
            price = input(f"Enter The New Price: ")
            menu.edit_price(item, price)
        elif choice == "5":
            print("==== Restaurant Order ====")
            order.view_order()
        elif choice == "6":
            if not order.menu:
                print("Cannot Create An Order — The Menu Is Empty!\n")
                continue
            item = input(f"Enter The Item You Want To Add To Order: ")
            quantity = input(f"Enter The Quantity Of The Item: ")
            order.add_order(item, quantity)
        elif choice == "7":
            if not order.order:
                print("Order Is Empty!\n")
                continue
            choice = input(f"Please Enter The Item You Want To Remove: ")
            order.remove_order(choice)
        elif choice == "8":
            print("Thanks For Visiting!")
            break
        else:
            print("Enter Valid Choice!\n")

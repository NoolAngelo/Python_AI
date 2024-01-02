class TakoyakiOrderingSystem:
    def __init__(self):
        self.total_cost = 0.0

    def display_menu(self):
        print("\t\t\t\t+=======================================+")
        print("\t\t\t\t            GELO'S TAKOYAKI MENU         ")
        print("\t\t\t\t Flavors:                                ")
        print("\t\t\t\t   1. Classic 4pcs             Php. 55.00")
        print("\t\t\t\t   2. Octopus 4pcs             Php. 65.00")
        print("\t\t\t\t   3. Green Onion 4pcs         Php. 55.00")
        print("\t\t\t\t   4. Cheese 4pcs              Php. 55.00")
        print("\t\t\t\t   5. Bacon 4pcs               Php. 65.00")
        print("\t\t\t\t   6. Crab 4pcs                Php. 65.00")
        print("\t\t\t\t   7. CANCEL")
        print("\t\t\t\t+=======================================+")

    def display_drinks(self):
        print("\t\t\t\t+=======================================+")
        print("\t\t\t\t                  Drinks                 ")
        print("\t\t\t\t Available canned:                       ")
        print("\t\t\t\t   1. Coke Original 325ml      Php. 34.10")
        print("\t\t\t\t   2. Coke Zero 325ml          Php. 34.50")
        print("\t\t\t\t   3. Sprite 325ml             Php. 34.10")
        print("\t\t\t\t   4. Royal 330ml              Php. 31.10")
        print("\t\t\t\t   5. Pepsi 320ml              Php. 26.95")
        print("\t\t\t\t   6. Mountain Dew 320ml       Php. 26.95")
        print("\t\t\t\t   7. CANCEL                             ")
        print("\t\t\t\t+=======================================+")

    def order_takoyaki(self, flavor, price):
        order_quantity = int(input("Order Quantity: "))
        order_cost = price * order_quantity
        self.total_cost += order_cost
        print(f"Total cost for {flavor} Takoyaki: Php. {order_cost} Added to Order")
        print(f"Overall selected items cost: {self.total_cost}")
        add_items = input("Would you like to add additional items? (Y/N): ").upper()
        while add_items not in ['Y', 'N']:
            print("Invalid choice. Please enter 'Y' for Yes or 'N' for No.")
            add_items = input("Would you like to add additional items? (Y/N): ").upper()
        if add_items == 'Y':
            while True:
                print("What item would you like to add?")
                print("1. Drink")
                print("2. Add New Takoyaki Order")
                choice1or2 = int(input("Your choice: "))
                if choice1or2 == 1:
                    self.display_drinks()
                    drink_choice = int(input("Select a drink (1-6) or 7 to cancel: "))
                    if 1 <= drink_choice <= 6:
                        drink_menu = ["Coke Original 325ml", "Coke Zero 325ml", "Sprite 325ml", "Royal 330ml", "Pepsi 320ml", "Mountain Dew 320ml"]
                        drink_prices = [34.10, 34.50, 34.10, 31.10, 26.95, 26.95]
                        drink_quantity = int(input("Drink Quantity: "))
                        if drink_quantity > 0:
                            print(f"You've added {drink_quantity} {drink_menu[drink_choice - 1]} to your order.")
                            self.total_cost += drink_prices[drink_choice - 1] * drink_quantity
                        else:
                            print("Drink order canceled.")
                    elif drink_choice == 7:
                        print("Drink order canceled.")
                    else:
                        print("Invalid choice.")
                elif choice1or2 == 2:
                    print("You've chosen to add a new takoyaki order.")
                    self.display_menu()
                    new_order_choice = int(input("Your choice for the new takoyaki order: "))
                    if new_order_choice == 1:
                        self.order_takoyaki("Classic", 55.00)
                    elif new_order_choice == 2:
                        self.order_takoyaki("Octopus", 65.00)
                    elif new_order_choice == 3:
                        self.order_takoyaki("Green Onion", 55.00)
                    elif new_order_choice == 4:
                        self.order_takoyaki("Cheese", 55.00)
                    elif new_order_choice == 5:
                        self.order_takoyaki("Bacon", 65.00)
                    elif new_order_choice == 6:
                        self.order_takoyaki("Crab", 65.00)
                    elif new_order_choice == 7:
                        print("Order canceled.")
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid choice.")
                add_items = input("Would you like to add more items? (Y/N): ").upper()
                while add_items not in ['Y', 'N']:
                    print("Invalid choice. Please enter 'Y' for Yes or 'N' for No.")
                    add_items = input("Would you like to add more items? (Y/N): ").upper()
                if add_items == 'N':
                    break
        print(f"Total cost: {self.total_cost} Php.")

    def get_total_cost(self):
        return self.total_cost


if __name__ == "__main__":
    print("\t\t\t\t+=======================================+")
    print("\t\t\t\t                              ")
    print("\t\t\t\t             GELO'S TAKOYAKI                ")
    print("\t\t\t\t                         ")
    print("\t\t\t\t            Press Enter to Order              ")
    print("\t\t\t\t          press Q to Quit Program           ")
    print("\t\t\t\t+=======================================+")
    input_choice = input()
    if input_choice.lower() == 'q':
        print("Program terminated.")
    else:
        ordering_system = TakoyakiOrderingSystem()
        ordering_system.display_menu()
        choice = int(input("Your choice: "))
        if choice == 1:
            ordering_system.order_takoyaki("Classic", 55.00)
        elif choice == 2:
            ordering_system.order_takoyaki("Octopus", 65.00)
        elif choice == 3:
            ordering_system.order_takoyaki("Green Onion", 55.00)
        elif choice == 4:
            ordering_system.order_takoyaki("Cheese", 55.00)
        elif choice == 5:
            ordering_system.order_takoyaki("Bacon", 65.00)
        elif choice == 6:
            ordering_system.order_takoyaki("Crab", 65.00)
        elif choice == 7:
            print("Order canceled.")
        else:
            print("Invalid choice.")
        print(f"Total cost: {ordering_system.get_total_cost()} Php.")
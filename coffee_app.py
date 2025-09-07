class Coffee: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Order: 
    def __init__(self):
        self.items = []
        
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to the order.")
        
    def total_price(self):
        return sum(item.price for item in self.items)
    
    def display_order(self):
        if not self.items:
            print("No items in the order.")
            return  
        print("Your Order:")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.name} - ${item.price:.2f}")
        
        print(f"Total Price: ${self.total_price():.2f}")
        
    def checkout(self):
        if not self.items:
            print("No items to checkout.")
            return  
        self.display_order()
        confirm = input("Confirm order? (yes/no): ").strip().lower()
        if confirm == 'yes':
            print("Order confirmed! Thank you for your purchase.")
            self.items.clear()
        else:
            print("Order cancelled.")

def main():
    menu_data = {
        "Americano": 3.00,
        "Cappuccino": 3.50,
        "Caffè macchiato": 3.75,
        "Latte": 4.00,
        "Espresso": 2.50,
        "Cold brew": 3.75,
        "Iced coffee": 3.25,
        "Irish coffee": 5.00,
        "Black coffee": 2.00,
        "Turkish coffee": 3.25,
    }

    menu_list = [Coffee(name, price) for name, price in menu_data.items()]

    order_instance = Order()
    
    while True:
        print("\n--- Coffee Menu ---")
        for i, coffee in enumerate(menu_list, 1):
            print(f"{i}. {coffee.name} - ${coffee.price:.2f}")
        
        print(f"{len(menu_list) + 1}. View Order")
        print(f"{len(menu_list) + 2}. Checkout")
        print(f"{len(menu_list) + 3}. Exit")
        
        choice = input(f"Select an option (1-{len(menu_list) + 3}): ").strip()
        
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menu_list):
                order_instance.add_item(menu_list[choice - 1])
            elif choice == len(menu_list) + 1:
                order_instance.display_order()
            elif choice == len(menu_list) + 2:
                order_instance.checkout()
            elif choice == len(menu_list) + 3:
                print("Thank you for visiting! Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

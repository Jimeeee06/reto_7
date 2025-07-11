import json
from queue import Queue
from collections import namedtuple

MenuSize = namedtuple('MenuSize', ['name', 'description'])

class MenuItem:
    def __init__(self, name: str, price: float, amount: int, type: str = None):
        self.__type = type
        self.name = name
        self.__price = price
        self.__amount = amount

    def total_price(self):
        return self.__price * self.__amount
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price:float):
        self.__price = price

    def get_type(self):
        return self.__type
    
    def set_type(self, type: str):
        self.__type = type
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount: int):
        self.__amount = amount

    def __str__(self):
        return f"{self.name} - $ {self.get_price()}"

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Beverage"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Beverage")

    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, amount: int, appetizer: str, type: str = "Main Course"):
        self.__appetizer = appetizer
        super().__init__(name, price, amount, type = "Main Course")
    
    def get_appetizer(self):
        return self.__appetizer
    
    def set_appetizer(self, appetizer: str):
        self.__appetizer = appetizer

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_appetizer()} - $ {self.get_price()}"

class Hamburger(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: MenuSize, type: str = "Hamburger"):
        self.__size = size
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Hamburger")
    
    def get_size(self):
        return self.__size.name
    
    def set_size(self, size: MenuSize):
        self.__size = size
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Pizza(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: MenuSize, type: str = "Pizza"):
        self.__size = size
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Pizza")
    
    def get_size(self):
        return self.__size.name
    
    def set_size(self, size: MenuSize):
        self.__size = size
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"
    
class Salad(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, size: MenuSize, type: str = "Salad"):
        self.__size = size
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Salad")
    
    def get_size(self):
        return self.__size.name
    
    def set_size(self, size: MenuSize):
        self.__size = size

    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Pasta(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Pasta"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Pasta")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class VeganFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Vegan Food"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Vegan Food")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - ${self.get_price()} -$ {self.get_flavour()}"

class SeaFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, fish_type: str, type: str = "Sea Food"):
        self.__fish_type = fish_type
        super().__init__(name, price, amount, type = "Sea Food")
    
    def get_fish_type(self):
        return self.__fish_type
    
    def set_fish_type(self, fish_type: str):
        self.__fish_type = fish_type

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_fish_type()} - $ {self.get_price()}"

class AsianFood(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Asian Food"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Asian Food")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Dessert"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Dessert")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Soup(MenuItem):
    def __init__(self, name: str, price: float, amount: int, flavour: str, type: str = "Soup"):
        self.__flavour = flavour
        super().__init__(name, price, amount, type = "Soup")
    
    def get_flavour(self):
        return self.__flavour
    
    def set_flavour(self, flavour: str):
        self.__flavour = flavour

    def __str__(self):
        return f"{self.get_type()} - {self.name} - {self.get_flavour()} - $ {self.get_price()}"

class Order:
    def __init__(self, order_number: int, discount: float = 0):
        self.order_number = order_number
        self.__items = []
        self.discount = discount


    def get_items(self):
        return self.__items

    def add_item(self, item: MenuItem):
        self.__items.append(item)

    def remove_item(self, item: MenuItem):
        if item in self.get_items():
            self.__items.remove(item)
        else:
            print("Item not found in the order.")

    def total_price(self) -> float:
        price = sum(item.get_price() * item.get_amount() for item in self.get_items())
        return price
    
    def calculate_discount(self) -> tuple:
        total = self.total_price()
        discount = 0
        message = "No discount applied"
        if total > 80000:
            discount = total * 0.20
            message = "20% off total"
        elif self.count_by_type("Dessert") > 4:
            beverage_discount = self.total_by_type("Beverage") * 0.30
            discount = beverage_discount
            message = "30% off beverages"
        elif self.total_by_type("Sea Food") > 50000:
            seafood_discount = self.total_by_type("Sea Food") * 0.10
            discount = seafood_discount
            message = "10% off seafood"
        elif any(item.get_type() == "Main Course" for item in self.get_items()):
            beverage_discount = self.total_by_type("Beverage") * 0.10
            discount = beverage_discount
            message = "10% discount on beverages (Main Course)"
        elif any(item.get_type() == "Dessert" for item in self.get_items()):
            beverage_discount = self.total_by_type("Beverage") * 0.15
            discount = beverage_discount
            message = "15% discount on beverages (Dessert)"
        total -= discount
        return total, f"{message}: -${discount:.2f}" if discount else message

    def total_by_type(self, item_type: str) -> float:
        return sum(item.get_price() * item.get_amount() for item in self.get_items() if item.get_type() == item_type)

    def count_by_type(self, item_type: str) -> int:
        return sum(item.get_amount() for item in self.get_items() if item.get_type() == item_type)
        
    def apply_discount(self):
        return self.calculate_discount()
        
    def __str__(self):
        order_details = f"Order Number: {self.order_number}\n"
        order_details += "Items:\n"
        for item in self.get_items():
            order_details += f" - {item} x {item.get_amount()} = ${item.total_price():.2f}\n"
        total_with_discount, discount_message = self.calculate_discount()
        if "No discount" not in discount_message:
            order_details += f"{discount_message}\n"
            order_details += f"Total Price with Discount: ${total_with_discount:.2f}"
        else:
            order_details += f"Total Price: ${total_with_discount:.2f}"
        return order_details
    

class Payment:
    def __init__(self, order: Order, medio_pago):
        self.__order = order
        self.__medio_pago = medio_pago
    
    def get_order(self):
        return self.__order
    
    def set_order(self, order: Order):
        self.__order = order
    
    def get_medio_pago(self):
        return self.__medio_pago
    
    def set_medio_pago(self, medio_pago):
        self.__medio_pago = medio_pago

    def realizar_pago(self):
        total, message = self.get_order().calculate_discount()
        print(f"Total a pagar: ${total:.2f}")
        self.get_medio_pago().pagar(total)

class MedioPago:
    def __init__(self):
        pass
 
    def pagar(self, monto):
        pass

class Tarjeta(MedioPago):
    def __init__(self, numero, cvv):
        super().__init__()
        self.__numero = numero
        self.__cvv = cvv

    def get_numero(self):
        return self.__numero
    
    def set_numero(self, numero):
        self.__numero = numero

    def get_cvv(self):
        return self.__cvv
    
    def set_cvv(self, cvv):
        self.__cvv = cvv
    
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta {self.get_numero()[-4:]}")

class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto):
        if self.monto_entregado >= monto:
            print(f"Pago realizado en efectivo. Cambio: ${self.monto_entregado - monto:.2f}")
        else:
            print(f"Fondos insuficientes. Faltan ${monto - self.monto_entregado:.2f} para completar el pago.")

class OrderManager:
    def __init__(self, menu_file: str = "menu.json"):
        self.__orders_queue = Queue()
        self.__completed_orders = []
        self.__in_progress_orders = []
        self.__next_order_number = 1
        self.__menu_file = menu_file
        self.__menu_data = self.load_menu()
    
    def create_order(self) -> 'Order':
        new_order = Order(self.__next_order_number)
        self.__orders_queue.put(new_order)
        self.__next_order_number += 1
        print(f"Orden #{new_order.order_number} creada y añadida a la cola.")
        return new_order
    
    def get_next_order(self) -> Order:
        if not self.__orders_queue.empty():
            order = self.__orders_queue.get()
            self.__in_progress_orders.append(order)
            print(f"Procesando orden #{order.order_number}")
            return order
        else:
            print("No hay órdenes pendientes")
            return None
    
    def complete_order(self, order: Order):
        if order in self.__in_progress_orders:
            self.__in_progress_orders.remove(order)
            self.__completed_orders.append(order)
            print(f"Orden #{order.order_number} completada")
        else:
            print("Orden no encontrada en órdenes en progreso")
    
    def get_pending_orders_count(self) -> int:
        return self.__orders_queue.qsize()
    
    def get_in_progress_orders_count(self) -> int:
        return len(self.__in_progress_orders)
    
    def get_completed_orders_count(self) -> int:
        return len(self.__completed_orders)
    
    def get_all_in_progress_orders(self) -> list:
        return self.__in_progress_orders.copy()
    
    def get_all_completed_orders(self) -> list:
        return self.__completed_orders.copy()
    
    def find_order(self, order_number: int) -> Order:
        for order in self.__in_progress_orders:
            if order.order_number == order_number:
                return order
        for order in self.__completed_orders:
            if order.order_number == order_number:
                return order
        print(f"Orden #{order_number} no encontrada.")
    
    def cancel_order(self, order_number: int) -> bool:
        for order in self.__in_progress_orders:
            if order.order_number == order_number:
                self.__in_progress_orders.remove(order)
                print(f"Orden #{order_number} cancelada (estaba en progreso)")
                return True
        print(f"Orden #{order_number} no encontrada en órdenes en progreso")
        return False
    
    def load_menu(self) -> dict:
        try:
            with open(self.__menu_file, 'r') as f:
                print(f"Menú cargado desde {self.__menu_file}")
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Archivo de menú no encontrado. Empezando con menú vacío.")
            return {}

    def save_menu(self):
        with open(self.__menu_file, 'w') as f:
            json.dump(self.__menu_data, f, indent=4)
            print("Menú guardado en el archivo.")


    def add_to_menu(self, item_type: str, item_details: dict):
        if 'name' not in item_details or 'price' not in item_details:
            print("Error: New item must have a 'name' and 'price'.")
            return
        if item_type not in self.__menu_data:
            self.__menu_data[item_type] = []
        if any(item['name'] == item_details['name'] for item in self.__menu_data[item_type]):
            print(f"Error: Item '{item_details['name']}' already exists in '{item_type}'.")
            return
        self.__menu_data[item_type].append(item_details)
        print(f"Added '{item_details['name']}' to '{item_type}' in the menu.")
        self.save_menu()

    def update_in_menu(self, item_type: str, item_name: str, updates: dict):
        if item_type not in self.__menu_data:
            print(f"Error: Item type '{item_type}' not found in menu.")
            return
        for item in self.__menu_data[item_type]:
            if item['name'] == item_name:
                item.update(updates)
                print(f"Updated '{item_name}' in the menu.")
                self._save_menu()
                return
        print(f"Error: Item '{item_name}' not found in '{item_type}'.")

    def delete_from_menu(self, item_type: str, item_name: str):
        if item_type not in self.__menu_data:
            print(f"Error: Item type '{item_type}' not found in menu.")
            return
        items_before = len(self.__menu_data[item_type])
        self.__menu_data[item_type] = [item for item in self.__menu_data[item_type] if item['name'] != item_name]
        if len(self.__menu_data[item_type]) < items_before:
            print(f"Deleted '{item_name}' from the menu.")
            self._save_menu()
        else:
            print(f"Error: Item '{item_name}' not found in '{item_type}'.")

    def show_menu(self):
        print("Restaurant Menu")
        if not self.__menu_data:
            print("The menu is currently empty.")
            return
        for item_type, items in self.__menu_data.items():
            print(f"\n## {item_type.upper()} ##")
            for item in items:
                details = [f"{k}: {v}" for k, v in item.items() if k not in ['name', 'price']]
                print(f"  - {item['name']} | Price: ${item['price']:.2f} | {', '.join(details)}")

    def __str__(self):
        summary = "=== RESUMEN DE ÓRDENES ===\n"
        summary += f"Órdenes pendientes: {self.get_pending_orders_count()}\n"
        summary += f"Órdenes en progreso: {self.get_in_progress_orders_count()}\n"
        summary += f"Órdenes completadas: {self.get_completed_orders_count()}\n"
        summary += f"Total de órdenes gestionadas: {self.__next_order_number - 1}\n"
        return summary
    

# Example usage
manager = OrderManager()

manager.show_menu()
manager.add_to_menu("Pasta", {"name": "Carbonara", "price": 32000, "flavour": "Classic"})

print("--- GESTIONANDO UNA ORDEN ---")
order_a = manager.create_order()


current_order = manager.get_next_order()

size_medium = MenuSize("Medium", "12-inch")
current_order.add_item(Pizza("Hawaiian", 35000, 1, "Sweet", size_medium))
current_order.add_item(Beverage("Cola", 5000, 2, "Classic"))


print(current_order)
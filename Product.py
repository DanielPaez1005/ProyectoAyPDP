class Product():
    def __init__(self, id, quantity, price):
        self.id = id
        self.quantity = quantity
        self.price = price * 1.16
        self.sales = 0
        self.total_amount = 0
    
    def modify_quantity(self, amount):
        """Modifica el quantity de productos
        """
        self.quantity -= amount
        self.sales += amount
    
    def calculate_amount(self):
        """Calcula el monto total de dinero gastado en productos por el cliente
        """
        self.total_amount = self.sales * self.price
    
    def show_info(self):
        """Muestra la informacion del producto
        """
        print(f"-Nombre: {self.id}")
        print(f"-quantity: {self.quantity}")
        print(f"-Precio: ${self.price}")
        print(f"-Vendidos: {self.sales}")
        print(f"-Monto total: ${self.total_amount}")

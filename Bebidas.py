from Product import Product

class Bebida(Product):
    def __init__(self, id, quantity, price, drink_type):
        super().__init__(id, quantity, price)
        self.drink_type = drink_type
    
    def modify_quantity(self, amount):
        """Modifica el quantity de productos"""
        return super().modify_quantity(amount)
    
    def show_info(self):
        """Muestra la informacion del producto
        """
        print(f"-Nombre: {self.id}")
        print(f"-Tipo de bebida: {self.drink_type}")
        print(f"-quantity: {self.quantity}")
        print(f"-Precio: ${self.price}")
        print(f"-Vendidos: {self.sales}")
        print(f"-Monto total: ${self.total_amount}")

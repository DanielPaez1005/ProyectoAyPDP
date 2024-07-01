from Product import Product

class Food(Product):
    def __init__(self, id, quantity, price, food_type):
        super().__init__(id, quantity, price)
        self.food_type = food_type
    
    def modify_quantity(self, amount):
        """Modifica el quantity de productos
        """
        return super().modify_quantity(amount)
    
    def show_info(self):
        """Muestra la informacion del producto
        """
        print(f"-Nombre: {self.id}")
        print(f"-Tipo de comida: {self.food_type}")
        print(f"-quantity: {self.quantity}")
        print(f"-Precio (Incluido el IVA): ${self.price}")
        print(f"-Vendidos: {self.sales}")
        print(f"-Monto total: ${self.total_amount}")

        
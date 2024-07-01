from Tickets import Ticket
from Product import Product

class Customer:
    def __init__(self, first_name, last_name, id_number, age):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.age = age
        self.has_special_discount = False
        self.has_vip_discount = False
        self.purchased_tickets = []
        self.purchased_products = []
        self.total_ticket_spend = 0
        self.total_product_spend = 0

    def generate_id_permutations(self, id_number):
        if len(id_number) == 1:
            return [id_number]
        
        permutations = []
        for i in range(len(id_number)):
            for j in self.generate_id_permutations(id_number[:i] + id_number[i+1:]):
                permutations.append(id_number[i] + j)

        return permutations

    def is_vampire_id(self):
        if len(self.id_number) % 2 != 0:
            return False

        permutations = self.generate_id_permutations(self.id_number)
        for perm in permutations:
            a = int(perm[:len(perm)//2])
            b = int(perm[len(perm)//2:])
            if a * b == int(self.id_number):
                return True
        
        return False

    def is_perfect_id(self):
        sum = 0
        for i in range(1, int(self.id_number)):
            if int(self.id_number) % i == 0:
                sum += i
        return sum == int(self.id_number)

    def check_discounts(self):
        if self.is_vampire_id():
            self.has_special_discount = True
            print("\nEl cliente tiene un descuento especial del 50% en la compra de tickets\n")
        
        if self.is_perfect_id():
            self.has_vip_discount = True
            print("\nEl cliente tiene un descuento VIP del 15% en los restaurantes\n")

    def calculate_ticket_spend(self):
        total_spend = 0
        for ticket in self.purchased_tickets:
            total_spend += ticket.price
        self.total_ticket_spend = total_spend

    def calculate_product_spend(self):
        total_spend = 0
        for product in self.purchased_products:
            total_spend += product.price
        self.total_product_spend = total_spend
        if self.has_vip_discount:
            self.total_product_spend *= 0.85

    def display_customer_info(self):
        print(f"Nombre: {self.first_name}")
        print(f"Apellido: {self.last_name}")
        print(f"Cédula: {self.id_number}")
        print(f"Edad: {self.age}")
        print(f"Descuento especial del 50% en la compra de tickets: {self.has_special_discount}")
        print(f"Descuento VIP del 15% en los restaurantes: {self.has_vip_discount}")
        print("\n\n\tEntradas compradas")
        for i, ticket in enumerate(self.purchased_tickets):
            print(f"\n________{i+1}________")
            ticket.display_ticket_info()
        print(f"\n-Total en entradas: ${self.total_ticket_spend}")

        if len(self.purchased_products) > 0:
            print("\n\n\tProductos comprados")
            for j, product in enumerate(self.purchased_products):
                print(f"\n________{j+1}________")
                product.display_product_info()
            print(f"\n-Total en productos: ${self.total_product_spend}")
        else:
            print("\n\n\tNo se han comprado productos")
        print(f"-Monto total gastado: ${self.total_ticket_spend + self.total_product_spend}")
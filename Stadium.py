class Stadium():
    def __init__(self, id, name, city, capacity):
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = []

    def show_info(self):
        """Muestra la información del estadio
        """
        print(f"-Id: {self.name}")
        print(f"-Nombre: {self.id}")
        print(f"-Ubicación: {self.city}")
        print(f"-Capacidad: {self.capacity[0] + self.capacity[1]}")
        print(f"\n\tRestaurantes")
        for n, restaurant in enumerate(self.restaurants):
            print(f"\n________{n+1}________")
            restaurant.show_info()
class Team():
    def __init__(self, id, code, name, group ):
        self.id = id
        self.name = name
        self.code = code
        self.group = group
        
        
    def show_info(self):
        """Muestra la información del equipo
        """
        print(f"-Id: {self.id}")
        print(f"-Equipo: {self.name}")
        print(f"-Código Fifa: {self.code}")
        print(f"-Grupo: {self.group}")
        
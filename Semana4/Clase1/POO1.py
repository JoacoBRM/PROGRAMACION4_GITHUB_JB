#Estrucutra de una clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"
    
persona1 = Persona("Joaquin", 50)
persona2 = Persona("Emilio", 49)

print(persona1.saludar())
print(persona2.saludar())

#Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def datos_completos(self):
        return f'{self.saludar()} estudio {self.carrera}'
    

estudiante1 = Estudiante("Pepito", 20, "Ing. Sistemas")
print(estudiante1.datos_completos())
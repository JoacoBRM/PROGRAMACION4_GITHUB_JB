class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad}'

def es_mayor_de_edad(edad):
    if edad >= 18:
        return "SI"
    else:
        return "NO"

p = Persona("Joaco", 19)
print(p.saludar())
print(f'Es mayor de edad? {es_mayor_de_edad(p.edad)}')
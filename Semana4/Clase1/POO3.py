# Definición de la clase Persona
class Persona:
    # Constructor que recibe nombre y edad al crear una instancia
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método que retorna un saludo con los datos de la persona
    def saludar(self):
        return f'Hola, me llamo {self.nombre} y tengo {self.edad}'

# Función externa que determina si una persona es mayor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "SI"  # Si la edad es 18 o más, es mayor de edad
    else:
        return "NO"  # Si no, es menor de edad

# Se crea una instancia de Persona con nombre "Joaco" y edad 19
p = Persona("Joaco", 19)

# Se imprime el saludo usando el método de la clase
print(p.saludar())

# Se verifica si la persona es mayor de edad usando la función externa
print(f'¿Es mayor de edad? {es_mayor_de_edad(p.edad)}')

# Estructura de una clase base llamada Persona
class Persona:
    # Método constructor que se ejecuta al crear una nueva instancia
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia 'nombre'
        self.edad = edad      # Atributo de instancia 'edad'
        
    # Método que devuelve un saludo con los datos de la persona
    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"

# Creación de dos objetos de la clase Persona
persona1 = Persona("Joaquin", 50)
persona2 = Persona("Emilio", 49)

# Llamada al método saludar de cada persona
print(persona1.saludar())
print(persona2.saludar())

# -------- HERENCIA --------

# Definición de una nueva clase Estudiante que hereda de Persona
class Estudiante(Persona):
    # Constructor que extiende el de la clase base con un nuevo atributo 'carrera'
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.carrera = carrera          # Atributo adicional propio de Estudiante
    
    # Método que devuelve una presentación más completa
    def datos_completos(self):
        return f'{self.saludar()} estudio {self.carrera}'

# Crear una instancia de Estudiante
estudiante1 = Estudiante("Pepito", 20, "Ing. Sistemas")

# Imprime la presentación completa del estudiante
print(estudiante1.datos_completos())

# Clase base llamada Animal
class Animal:
    # Método que puede ser sobrescrito por las clases hijas
    def hablar(self):
        return "hace un sonido"

# Clase Perro que hereda de Animal
class Perro(Animal):
    # Sobrescribe el método hablar para dar un comportamiento específico
    def hablar(self):
        return "ladra"

# Clase Gato que también hereda de Animal
class Gato(Animal):
    # También sobrescribe el método hablar
    def hablar(self):
        return "maulla"

# Lista de objetos que incluyen instancias de Perro, Gato y Animal
animales = [Perro(), Gato(), Animal()]

# Recorre la lista y llama al método hablar() de cada objeto
for animal in animales:
    print(animal.hablar())  # Aquí se demuestra el polimorfismo: misma llamada, diferentes comportamientos

# Imprime el resultado del método hablar() del primer elemento (un Perro)
print(animales[0].hablar())  # Resultado: "ladra"

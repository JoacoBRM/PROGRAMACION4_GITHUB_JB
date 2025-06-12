class Animal:
    def hablar(self):
        return "hace un sonido"
    
class Perro(Animal):
    def hablar(self):
        return "ladra"
    
class Gato(Animal):
    def hablar(self):
        return "maulla"
    
animales = [Perro(), Gato(), Animal()]

for animal in animales:
    print(animal.hablar())

print(animales[0].hablar())
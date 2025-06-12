class Calculadora:
    def suma(self, n1, n2):
        return n1+n2
    def resta(self, n1, n2):
        return n1-n2
    def multiplicacion(self, n1, n2):
        return n1*n2
    def division(self, n1, n2):
        if n2 == 0:
            return "No se puede dividir para 0!"
        return n1/n2
    
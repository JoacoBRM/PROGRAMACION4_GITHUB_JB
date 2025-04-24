print("***Funciones Recursivas***")
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Boooom!")

cuenta_regresiva(10)

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)
        
imprimir_lista([1,2,3,4,5])
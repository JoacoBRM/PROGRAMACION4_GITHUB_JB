# Imprime un título decorativo
print("***Funciones Recursivas***")

# Definición de una función recursiva para realizar una cuenta regresiva
def cuenta_regresiva(numero):
    # Decrementa el número en 1
    numero -= 1
    
    # Si el número aún es mayor que 0, imprime el número y vuelve a llamar a la función
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)  # llamada recursiva
    else:
        # Cuando el número ya no es mayor que 0, imprime "Boooom!" como fin de la cuenta
        print("Boooom!")

# Llamada inicial a la función con el número 10
cuenta_regresiva(10)


# Definición de una función para imprimir todos los elementos de una lista
def imprimir_lista(lista):
    # Itera sobre cada elemento en la lista y lo imprime
    for elemento in lista:
        print(elemento)
        
# Llama a la función con una lista de ejemplo
imprimir_lista([1, 2, 3, 4, 5])

# Inicializa la variable contador con 0
contador = 0

# Bucle while que se ejecuta mientras contador sea distinto de 5
while contador != 5:
    print(contador)     # Imprime el valor actual de contador
    contador += 1       # Incrementa contador en 1

# Imprime una línea divisoria
print("=======")

# Aquí hay un error: falta el argumento del rango en range()
# Debe especificarse un valor para indicar hasta dónde contará el bucle for
# Por ejemplo, si se desea repetir lo mismo que en el while, puedes usar range(5):
for i in range(5):
    print(i)

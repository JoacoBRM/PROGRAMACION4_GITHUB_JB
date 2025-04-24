# Realizado por Joaquín Bermeo

try:
    # Muestra un menú con las operaciones básicas disponibles
    print("Menú:\n(1) Suma\n(2) Resta\n(3) Multiplicación\n(4) División")
    
    # Solicita al usuario que ingrese una opción del menú
    opcion = int(input(">> Ingrese su opción: "))
    
    # Verifica si la opción está dentro del rango permitido (1 a 4)
    if opcion in range(1,5):
        # Solicita al usuario que ingrese dos números reales (pueden tener decimales)
        num1 = float(input("Ingrese el número 1: "))
        num2 = float(input("Ingrese el número 2: "))
        print("")
        
        # Realiza la operación correspondiente según la opción seleccionada
        if opcion == 1:
            respuesta = num1 + num2  # Suma
        elif opcion == 2:
            respuesta = num1 - num2  # Resta
        elif opcion == 3:
            respuesta = num1 * num2  # Multiplicación
        else:
            # Antes de dividir, verifica que el divisor no sea cero
            if num2 == 0:
                print("⚠️  ERROR, no se puede dividir para 0")
                # Se puede usar "exit()" aquí si se desea terminar el programa inmediatamente
                respuesta = "Sin Definir"
            else:
                respuesta = num1 / num2  # División segura
        # Muestra el resultado de la operación
        print(">> Resultado: ", respuesta)
        
    else:
        # Si la opción ingresada no está entre 1 y 4, muestra un mensaje de error
        print("⚠️  ERROR, su opción no es válida!")
        
# Captura errores de conversión si el usuario ingresa un valor no numérico
except ValueError:
    print("⚠️  ERROR, ingrese un número!")


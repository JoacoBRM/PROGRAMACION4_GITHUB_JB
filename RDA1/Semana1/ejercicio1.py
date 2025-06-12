#Realizado por Joaquín Bermeo
try:
    print("Menú:\n(1) Suma\n(2) Resta\n(3) Multiplicación\n(4) División")
    opcion = int(input(">> Ingrese su opción: "))
    
    if opcion in range(1,5):
        num1 = float(input("Ingrese el número 1: "))
        num2 = float(input("Ingrese el número 2: "))
        print("")
        if opcion == 1:
            respuesta = num1+num2
        elif opcion == 2:
            respuesta = num1-num2
        elif opcion == 3:
            respuesta = num1*num2
        else:
            if num2 == 0:
                print("⚠️  ERROR, no se puede divir para 0")
                #Se puede usar "exit()" para terminar el programa justo en la linea donde se lo añada
                respuesta = "Sin Definir"
            else:
                respuesta = num1/num2
        print(">> Resultado: ",respuesta)
        
    else:
        print("⚠️  ERROR, su opción no es válida!")
except ValueError:
    print("⚠️  ERROR, ingrese un numero!")

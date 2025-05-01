from herramientas import registrar_estudiante, asignar_calificacion, mostrar_informacion_com, mostrar_todos_estudiantes
#Funcion para crear el menu principal
def menu():
    while True:
        #Se imprime el menu
        print("\n\t\t << | MENU DE OPCIONES| >>")
        print("(1) Registrar un nuevo estudiante")
        print("(2) Asignar una calificacion")
        print("(3) Mostrar informacion del estudiante")
        print("(4) Mostrar todos los estudiantes")
        print("(5) Salir") 
        
        #Se valida la entrada del usuario
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("ERROR, opcion no válida. Ingresar un numero del 1 al 5!.")
            continue
        
        #Se compara la opcion ingresada por el usuario con un if y elifs
        if opcion == 1:
            print("\n\t\t| NUEVO ESTUDIANTE |")
            registrar_estudiante()

        elif opcion == 2:
            print("\n\t\t| ASIGNAR CALIFICACION |")
            asignar_calificacion()
            

        elif opcion == 3:
            print("\n\t\t| MOSTRAR INFORMACION |")
            mostrar_informacion_com()
            

        elif opcion == 4:
            print("\n\t\t| ESTUDIANTES REGISTRADOS |")
            mostrar_todos_estudiantes()
            
        elif opcion == 5:
            print("\n Gracias por usar el sistema :3")
            break
        else:
            print("\nERROR, esta no opcion no esta dentro del rango!")

if __name__ == "__main__":
    menu()
#Se importan todas las funciones del archivo utilidades
from utilidades import registrar_huesped, crear_reserva, mostrar_huespedes, mostrar_reservas

#Funcion para crear el menu principal
def menu():
    while True:
        #Se imprime el menu
        print("\n\t\t << | MENU DE OPCIONES| >>")
        print("(1) Registrar un nuevo huesped")
        print("(2) Crear una nueva reserva")
        print("(3) Mostrar todas las reservas")
        print("(4) Mostrar todos los huespedes registrados")
        print("(5) Salir") 
        
        #Se valida la entrada del usuario
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("ERROR, opcion no válida. Ingresar un numero del 1 al 5!.")
            continue
        
        #Se compara la opcion ingresada por el usuario con un if y elifs
        if opcion == 1:
            print("\n\t\t| NUEVO HUESPED |")
            registrar_huesped()

        elif opcion == 2:
            print("\n\t\t| NUEVA RESERVA |")
            crear_reserva()

        elif opcion == 3:
            print("\n\t\t| RESERVAS REGISTRADAS |")
            mostrar_reservas()

        elif opcion == 4:
            print("\n\t\t| HUESPEDES REGISTRADOS |")
            mostrar_huespedes()

        elif opcion == 5:
            print("\n Gracias por usar el sistema :3")
            break
        else:
            print("\nERROR, esta no opcion no esta dentro del rango!")

if __name__ == "__main__":
    menu()

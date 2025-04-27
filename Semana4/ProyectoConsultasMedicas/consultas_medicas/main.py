# Se importa las funciones definidas en el archivo funciones.py
from funciones import registrar_paciente, registrar_consulta, mostrar_paciente, mostrar_todos_pacientes

# Función principal del menú
def menu():
    while True:
        # Muestra el menú de opciones
        print("\n\t\t << | MENU DE OPCIONES| >>")
        print("(1) Registrar nuevo paciente\n(2) Registar una consulta medica\n(3) Mostrar los datos completos del paciente\n(4) Mostrar todos los pacientes registrados\n(5) Salir")
        
        # Intenta capturar una opción válida (un número entre 1 y 5)
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            # Si el usuario ingresa algo que no es un número, muestra un mensaje de error y sigue pidiendo una opción válida
            print("ERROR, opcion no válida. Ingresar un numero del 1 al 5!.")
            continue
        
        # Opción para registrar un nuevo paciente
        if opcion == 1:
            print("\n\t\t| NUEVO PACIENTE |")
            # Llama a la función registrar_paciente para registrar un nuevo paciente
            registrar_paciente()
        
        # Opción para registrar una nueva consulta médica
        elif opcion == 2:
            print("\n\t\t| NUEVA CONSULTA |")
            # Llama a la función registrar_consulta para registrar una consulta médica
            registrar_consulta()
        
        # Opción para mostrar los datos completos de un paciente
        elif opcion == 3:
            print("\n\t\t| DATOS PACIENTE |")
            # Llama a la función mostrar_paciente para mostrar los datos de un paciente específico
            mostrar_paciente()
        
        # Opción para mostrar todos los pacientes registrados
        elif opcion == 4:
            print("\n\t\t| PACIENTES REGISTRADOS |")
            # Llama a la función mostrar_todos_pacientes para mostrar todos los pacientes
            mostrar_todos_pacientes()
        
        # Opción para salir del programa
        elif opcion == 5:
            print("\n Gracias por usar el sistema :3")
            # Salir del bucle infinito, terminando el programa
            break
        
        # Si el usuario ingresa una opción fuera del rango 1-5, muestra un mensaje de error
        else:
            print("\nERROR, esta no opcion no esta dentro del rango!")

# Comprobamos si el script está siendo ejecutado directamente y, si es así, se llama al menú
if __name__ == "__main__":
    menu()

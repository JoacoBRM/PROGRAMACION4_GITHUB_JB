# Se importa la clase Paciente desde el archivo paciente.py
from paciente import Paciente
# Se importa la clase datetime para manipular fechas
from datetime import datetime

# Lista que almacena todos los pacientes registrados
lista_pacientes = []

# Función para registrar un nuevo paciente
def registrar_paciente():
    # Lista de tipos de sangre válidos
    tipos_sangre = ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

    # Captura del nombre del paciente
    nombre = input("Nombre: ")
    # Captura de la cédula, asegurándose de que no sea repetida
    cedula = validar_cedula()
    while buscar_paciente_cedula(cedula) != None:  # Verifica que la cédula no esté registrada
        print("ERROR, cédula repetida!")
        cedula = validar_cedula()
    
    # Captura de la edad, validando que sea un número positivo
    while True:
        try:
            edad = int(input("Edad: "))
            if edad < 0:
                print("ERROR, no puede ingresar una edad negativa!")
                continue
            break
        except ValueError:  # Si se ingresa algo que no sea un número, muestra un error
            print("ERROR, edad no válida!")
            continue
    
    # Captura del tipo de sangre, validando que sea uno de los tipos permitidos
    tipo_sangre = input("Tipo de sangre (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
    while tipo_sangre not in tipos_sangre:  # Si el tipo de sangre no es válido
        print("ERROR, tipo de sangre no valido!")
        tipo_sangre = input("Tipo de sangre (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
    
    # Crea un objeto Paciente y lo agrega a la lista de pacientes
    paciente = Paciente(nombre, cedula, edad, tipo_sangre)
    lista_pacientes.append(paciente)
    print(">> Paciente registrado con éxito :).")

# Función para validar la cédula (debe ser un número de 10 dígitos)
def validar_cedula():
    cedula = input("Ingrese la cedula: ")
    while cedula.isdigit() == False or len(cedula) < 10:  # Si la cédula no es válida
        print("ERROR, cedula no valida!")
        cedula = input("Ingrese la cedula: ")
    return cedula

# Función para buscar un paciente por cédula en la lista
def buscar_paciente_cedula(cedula):
    # Recorre la lista de pacientes para encontrar uno con la misma cédula
    for paciente in lista_pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None  # Si no lo encuentra, devuelve None

# Función para registrar una consulta para un paciente
def registrar_consulta():
    if lista_pacientes:  # Si hay pacientes registrados
        cedula = validar_cedula()  # Valida la cédula del paciente
        paciente = buscar_paciente_cedula(cedula)  # Busca el paciente en la lista
        if paciente:  # Si el paciente es encontrado
            # Bucle para validar que la fecha no sea futura
            while True:
                try:
                    fecha = input("Fecha (DD/MM/AAAA): ")
                    fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")  # Intenta convertir la fecha
                    if fecha_valida > datetime.today():  # Si la fecha es futura
                        print("ERROR, La fecha no puede ser futura!")
                    else:
                        break  # Si la fecha es válida, rompe el bucle
                except ValueError:  # Si la fecha no es válida, muestra un error
                    print("ERROR, fecha no valida!")
                
            # Captura del diagnóstico y tratamiento
            diagnostico = input("Diagnóstico: ")
            tratamiento = input("Tratamiento: ")
            
            # Llama al método para agregar la consulta al historial del paciente
            paciente.agregar_consulta(fecha, diagnostico, tratamiento)
            print(">> Consulta registrada correctamente :).")
        else:
            print("Paciente no encontrado :(")
    else:
        print("No hay pacientes registrados!")

# Función para mostrar los datos de un paciente
def mostrar_paciente():
    if lista_pacientes:  # Si hay pacientes registrados
        cedula = validar_cedula()  # Valida la cédula del paciente
        paciente = buscar_paciente_cedula(cedula)  # Busca el paciente en la lista
        if paciente:  # Si el paciente es encontrado
            paciente.mostrar_informacion()  # Muestra la información básica del paciente
            paciente.mostrar_consultas()  # Muestra el historial de consultas
        else:
            print("Paciente no encontrado :(")
    else:
        print("No hay pacientes registrados!")

# Función para mostrar todos los pacientes registrados
def mostrar_todos_pacientes():
    contador = 1  # Inicia el contador para mostrar el número de paciente
    if lista_pacientes:  # Si hay pacientes registrados
        print(f'>> Número de pacientes registrados: {len(lista_pacientes)}')
        for paciente in lista_pacientes:  # Recorre todos los pacientes
            print(f'\n| PACIENTE #{contador}|')
            paciente.mostrar_informacion()  # Muestra los datos del paciente
            contador += 1  # Aumenta el contador para el siguiente paciente
    else:
        print("No hay pacientes registrados!")  # Si no hay pacientes, muestra un mensaje

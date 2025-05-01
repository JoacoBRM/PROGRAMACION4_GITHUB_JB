from reserva import Reserva
from huesped import Huesped
from datetime import datetime

#Se crean dos listas, una para guardar los huespedes y otra las reservas
lista_huespedes = []
lista_reservas = []


#Funcion que recibe como parametro una cedula, si encuentra un huesped con esa cedula devuelve al paciente sino un None
def buscar_huesped(cedula):
    for huesped in lista_huespedes:
        if huesped.cedula == cedula:
            return huesped
    return None
   
#Funcion que valida si la cedula ingresada tiene solo numeros y si la cantidad de caracteres sean 10
def validar_cedula():
    cedula = input("Ingrese la cedula: ")
    while cedula.isdigit() == False or len(cedula) < 10:
        print("ERROR, cedula no valida!")
        cedula = input("Ingrese la cedula: ")
    return cedula

#Funcion que captura la informacion necesaria para crear el objeto huesped y luego guardarlo en una lista
def registrar_huesped():
    nombre = input("Ingrese el nombre del nuevo huesped: ")
    cedula = validar_cedula()
    while buscar_huesped(cedula) != None: #Validar que no haya cedulas repetidas
        print("ERROR, ya existe un huesped registrado con esta cedula!")
        cedula = validar_cedula()
    correo_electronico = input("Ingrese el correo personal del nuevo huesped: ")
    huesped = Huesped(nombre, cedula, correo_electronico)    
    lista_huespedes.append(huesped)
    print("-- Huesped registrado con exito :) --")
    

#Funcion similar a la anterior, igual captura los datos necesarios y guarda la reserva en una lista
def crear_reserva():
    if lista_huespedes: #Si la lista contiene al menos un dato
        cedula = validar_cedula()
        huesped = buscar_huesped(cedula)
        if huesped:
            while True:
                try:
                    fecha_entrada = input("(1) Fecha de entrada (DD/MM/AAAA): ")
                    fecha_entrada_valida = datetime.strptime(fecha_entrada, "%d/%m/%Y") #Validacion de fecha valida y formato (DIA/MES/AÑO)
                    break
                    
                except ValueError: 
                    print("ERROR, fecha no valida!")
                    
            while True:
                try:
                                        
                    fecha_salida = input("(2) Fecha de salida (DD/MM/AAAA): ") 
                    fecha_salida_valida = datetime.strptime(fecha_salida, "%d/%m/%Y") #Validacion de fecha valida y formato (DIA/MES/AÑO)
                    break  
                except ValueError:
                    print("ERROR, fecha no valida!")

            tipo_habitacion = input("(3) Ingrese el tipo de habitacion: ")
            
            nueva_reserva = Reserva(huesped, fecha_entrada_valida, fecha_salida_valida, tipo_habitacion)
            lista_reservas.append(nueva_reserva)
            print("-- Reserva creada con exito :) --")
        else:
            print("Huesped no encontrado :(")
    else:
        print("No hay huespedes registrados :(")

#Funcion que se encarga de mostrar de manera numerada cada uno de los huespedes registrados
def mostrar_huespedes():
    contador_huespedes = 1
    if lista_huespedes: #Si la lista tiene al menos un dato
        print(f'>> Número de huespedes registrados: {len(lista_huespedes)}')
        for huesped in lista_huespedes:
            print(f'\n\t\t| HUESPED #{contador_huespedes}|')
            huesped.mostrar_info() 
            contador_huespedes += 1
    else:
        print("No hay huespedes registrados!")

#Funcion que se encarga de mostrar de manera numerada cada una de las reservas registradas
def mostrar_reservas():
    contador_reservas = 1
    if lista_reservas:
        print(f'>> Número reservas registradas: {len(lista_reservas)}')
        for reserva in lista_reservas:
            print(f'\n\t\t| RESERVA #{contador_reservas}|')
            reserva.mostrar_info() 
            contador_reservas += 1
    else:
        print("No hay reservas registradas!")
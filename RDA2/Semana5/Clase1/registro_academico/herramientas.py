from estudiante import Estudiante
from calificacion import Calificacion
#Lista donde se guardan todos los estudaintes
lista_estudiantes = []

#Funcion que busca por matricula y retorna un estudiante si se encuentra
def buscar_estudiante(matricula):
    for estudiante in lista_estudiantes:
        if estudiante.matricula == matricula:
            return estudiante
    return None

#Funcion que valida que la matricula ingresada sean solo numeros
def validar_matricula():
    while True:
        try:
            matricula = int(input("Ingrese la matricula del estudiante: "))
            return matricula
        except ValueError:
            print("ERROR, matricula no valida. Ingrese solo numeros!")

#Funcion que captura los datos necesarios para crear el objeto estudiante
def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    
    matricula = validar_matricula()
    while buscar_estudiante(matricula) != None: #Se valida que la matricula no se repita para cada estudiante
        print("ERROR, matricula repetida!")
        matricula = validar_matricula()
        
    carrera = input("Ingrese la carrera del estudiante: ")
    nuevo_estudiante = Estudiante(nombre, matricula, carrera) #Se crea el objeto
    lista_estudiantes.append(nuevo_estudiante) #Se añade el objeto a la lista
    print("Estudiante registrado con exito! ")

#Funcion que crea el objeto calificacion y lo añade al estudiante respectivamente
def asignar_calificacion():
    if lista_estudiantes: #Se valida que haya al menos un dato en la lista estudiantes
        matricula = validar_matricula()
        estudiante = buscar_estudiante(matricula)
        if estudiante:
            materia = input("Ingrese la materia: ")
            while True: #Se valida que se ingrese solo numeros y que esten entre 0 y 10
                try:
                    nota = int(input("Ingrese la nota respectiva a la materia (0-10): "))
                    if nota >= 0 and nota <= 10:
                        break
                    else:
                        print("ERROR, ingrese una calificacion entre 0 y 10!")
                        continue
                except:
                    print("ERROR, nota invalida!. Ingrese solo numeros.")
            nueva_calificacion = Calificacion(materia, nota) #Se crea el objeto calificacion
            estudiante.agregar_calificacion(nueva_calificacion) #Se añade el objeto a la lista calificaciones de la clase estudiante
        else:
            print("No se encontro al estudiante! ")
    else:
        print("NO hay estudiantes registrados!")

#Funcion que permite mostrar la información completa del estudiante
def mostrar_informacion_com():
    if lista_estudiantes: # Se valida que haya al menos un estudiante
        matricula = validar_matricula()
        estudiante = buscar_estudiante(matricula)
        if estudiante: #Si se encuentra al estudiante 
            print(f'\n\t\t| DATOS DEL ESTUDIANTE |')
            estudiante.mostrar_info()
            print("--- Calificaciones ---")
            estudiante.mostrar_calificaciones()
        else:
            print("No se encontró al estudiante!")
    else:
        print("No hay estudiantes registrados!")

#Función que permite mostrar la información principal de todos los estudiantes registrados   
def mostrar_todos_estudiantes():
    contador = 1
    if lista_estudiantes: #Se valida que haya al menos un estudiante
        for estudiante in lista_estudiantes:
            print(f'> ESTUDIANTE #{contador}')
            estudiante.mostrar_info()
            contador += 1
    else:
        print("No hay estudiantes registrados! ")
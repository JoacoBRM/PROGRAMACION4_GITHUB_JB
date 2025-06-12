# Definición de la clase Paciente
class Paciente:
    # Constructor de la clase, inicializa los atributos del paciente
    def __init__(self, nombre, cedula, edad, tipo_sangre):
        self.nombre = nombre         # Atributo que almacena el nombre del paciente
        self.cedula = cedula         # Atributo que almacena la cédula del paciente
        self.edad = edad             # Atributo que almacena la edad del paciente
        self.tipo_sangre = tipo_sangre  # Atributo que almacena el tipo de sangre del paciente
        self.lista_consultas = []    # Inicializa una lista vacía para almacenar las consultas del paciente

    # Método para agregar una nueva consulta al historial del paciente
    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        consulta = {  # Crea un diccionario con los datos de la consulta
            "fecha": fecha, 
            "diagnostico": diagnostico, 
            "tratamiento": tratamiento
        }
        self.lista_consultas.append(consulta)  # Agrega la consulta a la lista de consultas del paciente

    # Método para mostrar la información básica del paciente
    def mostrar_informacion(self):
        print('\n>>> DATOS <<<')
        # Muestra los datos básicos del paciente (nombre, cédula, edad, tipo de sangre)
        print(f'Nombre: {self.nombre}\nCedula: {self.cedula}\nEdad: {self.edad}\nTipo de Sangre: {self.tipo_sangre}')

    # Método para mostrar el historial de consultas del paciente
    def mostrar_consultas(self):
        contador_mostrar_inf = 1  # Contador para numerar las consultas
        print("\n>>> Historial de Consultas <<<")
        
        if self.lista_consultas:  # Si el paciente tiene consultas registradas
            # Itera sobre todas las consultas y las imprime
            for consulta in self.lista_consultas:
                print(f'\nConsulta #{contador_mostrar_inf}:')
                # Muestra la información de la consulta: fecha, diagnóstico y tratamiento
                print(f'Fecha: {consulta["fecha"]}\nDiagnostico: {consulta["diagnostico"]}\nTratamiento: {consulta["tratamiento"]}')
                contador_mostrar_inf += 1  # Aumenta el contador de consultas
        else:
            print("AVISO! No existen registros.")  # Si no hay consultas, muestra un mensaje

class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.lista_calificaciones = [] #Lista donde se guardan todas las calificaciones
        
    #Metodo que agrega la calificacion a la lista   
    def agregar_calificacion(self, calificacion):
        self.lista_calificaciones.append(calificacion)
        
    #Metodo que muestra la informacion principal del estudiante
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}\nMatricula: {self.matricula}\nCarrera: {self.carrera}\n')
        
    #Metodo que muestra todas las calificaciones del estudiante que se encuentran en la lista, sino hay se avisa que no existen calificaciones registradas
    def mostrar_calificaciones(self):   
        contador = 1
        if self.lista_calificaciones:
            for calificacion in self.lista_calificaciones:
                print(f' ++ Materia #{contador}')
                calificacion.mostrar_notas()
                contador+=1
        else:
            print("No hay calificaciones registradas")
            
            
        
        
        
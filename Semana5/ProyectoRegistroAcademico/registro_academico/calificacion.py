class Calificacion:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota
    
    #Metodo de la clase Calificacion que muestra la materia y la nota
    def mostrar_notas(self):
        print(f'{self.materia} ---> Nota: {self.nota}')
        
        
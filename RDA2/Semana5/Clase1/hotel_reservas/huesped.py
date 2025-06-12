class Huesped:
    def __init__(self, nombre, cedula, correo_electronico):
        
        self.nombre = nombre
        self.cedula = cedula
        self.correo_electronico = correo_electronico

    #Metodo de la clase huesped que muestra la informacion personal del huesped
    def mostrar_info(self):
        print(f'Nombre: {self.nombre}\nCedula: {self.cedula}\nEdad: {self.correo_electronico}')
    
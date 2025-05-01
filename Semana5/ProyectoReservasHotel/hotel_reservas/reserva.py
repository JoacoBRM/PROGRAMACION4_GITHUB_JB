class Reserva:
    def __init__(self, huesped, fecha_entrada, fecha_salida, tipo_habitacion):
        self.huesped = huesped
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.tipo_habitacion = tipo_habitacion
    
    #Metodo de la clase reserva que muestra la informacion principal del huesped y los daatos de su respectiva reserva
    def mostrar_info(self):
        print("> Datos del Huesped: ")
        print(f'Nombre: {self.huesped.nombre}\nCedula: {self.huesped.cedula}\n')
        print("> Datos de la Reserva: ")
        print(f'Fecha de Entrada: {self.fecha_entrada.date()}')
        print(f'Fecha de Salida: {self.fecha_salida.date()}')
        print(f'Tipo de Habitacion: {self.tipo_habitacion}')

        
        
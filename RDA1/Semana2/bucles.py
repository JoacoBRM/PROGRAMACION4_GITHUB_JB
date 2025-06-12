#for i in range(1,5,1): #La candicion de este for seria 5>i lo que permite gestionar menos cantidad de datos.
    #print(i)

#Se ingresa por teclado un valor entero y se enlistao desde el 0 hasta el valor ingresado
#valor = int(input("Ingrese un valor limite: "))
#for i in range(valor+1): #Esta manera es mas optima que sumar +1 al i
#    print(i) #---> "i+1"


#=====================================================================================
#print("\n")  
#for i in [1,2,3,4,10]:
#    print(i)
#    
#=====================================================================================
#for i in range(0,6):
#    print("tabla del ",i)
#    for j in range(0,11):
#        print(i,"x",j,"=","i*j")

#Lista desde -10 al 10 y que identifique que numero es par o impar
#=====================================================================================
#a = -10
#while a < 11:
#    if a%2 == 0:
#        print(a, "---> Es par")
#    else:
#        print(a,"--> Es impar")
#    a += 1
#=====================================================================================
# def nombre(apellido, nombre):
#     print(f'Nombre: {nombre}\nApellido: {apellido}')
    
# nombre("Bermeo","Joaquin") #POSICIONAL
# print("=============")
# nombre(nombre="Joaquin",apellido="Bermeo") #NOMINAL

# print("\n")
# def nombre2(apellido, nombre, edad='10'): #Argumento por defecto
#     print(f'Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}')
    
# nombre2("Bermeo","Joaquin") #Se va a imprimir el argumento por defecto
# nombre2("Bermeo","Joaquin","20") #Se va a remplazar el argumento por defecto

#=====================================================================================
def menu(*platos): # '*' sirve para cuando hay una n cantidad de argumentos que van a ingresar
    print("Hoy tenemos: ",end='')
    for plato in platos:
        print(plato, end=', ')

menu('pasta','pizza','ensalada')
print('\n')

def contacto(**info):
    print("Datos del contacto")
    for clave, valor in info.items():
        print(clave, ":", valor)
contacto(Nombre = 'Joaquin',Apellido='Bermeo')

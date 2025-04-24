# Se asignan valores a las variables a, b y c
a = 4
b = 2
c = 6

# Se evalúa si 'a' es mayor que 'b'
if a > b:
    print("a es mayor que b")  # Si 'a' es mayor que 'b', se imprime este mensaje

# Si no se cumple la condición anterior, se evalúa si 'a' es igual a 'b'
elif a == b:
    print("a es igual a b")  # Si 'a' es igual a 'b', se imprime este mensaje

# Si no se cumplen las condiciones anteriores, se evalúa si 'a' es menor que 'c'
elif a < c:
    print("a es menor que c")  # Si 'a' es menor que 'c', se imprime este mensaje

# Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque 'else'
else:
    print("a no es mayor que b ni menor que c")  # Se imprime este mensaje en caso de que no se cumpla ninguna condición

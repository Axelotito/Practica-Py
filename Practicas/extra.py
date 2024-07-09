""" Implementa una función que tome tres parámetros enteros, m, n y k. 
La función debe devolver una matriz con m filas y n columnas, 
donde cada elemento sea un número entero aleatorio. Además,
la suma de todos los elementos de la matriz debe ser igual a k.

La matriz generada no debe contener ceros. """

import random

def generar_matriz_con_suma(m, n, k):
    # Genera una lista plana de m*n elementos
    elementos = [random.randint(1, k) for _ in range(m * n)]
    
    # Ajustar la suma para que sea igual a k
    suma_actual = sum(elementos)
    diferencia = k - suma_actual

    # Mientras la diferencia no sea cero, ajustara un elemento aleatorio
    while diferencia != 0:
        i = random.randint(0, m * n - 1)
        ajuste = random.randint(1, abs(diferencia))
        if diferencia > 0:
            elementos[i] += ajuste
        elif diferencia < 0 and elementos[i] > ajuste:
            elementos[i] -= ajuste
        diferencia = k - sum(elementos)
    
    matriz = [elementos[i * n:(i + 1) * n] for i in range(m)]
    return matriz

# Pruebas
m = 3
n = 2
k = 45
matriz = generar_matriz_con_suma(m, n, k)
for fila in matriz:
    print(fila)
print("Suma de la matriz:", sum(sum(fila) for fila in matriz))
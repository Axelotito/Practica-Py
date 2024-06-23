""" Ordena una lista de numero de menos a mayor """
""" lo hare por el algoritmos de burbuja """

cadena1 = [10,2,1,3,5,6,7,8,9,4]

def bubble_short(cadena):
    n = len(cadena)

    for i in range(n):
        for j in range(0, n-i-1):
            
            if cadena[j] > cadena[j+1]:
                cadena[j], cadena[j+1] = cadena[j+1], cadena[j]
    return cadena

print("Esta es la cadena:",cadena1)
print(bubble_short(cadena1))


""" Tambien se puede hacer con el metodo sort() """

cadena1.sort()

print('ordernada =', cadena1)
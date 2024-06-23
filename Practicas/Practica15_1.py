""" Es el mismo ejercicio pero usando otro algoritmo """

cadena = [1,24,6,7,8,4,3,23,5,76,468,5,758]

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        medio = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quick_sort(izquierda) + medio + quick_sort(derecha)
    
print(cadena)
print(quick_sort(cadena))
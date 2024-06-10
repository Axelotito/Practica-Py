# Bubble Sort

## Descripción
- Algoritmo de ordenación sencillo
- Compara elementos adyacentes e intercambia si están en orden incorrecto
- Repite el proceso hasta que la lista está ordenada

## Funcionamiento
- Iteraciones múltiples
  - Cada pasada recorre la lista
  - Valores grandes "burbujearán" hacia el final
- Proceso de comparación e intercambio
  - Compara elementos adyacentes
  - Intercambia si el primer elemento es mayor
- Termina cuando no se realizan intercambios

## Pasos
- **Paso 1**: Comparar primeros dos elementos
- **Paso 2**: Moverse al siguiente par de elementos
- **Paso 3**: Repetir hasta el final de la lista
- **Paso 4**: Repetir todo el proceso excluyendo el último elemento ordenado
- **Paso 5**: Terminar cuando no se hagan intercambios

## Ejemplo
- Lista inicial: `[5, 1, 4, 2, 8]`
  - Primera pasada:
    - Compara 5 y 1, intercambia: `[1, 5, 4, 2, 8]`
    - Compara 5 y 4, intercambia: `[1, 4, 5, 2, 8]`
    - Compara 5 y 2, intercambia: `[1, 4, 2, 5, 8]`
    - Compara 5 y 8, no intercambia: `[1, 4, 2, 5, 8]`
  - Segunda pasada:
    - Compara 1 y 4, no intercambia: `[1, 4, 2, 5, 8]`
    - Compara 4 y 2, intercambia: `[1, 2, 4, 5, 8]`
    - Compara 4 y 5, no intercambia: `[1, 2, 4, 5, 8]`
  - Tercera pasada:
    - Compara 1 y 2, no intercambia: `[1, 2, 4, 5, 8]`
    - Compara 2 y 4, no intercambia: `[1, 2, 4, 5, 8]`
  - Lista ordenada: `[1, 2, 4, 5, 8]`

## Implementación en Python
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada:", bubble_sort(lista))

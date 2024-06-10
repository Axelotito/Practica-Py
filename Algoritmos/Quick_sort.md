# Quick Sort

## Descripción
- Algoritmo de ordenación eficiente
- Utiliza el enfoque "divide y vencerás"
- Selecciona un pivote y particiona la lista en sublistas

## Funcionamiento
- Selección del pivote
  - Puede ser el primer elemento, el último, el medio o un elemento aleatorio
- Particionamiento
  - Elementos menores que el pivote a la izquierda
  - Elementos mayores que el pivote a la derecha
- Llamadas recursivas
  - Ordena las sublistas izquierda y derecha recursivamente

## Pasos
- **Paso 1**: Seleccionar un pivote
- **Paso 2**: Particionar la lista en tres partes
  - Elementos menores que el pivote
  - Elementos iguales al pivote
  - Elementos mayores que el pivote
- **Paso 3**: Ordenar recursivamente las sublistas izquierda y derecha
- **Paso 4**: Combinar las sublistas ordenadas y el pivote

## Ejemplo
- Lista inicial: `[10, 7, 8, 9, 1, 5]`
  - Seleccionar pivote: 8
  - Particionar: `[7, 1, 5]`, `[8]`, `[10, 9]`
  - Ordenar recursivamente:
    - `[7, 1, 5]` -> pivote 5 -> `[1]`, `[5]`, `[7]`
    - `[10, 9]` -> pivote 9 -> `[9]`, `[10]`
  - Combinar: `[1, 5, 7, 8, 9, 10]`

## Implementación en Python
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
lista = [10, 7, 8, 9, 1, 5]
print("Lista ordenada:", quick_sort(lista))

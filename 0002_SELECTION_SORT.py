
def selection_sort(arr):
    n = len(arr)
    # Iterar a través de todos los elementos de la lista
    for i in range(n):
        # Encontrar el valor mínimo sin ordenar en la lista restante
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Intercambiar el valor mínimo con el primer elemento sin ordenar
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print (arr)
# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print("La lista ordenada es:")
for i in range(len(arr)):
    print("%d" %arr[i])

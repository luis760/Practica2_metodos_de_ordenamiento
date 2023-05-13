def insertion_sort(arr):
    # Iterar a través de todos los elementos de la lista
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mover los elementos mayores que la clave hacia adelante en la lista
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insertar la clave en su posición correcta
        arr[j + 1] = key
        print(arr)
# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)
print("La lista ordenada es:")
for i in range(len(arr)):
    print("%d" %arr[i])

def merge_sort(arr):
    # Verificar si la lista tiene más de un elemento
    if len(arr) > 1:
        # Dividir la lista en mitades izquierda y derecha
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Ordenar las mitades izquierda y derecha recursivamente
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Inicializar los índices de los subarreglos y la lista combinada
        i = j = k = 0
        
        # Combinar las mitades izquierda y derecha en la lista ordenada
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Añadir cualquier elemento restante de la mitad izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Añadir cualquier elemento restante de la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        print (arr)
# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print("La lista ordenada es:")
for i in range(len(arr)):
    print("%d" %arr[i])

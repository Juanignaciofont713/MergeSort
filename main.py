def merge_sort(arr):
    if len(arr) > 1:
        # Dividir el arreglo en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializamos los índices para el arreglo izquierdo (i), derecho (j) y para la lista ordenada (k)
        i = j = k = 0

        # Combinamos las dos mitades
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificamos si queda algún elemento en la mitad izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificamos si queda algún elemento en la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10, 1]
print("Arreglo original:", arr)
merge_sort(arr)
print("Arreglo ordenado:", arr)
 
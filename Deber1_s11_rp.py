def bubble_sort(row):
    n = len(row)
    for i in range(n):
        for j in range(0, n-i-1):
            if row[j] > row[j+1]:
                row[j], row[j+1] = row[j+1], row[j]
    return row

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Matriz 3x3
matrix = [
    [34, 23, 12],
    [45, 78, 56],
    [67, 89, 24]
]

# Fila a ordenar (por ejemplo, la segunda fila con índice 1)
row_to_sort = 1

print("Matriz original:")
print_matrix(matrix)

# Ordenando la fila específica
matrix[row_to_sort] = bubble_sort(matrix[row_to_sort])

print("\nMatriz con la fila {} ordenada:".format(row_to_sort + 1))
print_matrix(matrix)

def cascada_sum(n):
    # Creamos una matriz de n x n llena de ceros
    matriz = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            # CASO BASE: Si es la primera fila (r=0) o primera columna (c=0)
            if r == 0 or c == 0:
                matriz[r][c] = 1
            else:
                # LÓGICA DE TRANSICIÓN:
                # ¿Qué valores deberías sumar aquí?
                # matriz[r][c] = ??? + ???
                matriz[r][c] = matriz[r-1][c] + matriz[r][c-1]
                # pass

    return matriz


# Debería devolver:
# [[1, 1, 1],
#  [1, 2, 3],
#  [1, 3, 6]]
print(cascada_sum(3))

def spiralOrder(matrix):
    min_col = min_row = 0
    max_col, max_row = len(matrix[0]), len(matrix)
    row = 0
    output = []
    while min_col < max_col and min_row < max_row:
        print(min_col, max_col)
        for col in range(min_col, max_col):
            output.append(matrix[row][col])
        min_row += 1

        for row in range(min_row, max_row):
            output.append(matrix[row][col])
        max_col -= 1

        if min_col < max_col and min_row < max_row:

            for col in range(max_col-1, min_col-1, -1):
                output.append(matrix[row][col])
            max_row -= 1
            for row in range(max_row-1, min_row-1, -1):
                output.append(matrix[row][col])
            min_col += 1
    return output


""" [ [1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9] ] """

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix))


def spiralOrder1(matrix):
    # Línea 1: Define una función llamada 'spiralOrder' que toma una 'matrix' (lista de listas) como entrada.
    # Ejemplo: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    min_col = min_row = 0
    # Línea 2: Inicializa 'min_col' y 'min_row' a 0.
    # Estos representan los límites superior e izquierdo de la capa actual de la espiral.

    max_col, max_row = len(matrix[0]), len(matrix)
    # Línea 3: Inicializa 'max_col' y 'max_row'.
    # - 'len(matrix)' da el número de filas (alto de la matriz).
    # - 'len(matrix[0])' da el número de columnas (ancho de la matriz, asumiendo que la matriz no está vacía y las filas tienen la misma longitud).
    # Estos representan los límites inferior y derecho de la capa actual de la espiral.
    # Para matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    # max_col será 3, max_row será 3.

    row = 0
    # Línea 4: Inicializa 'row' a 0. Esta variable se usa para el primer bucle 'for' para indicar en qué fila estamos.
    # ¡OJO! Esta variable 'row' fuera del bucle se usa de forma un poco particular, ya que luego se redefine dentro de los bucles.
    # Esto puede ser un poco confuso al principio.

    output = []
    # Línea 5: Inicializa una lista vacía llamada 'output'. Aquí se almacenarán los elementos de la matriz en orden espiral.

    while min_col < max_col and min_row < max_row:
        # Línea 6: Este es el bucle principal. Continuará mientras los límites de columna y fila no se hayan cruzado o encontrado.
        # Es decir, mientras haya elementos sin recorrer en la capa actual.
        # Si min_col == max_col o min_row == max_row, significa que no queda una capa válida (se ha recorrido todo).

        # --- FASE 1: Recorrer la fila superior (de izquierda a derecha) ---
        for col in range(min_col, max_col):
            # Línea 7: Bucle para recorrer las columnas de 'min_col' hasta 'max_col - 1'.
            # La 'row' utilizada aquí es la 'row' que tenía antes de este bucle (inicialmente 0).
            output.append(matrix[row][col])
            # Línea 8: Añade el elemento actual (de la fila 'row' y la columna 'col') a la lista 'output'.
        # Después de este bucle, 'col' tendrá el valor de 'max_col - 1' (la última columna visitada).

        min_row += 1
        # Línea 9: Incrementa 'min_row' en 1. Esto significa que la fila superior ya ha sido visitada,
        # así que la próxima "capa" de la espiral comenzará una fila más abajo.
        # Si matrix = [[1,2,3], [4,5,6], [7,8,9]]:
        # Primera iteración:
        # matrix[0][0], matrix[0][1], matrix[0][2] (1, 2, 3) se añaden a output.
        # output = [1, 2, 3]
        # min_row se convierte en 1.

        # --- FASE 2: Recorrer la columna derecha (de arriba hacia abajo) ---
        # ¡OJO! La variable 'row' aquí toma el valor final del bucle anterior si hubiera uno,
        # o el valor que tenía antes de este bucle. Este es un punto de posible confusión.
        # La forma correcta de pensarlo es que `row` es el índice de fila y `col` es el índice de columna.
        # El `col` aquí es el *último* `col` del bucle anterior (max_col - 1).
        for row in range(min_row, max_row):
            # Línea 10: Bucle para recorrer las filas de 'min_row' hasta 'max_row - 1'.
            # Aquí, 'col' es el valor que tenía después del bucle anterior (max_col - 1).
            output.append(matrix[row][col])
            # Línea 11: Añade el elemento actual (de la fila 'row' y la columna 'col') a la lista 'output'.
        # Después de este bucle, 'row' tendrá el valor de 'max_row - 1' (la última fila visitada).

        max_col -= 1
        # Línea 12: Decrementa 'max_col' en 1. Esto significa que la columna derecha ya ha sido visitada,
        # así que la próxima "capa" de la espiral terminará una columna más a la izquierda.
        # Para matrix = [[1,2,3], [4,5,6], [7,8,9]]:
        # En la primera iteración:
        # matrix[1][2], matrix[2][2] (6, 9) se añaden a output.
        # output = [1, 2, 3, 6, 9]
        # max_col se convierte en 2.

        # --- Comprobación de límites antes de recorrer las fases inferiores ---
        # Esta comprobación es crucial para matrices no cuadradas o cuando se alcanza el centro.
        # Evita intentar recorrer una fila o columna que ya no existe (o que ya fue completamente recorrida).
        if min_col < max_col and min_row < max_row:
            # Línea 13: Comprueba si todavía hay al menos una fila y una columna para recorrer.
            # Si, por ejemplo, solo queda una fila en el centro (matriz 1xN o Nx1),
            # o si ya hemos recorrido todas las filas/columnas, las siguientes fases no deben ejecutarse.

            # --- FASE 3: Recorrer la fila inferior (de derecha a izquierda) ---
            # La 'row' aquí es el valor que tenía después del bucle anterior (max_row - 1).
            for col in range(max_col-1, min_col-1, -1):
                # Línea 14: Bucle para recorrer las columnas de 'max_col - 1' (la penúltima columna visitada)
                # hasta 'min_col' (excluyendo min_col-1). El paso es -1 para ir hacia atrás.
                output.append(matrix[row][col])
                # Línea 15: Añade el elemento actual a la lista 'output'.
            # Después de este bucle, 'col' tendrá el valor de 'min_col'.

            max_row -= 1
            # Línea 16: Decrementa 'max_row' en 1. Esto significa que la fila inferior ya ha sido visitada.
            # Para matrix = [[1,2,3], [4,5,6], [7,8,9]]:
            # En la primera iteración:
            # matrix[2][1], matrix[2][0] (8, 7) se añaden a output.
            # output = [1, 2, 3, 6, 9, 8, 7]
            # max_row se convierte en 2.

            # --- FASE 4: Recorrer la columna izquierda (de abajo hacia arriba) ---
            # La 'col' aquí es el valor que tenía después del bucle anterior (min_col).
            for row in range(max_row-1, min_row-1, -1):
                # Línea 17: Bucle para recorrer las filas de 'max_row - 1' (la penúltima fila visitada)
                # hasta 'min_row' (excluyendo min_row-1). El paso es -1 para ir hacia atrás.
                # Aquí, 'col' es el valor que tenía después del bucle anterior (min_col).
                output.append(matrix[row][col])
                # Línea 18: Añade el elemento actual a la lista 'output'.
            # Después de este bucle, 'row' tendrá el valor de 'min_row'.

            min_col += 1
            # Línea 19: Incrementa 'min_col' en 1. Esto significa que la columna izquierda ya ha sido visitada.
            # Para matrix = [[1,2,3], [4,5,6], [7,8,9]]:
            # En la primera iteración:
            # matrix[1][0] (4) se añade a output.
            # output = [1, 2, 3, 6, 9, 8, 7, 4]
            # min_col se convierte en 1.

    return output
    # Línea 20: Una vez que el bucle 'while' termina (cuando min_col >= max_col o min_row >= max_row),
    # significa que todos los elementos han sido visitados. La función devuelve la lista 'output'.

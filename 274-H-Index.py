def hIndex(citations):

    n = len(citations)
    paperCounts = [0] * (n + 1)

    for c in citations:
        paperCounts[min(n, c)] += 1

    h = n
    papers = paperCounts[n]

    while papers < n:
        h -= 1
        papers += paperCounts[n]
    return h


citations = [1, 8, 4, 5, 7]
print(hIndex(citations))


def hIndex1(citations):
    # Línea 1: Define una función llamada 'hIndex' que toma una lista de enteros 'citations' como entrada.
    # 'citations' representa el número de citas que ha recibido cada una de las publicaciones de un investigador.
    # Ejemplo: citations = [3, 0, 6, 1, 5] significa que hay 5 artículos, con 3, 0, 6, 1 y 5 citas respectivamente.

    n = len(citations)
    # Línea 2: Calcula el número total de publicaciones (artículos) que tiene el investigador.
    # Esto se obtiene simplemente como la longitud de la lista 'citations'.
    # Para citations = [3, 0, 6, 1, 5], n será 5.

    paperCounts = [0] * (n + 1)
    # Línea 3: Inicializa una lista llamada 'paperCounts' con n + 1 elementos, todos inicializados a 0.
    # Esta lista actuará como una especie de "cubetas" o "frecuencias".
    # El índice de 'paperCounts' representará un número de citas, y el valor en ese índice
    # representará cuántos artículos tienen *ese número exacto de citas o más* (hasta 'n').
    # El tamaño es n+1 porque queremos índices desde 0 hasta n.
    # Para n = 5, paperCounts será [0, 0, 0, 0, 0, 0] (6 elementos, índices 0 a 5).

    for c in citations:
        # Línea 4: Inicia un bucle 'for' para iterar sobre cada número de citas 'c' en la lista 'citations'.
        # Esto nos permite contar cuántos artículos tienen un cierto número de citas.

        paperCounts[min(n, c)] += 1
        # Línea 5: Esta es la parte clave del conteo.
        # min(n, c) hace dos cosas:
        # 1. Si el número de citas 'c' es mayor que el número total de publicaciones 'n',
        #    simplemente lo "corta" a 'n'. Esto es porque un artículo con, por ejemplo, 100 citas,
        #    contribuye a un posible índice h de 5 de la misma manera que un artículo con 5 citas,
        #    si el total de publicaciones es 5. No puede haber un índice h mayor que el número total de publicaciones.
        # 2. Si 'c' es menor o igual que 'n', simplemente usa 'c'.
        # Luego, incrementa el contador en la posición correspondiente en 'paperCounts'.

        # Vamos a seguir con citations = [3, 0, 6, 1, 5] y n = 5:
        # c = 3: min(5, 3) = 3. paperCounts[3] += 1.  paperCounts = [0, 0, 0, 1, 0, 0]
        # c = 0: min(5, 0) = 0. paperCounts[0] += 1.  paperCounts = [1, 0, 0, 1, 0, 0]
        # c = 6: min(5, 6) = 5. paperCounts[5] += 1.  paperCounts = [1, 0, 0, 1, 0, 1]
        # c = 1: min(5, 1) = 1. paperCounts[1] += 1.  paperCounts = [1, 1, 0, 1, 0, 1]
        # c = 5: min(5, 5) = 5. paperCounts[5] += 1.  paperCounts = [1, 1, 0, 1, 0, 2]

    # Al final del bucle, paperCounts nos dice:
    # paperCounts[0] = 1 (1 artículo con 0 citas)
    # paperCounts[1] = 1 (1 artículo con 1 cita)
    # paperCounts[2] = 0 (0 artículos con 2 citas)
    # paperCounts[3] = 1 (1 artículo con 3 citas)
    # paperCounts[4] = 0 (0 artículos con 4 citas)
    # paperCounts[5] = 2 (2 artículos con 5 o más citas - en este caso, 5 y 6)

    h = n
    # Línea 6: Inicializa la variable 'h' con el valor de 'n' (número total de publicaciones).
    # 'h' representa nuestro candidato actual para el índice h. Empezamos con el valor máximo posible.
    # Para n = 5, h será 5.

    papers = paperCounts[n]
    # Línea 7: Inicializa la variable 'papers' con el número de artículos que tienen 'n' o más citas.
    # Esta variable acumulará el total de artículos que tienen al menos 'h' citas.
    # Para n = 5, papers será paperCounts[5] = 2 (los artículos con 5 y 6 citas).

    while papers < h:
        # Línea 8: Inicia un bucle 'while'. Este bucle se ejecuta mientras el número acumulado de 'papers'
        # (artículos con al menos 'h' citas) sea menor que nuestro candidato 'h'.
        # El objetivo es encontrar el 'h' más grande para el cual la condición 'papers >= h' se cumple.
        # Empezamos con h=5 y papers=2. Como 2 < 5, el bucle se ejecutará.

        # Primera iteración del while:
        # h = 5, papers = 2. Condition (2 < 5) is True.
        h -= 1
        # Línea 9: Decrementa 'h' en 1. Estamos probando un índice h más pequeño.
        # h se convierte en 4.

        papers += paperCounts[h]
        # Línea 10: Suma a 'papers' la cantidad de artículos que tienen exactamente el nuevo valor de 'h' citas.
        # papers se convierte en papers + paperCounts[4] = 2 + 0 = 2.
        # Ahora h = 4, papers = 2. Condition (2 < 4) is True. El bucle se repite.

        # Segunda iteración del while:
        # h = 4, papers = 2. Condition (2 < 4) is True.
        h -= 1
        # Línea 9: h se convierte en 3.

        papers += paperCounts[h]
        # Línea 10: papers se convierte en papers + paperCounts[3] = 2 + 1 = 3.
        # Ahora h = 3, papers = 3. Condition (3 < 3) is False. El bucle termina.

    return h
    # Línea 11: Cuando el bucle 'while' termina, significa que hemos encontrado el valor más grande de 'h'
    # para el cual 'papers' (el número de artículos con al menos 'h' citas) es mayor o igual que 'h'.
    # La función devuelve este valor de 'h'.
    # En nuestro ejemplo, devuelve 3. (Oops, mi ejemplo manual anterior dio 4, veamos por qué la discrepancia)

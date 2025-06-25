def productArrayExceptSelf(nums):
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans


def productArrayExceptSelf_1(nums):
    ans = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]
    sufix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= sufix
        sufix *= nums[i]
    return ans


def productArrayExceptSelf_2(nums):
    ans = len(nums)
    products = [1] * ans
    for i in range(1, ans):
        print(f'')
        products[i] = products[i-1] * nums[i-1]

    right = nums[-1]
    for i in range(ans-2, -1, -1):
        products[i] *= right
        right *= nums[i]
    return products


nums = [1, 2, 3, 4]
# print(productArrayExceptSelf(nums))
# print(productArrayExceptSelf_1(nums))
print(productArrayExceptSelf_2(nums))


def productArrayExceptSelf_2(nums):
    # Línea 1: Define una función llamada 'productArrayExceptSelf_2' que toma una lista de números 'nums' como entrada.
    # El objetivo de esta función es devolver una nueva lista 'products' donde products[i]
    # sea el producto de todos los elementos en 'nums' excepto nums[i].

    ans = len(nums)
    # Línea 2: Obtiene la longitud de la lista de entrada 'nums' y la almacena en la variable 'ans'.
    # Para nums = [2, 3, 4, 5], ans será 4.

    products = [1] * ans
    # Línea 3: Inicializa una nueva lista llamada 'products' con el mismo tamaño que 'nums'.
    # Cada elemento de 'products' se inicializa con el valor 1.
    # Esta lista es donde almacenaremos nuestros resultados finales.
    # Después de esta línea: products = [1, 1, 1, 1]

    for i in range(1, ans):
        # Línea 4: Inicia el primer bucle 'for'.
        # Este bucle va desde el índice 1 hasta 'ans - 1' (es decir, el último índice del array).
        # El objetivo de este bucle es calcular el producto de todos los elementos *a la izquierda* de cada posición 'i'.

        # i = 1:
        # products[1] = products[0] * nums[0]
        # products[1] = 1 * 2 = 2
        # products = [1, 2, 1, 1] (products[1] ahora tiene el producto de los elementos a la izquierda de nums[1], que es solo nums[0])

        # i = 2:
        # products[2] = products[1] * nums[1]
        # products[2] = 2 * 3 = 6
        # products = [1, 2, 6, 1] (products[2] ahora tiene el producto de los elementos a la izquierda de nums[2], que son nums[0]*nums[1])

        # i = 3:
        # products[3] = products[2] * nums[2]
        # products[3] = 6 * 4 = 24
        # products = [1, 2, 6, 24] (products[3] ahora tiene el producto de los elementos a la izquierda de nums[3], que son nums[0]*nums[1]*nums[2])

        products[i] = products[i-1] * nums[i-1]
        # Línea 5: En cada iteración, el elemento actual de 'products' (products[i])
        # se calcula multiplicando el elemento anterior de 'products' (products[i-1])
        # por el elemento de 'nums' que está justo a la izquierda del índice actual (nums[i-1]).
        # Al final de este bucle, products[i] contendrá el producto de todos los elementos
        # en 'nums' *antes* del índice 'i'.

    # En este punto, para nums = [2, 3, 4, 5]:
    # products = [1, 2, 6, 24]
    # products[0] = 1 (porque no hay elementos a la izquierda de nums[0])
    # products[1] = 2 (producto de [2])
    # products[2] = 6 (producto de [2, 3])
    # products[3] = 24 (producto de [2, 3, 4])

    right = nums[-1]
    # Línea 6: Inicializa una variable 'right' con el valor del último elemento de la lista 'nums'.
    # Esta variable se utilizará para acumular el producto de los elementos *a la derecha* de cada posición.
    # Para nums = [2, 3, 4, 5], right será 5.

    for i in range(ans-2, -1, -1):
        # Línea 7: Inicia el segundo bucle 'for'.
        # Este bucle itera de derecha a izquierda.
        # Va desde 'ans - 2' (el penúltimo índice) hasta 0 (el primer índice), de forma decreciente (-1).
        # El objetivo de este bucle es multiplicar los productos de la izquierda (ya calculados en 'products')
        # por los productos acumulados de la derecha.

        # i = 2 (para nums[2] = 4):
        # products[2] *= right  (products[2] = 6 * 5 = 30)
        # products = [1, 2, 30, 24]
        # right *= nums[2] (right = 5 * 4 = 20)  (acumula el producto de los elementos a la derecha de nums[2], que es solo nums[3])

        # i = 1 (para nums[1] = 3):
        # products[1] *= right (products[1] = 2 * 20 = 40)
        # products = [1, 40, 30, 24]
        # right *= nums[1] (right = 20 * 3 = 60) (acumula el producto de los elementos a la derecha de nums[1], que son nums[2]*nums[3])

        # i = 0 (para nums[0] = 2):
        # products[0] *= right (products[0] = 1 * 60 = 60)
        # products = [60, 40, 30, 24]
        # right *= nums[0] (right = 60 * 2 = 120) (acumula el producto de los elementos a la derecha de nums[0], que son nums[1]*nums[2]*nums[3])

        products[i] *= right
        # Línea 8: Multiplica el valor actual en 'products[i]' (que contiene el producto de los elementos a la izquierda)
        # por la variable 'right' (que contiene el producto acumulado de los elementos a la derecha).
        # Esto nos da el producto de todos los elementos *excepto* nums[i].

        right *= nums[i]
        # Línea 9: Actualiza la variable 'right' multiplicándola por el elemento 'nums[i]' actual.
        # Esto asegura que 'right' siempre contenga el producto de todos los elementos
        # que ya hemos procesado a la derecha del índice actual (y que serán a la derecha de los próximos índices).

    return products
    # Línea 10: Una vez que ambos bucles han terminado, la lista 'products' contiene los resultados deseados.
    # La función devuelve esta lista.

# --- Fuera de la función ---


nums = [2, 3, 4, 5]
# Línea 11: Define la lista de números de ejemplo que se pasará a la función.

# print(productArrayExceptSelf_2(nums))
# Línea 12: Llama a la función con 'nums' y imprime el resultado que devuelve.

""" class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            temp = curr.next
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr

            curr = temp
        return dummy.next


# head = [-1, 5, 3, 4, 0]

if __name__ == "__main__":
    head = ListNode(-1)
    head.next = ListNode(5)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)
    print(Solution().insertionSortList(head))
 """


# 1. Definición del Nodo (Lo que LeetCode ya tiene interno)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Función para convertir lista de Python -> Lista Enlazada


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next
    return head

# 3. Función para imprimir la lista (Para ver el resultado)


def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))

# 4. TU SOLUCIÓN (Versión con punteros)


def insertionSortList(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    dummy.next = head
    # 'last_sorted' es el final de la sección que ya está en orden
    last_sorted = head
    # 'curr' es el que vamos a intentar insertar
    curr = head.next

    while curr:
        if last_sorted.val <= curr.val:
            # ¡Perfecto! El nodo ya es mayor que el anterior.
            # Solo movemos la frontera un paso.
            last_sorted = last_sorted.next
        else:
            # Oh no, el nodo es más pequeño. Hay que buscarle sitio.
            prev = dummy
            while prev.next.val < curr.val:
                prev = prev.next

            # 1. Desconectamos 'curr' de su posición actual
            last_sorted.next = curr.next

            # 2. Lo insertamos entre 'prev' y 'prev.next'
            curr.next = prev.next
            prev.next = curr

        # El siguiente a procesar siempre será el que quedó después del 'last_sorted'
        curr = last_sorted.next

    return dummy.next


# --- PRUEBA DEL CÓDIGO ---
nums = [-1, 5, 3, 4, 0]
linked_list_head = create_linked_list(nums)

print("Lista original:")
print_list(linked_list_head)

sorted_head = insertionSortList(linked_list_head)

print("\nLista ordenada:")
print_list(sorted_head)

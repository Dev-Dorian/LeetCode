

def validParentheses(cadena):
    pila = []
    parentheses = {
        '{': '}', '(': ')', '[': ']'
    }

    for c in cadena:
        if c in parentheses:
            pila.append(c)
        # elif len(pila) == 0 or c != parentheses[pila.pop()]:
            print(pila.append(c), c, parentheses[pila.pop()])
        elif not pila or c != parentheses[pila.pop()]:
            return False
    return len(pila) == 0


print(validParentheses('([{})'))

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()

# print(stack)


def funcExpresion():
    expresion = "()()"
    parentesis_izq = expresion.count('(')
    parentesis_der = expresion.count(')')
    pilas = []
    if parentesis_izq == parentesis_der:
        for caracter in expresion:
            if caracter in ['(', ')']:
                if caracter == '(':
                    pilas.append(caracter)
                elif len(pilas) > 0:
                    pilas.pop()
        if len(pilas) == 0:
            print('La estructura esta completa')
        else:
            print('La estructura esta incompleta')
    else:
        if parentesis_izq > parentesis_der:
            print('Agrega los parentesis ")"')
        else:
            print('Agrega los parentesis "("')


funcExpresion()

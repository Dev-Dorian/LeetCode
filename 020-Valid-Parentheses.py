

def validParentheses(cadena):
    pila = []
    parentheses = {
        '{': '}', '(': ')', '[': ']'
    }

    for c in cadena:
        if c in parentheses:
            pila.append(c)
        # elif len(pila) == 0 or c != parentheses[pila.pop()]:
            # print(pila.append(c), c, parentheses[pila.pop()])
        elif not pila or c != parentheses[pila.pop()]:
            return False
    return len(pila) == 0


print(validParentheses('())'))


def getMin(s):
    # Write your code here
    ls = len(s)
    stack = []
    data = [0] * ls
    for i in range(ls):
        curr = s[i]
        if curr == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                data[i] = 1
                data[stack.pop(-1)] = 1
    tep, res = 0, 0
    for t in data:
        if t == 1:
            tep += 1
        else:
            res = max(tep, res)
            tep = 0
    return max(tep, res)


print(getMin("()("))
"""
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
"""

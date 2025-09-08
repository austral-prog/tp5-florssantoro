# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    disc = (b**2-4*a*c)
    x1 = (-b + (disc)**0.5)/2*a
    x2 = (-b - (disc)**0.5)/2*a

    if disc > 0:
        if x1 != x2:
            return (f"({x1}, {x2})")
    elif disc == 0:
        if x1 == x2:
            return (f"({x1})")
    else:
        return "( )"


"""raices = roots(int(input()),int(input()),int(input()))
print(raices)"""

def value_y(a, b, c, x):
    y = a*(x**2) + b*x + c
    return y

"""valory = value_y(int(input()),int(input()),int(input()),int(input()))
print(valory)"""


def to_string(a, b, c):
    if a == 0 and b == 0:
        funcion = f"f(x) = {c}"
    elif a == 0 and c == 0:
        funcion = f"f(x) = {b} * X"
    elif b == 0 and c == 0:
        funcion = f"f(x) = {a} * X^2"
    elif a == 0:
        funcion = f"f(x) = {b} * X + {c}"
    elif b == 0:
        funcion = f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        funcion = f"f(x) = {a} * X^2 + {b} * X"
    else:
        funcion = f"f(x) = {a} * X^2 + {b} * X + {c}"
    return funcion

"""print(to_string(int(input()), int(input()), int(input())))"""

def derivation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        derivada = f"f'(x) = 0"
    elif a == 0 and c == 0:
        derivada = f"f'(x) = {b}"
    elif b == 0 and c == 0:
        derivada = f"f'(x) = {2*a} * X"
    elif a == 0 and b == 0:
        derivada = f"f'(x) = 0"
    elif a == 0:
        derivada = f"f'(x) = {b}"
    elif b == 0:
        derivada = f"f'(x) = {2*a} * X"
    else:
        derivada = f"f'(x) = {2*a} * X + {b}"
    return derivada

"""print(derivation(int(input()), int(input()), int(input())))"""
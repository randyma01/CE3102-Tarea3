from symtable import Symbol

import sympy as sym
import numpy as np
from sympy import solve

x = sym.Symbol('x')


########################################################################################################################
# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral
# Salidas:
# valor I, el cual el resultado de la integral, er: error de aproximacion
def regla_trapecio(f, a, b):
    f1 = sym.sympify(f)
    h = b - a
    I = h / 2 * (f1.subs(x, a) + f1.subs(x, b))

    # calcula la primera derivada
    dx = sym.diff(f1, x)
    # calcula la segunda derivada
    dx2 = sym.diff(dx, x)
    # calcula la tercera derivada
    dx3 = sym.diff(dx2, x)

    # resolver f'''(x) igual a cero
    s0 = solve(dx3)

    if not s0:
        s1 = [abs(dx2.subs(x, a)), abs(dx2.subs(x, b))]
    else:
        # evaluar en la segunda derivada en valor absoluto
        s1 = [abs(dx2.subs(x, s0))]

    # Obtener el error
    er = ((b - a) ** 3) / 12 * max(s1)
    return [I, er]


########################################################################################################################
# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral, Cantidad de puntos N
# Salidas:
# lista [I,r], donde I es el resultado de la integral y er el error de aproximacion
def regla_trapecio_compuesto(f, a, b, N):
    f1 = sym.sympify(f)
    h = (b - a) / (N - 1)
    I = 0
    er = 0
    vec = np.arange(a, b + 0.1, h).tolist()

    for i in range(N - 1):
        I = I + regla_trapecio(f1, vec[i], vec[i + 1])[0]

    # calcula la primera derivada
    dx = sym.diff(f1, x)
    # calcula la segunda derivada
    dx2 = sym.diff(dx, x)
    # calcula la tercera derivada
    dx3 = sym.diff(dx2, x)

    # resolver f'''(x) igual a cero
    s0 = solve(dx3)

    if not s0:
        s1 = [abs(dx2.subs(x, a)), abs(dx2.subs(x, b))]
    else:
        # evaluar en la segunda derivada en valor absoluto
        s1 = [abs(dx2.subs(x, s0))]

    # Obtener el error
    er = ((b - a) * h ** 2) / 12 * max(s1)

    return [I, er]


########################################################################################################################
# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral
# Salidas:
# I: resultado de la integgral, er: error de aproximacion
def regla_simpson(f, a, b):
    f1 = sym.sympify(f)
    I = 0
    er = 0
    # Definir los puntos evaluables
    x1 = a
    x2 = ((a + b) / 2)
    x3 = b
    # Definir las integrales para el calculo del error.
    dx = sym.diff(f1, x)
    dx2 = sym.diff(dx, x)
    dx3 = sym.diff(dx2, x)
    dx4 = sym.diff(dx3, x)
    dx5 = sym.diff(dx4, x)

    # resolver f(5)(x) igual a cero
    s0 = solve(dx5)

    if not s0:
        s1 = [abs(dx4.subs(x, a)), abs(dx4.subs(x, b))]
    else:
        # evaluar en la cuarta derivada en valor absoluto
        s1 = [abs(dx4.subs(x, s0))]

    # Calcular el valor de la integral
    I = ((b - a) / 6) * (f1.subs(x, x1) + 4 * f1.subs(x, x2) + f1.subs(x, x3))

    # Calcular el error
    er = (((b - a) ** 5) / 2880) * max(s1)

    return [I, er]


########################################################################################################################
# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral, Cantidad de puntos N
# Salidas:
# I: resultado de la integgral, er: error de aproximacion
def regla_simpson_compuesto(f, a, b, N):
    # N debe ser impar y mayor a 5
    if N <= 5 and N % 2 == 1:
        print("El valor de m debe ser un entero impar mayor o igual a 5")
        return None
    f1 = sym.sympify(f)
    I = 0
    er = 0
    h = ((b - a) / (N - 1))
    # Definir los puntos evaluables
    vec = np.arange(a, b + 0.1, h).tolist()

    vec_par = []
    vec_impar = []
    spar = 0
    simpar = 0

    for i in range(1, N - 1):
        if i % 2 == 0:
            vec_par.append(vec[i])
            spar = spar + 1
        elif i % 2 == 1:
            vec_impar.append(vec[i])
            simpar = simpar + 1

    suma_pares = 0
    for i in range(spar):
        suma_pares = suma_pares + f1.subs(x, vec_par[i])

    suma_impares = 0
    for i in range(simpar):
        suma_impares = suma_impares + f1.subs(x, vec_impar[i])

    I = (h / 3) * (f1.subs(x, a) + 2 * suma_pares + 4 * suma_impares + f1.subs(x, b))

    # Definir las integrales para el calculo del error.
    dx = sym.diff(f1, x)
    dx2 = sym.diff(dx, x)
    dx3 = sym.diff(dx2, x)
    dx4 = sym.diff(dx3, x)
    dx5 = sym.diff(dx4, x)

    # resolver f(5)(x) igual a cero
    s0 = solve(dx5)

    if not s0:
        s1 = [abs(dx4.subs(x, a)), abs(dx4.subs(x, b))]
    else:
        # evaluar en la cuarta derivada en valor absoluto
        s1 = [abs(dx4.subs(x, s0))]

    # Calcular el error
    er = (((b - a) * h ** 4) / 180) * max(s1)

    return [I, er]


########################################################################################################################
# funcion auxiliar
def polinomio(n):
    f = (x ** 2 - 1) ** n
    k = 1
    while k <= n:
        f = sym.diff(f, x)
        k += 1
    y = f / (np.math.factorial(n) * (2 ** n))
    return y


# Entradas:
# Funcion evaluable f y grado del polinomio N
# Salidas:
# I: resultado de la integral, error de aproximacion
def cuadraturas_aux(f, N):
    f1 = sym.sympify(f)
    # P es el polinomio de grado N
    P = polinomio(N)
    # p es la derivada de P
    p = sym.diff(P, x)

    I = 0
    er = 0
    # Se ordenan las soluciones del polinomio
    S = sorted(solve(P))

    for i in range(len(S)):
        Wi = 2 / ((1 - (S[i]) ** 2) * p.subs(x, S[i]))
        I = I + (Wi * f1.subs(x, S[i]))

    return [float(I), er]


# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral y grado de P(n)
# Salidas:
# I: resultado de la integral, error de aproximacion
def cuadraturas_gausseana(f, a, b, N):
    f1 = sym.sympify(f)
    g1 = ((b - a) / 2) * f1.subs(x, ((b - a) * x + (b + a)) / 2)

    res = cuadraturas_aux(g1, N)
    I = float(res[0])
    er = res[1]

    return [float(I), er]


########################################################################################################################
# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral
# Salidas:
# valor I, el cual el resultado de la integral, er: error de aproximacion
def regla_boole(f, a, b):
    f1 = sym.sympify(f)
    N = 5
    h = (b - a) / (N - 1)

    # Definir los puntos evaluables
    vec = np.arange(a, b + 0.1, h).tolist()

    I = ((b - a) / 90) * (7 * f1.subs(x, vec[0]) + 32 * f1.subs(x, vec[1]) + 12 * f1.subs(x, vec[2])
                          + 32 * f1.subs(x, vec[3]) + 7 * f1.subs(x, vec[4]))

    # calcula la primera derivada
    dx = sym.diff(f1, x)
    # calcula la segunda derivada
    dx2 = sym.diff(dx, x)
    # calcula la tercera derivada
    dx3 = sym.diff(dx2, x)
    # calcula la cuarta derivada
    dx4 = sym.diff(dx3, x)
    # calcula la quinta derivada
    dx5 = sym.diff(dx4, x)
    # calcula la sexta derivada
    dx6 = sym.diff(dx5, x)
    # calcula la septima derivada
    dx7 = sym.diff(dx6, x)

    # resolver f(7)(x) igual a cero
    s0 = solve(dx7)

    if not s0:
        s1 = [abs(dx6.subs(x, a)), abs(dx6.subs(x, b))]
    else:
        # evaluar en la segunda derivada en valor absoluto
        s1 = [abs(dx6.subs(x, s0))]

    # Obtener el error
    er = ((b - a) / N) ** 7 * (8 / 945) * max(s1)
    return [I, er]


########################################################################################################################
# Llamados a los metodos
A = regla_trapecio('13/(7*x+11)', 1, 2)
B = regla_trapecio_compuesto('13/(7*x+11)', 1, 2, 10)
C = regla_simpson('13/(7*x+11)', 1, 2)
D = regla_simpson_compuesto('13/(7*x+11)', 1, 2, 11)
E = cuadraturas_gausseana('13/(7*x+11)', 1, 2, 10)
F = regla_boole('13/(7*x+11)', 1, 2)

# Mostrar los resultados
print("Regla Trapecio ,", "Resultado: ", A[0], "Error: ", A[1])
print("Regla Trapecio Compuesto ,", "Resultado: ", B[0], "Error: ", B[1])
print("Regla Simpson,", "Resultado: ", C[0], "Error: ", C[1])
print("Regla Simpson Compuesto,", "Resultado: ", D[0], "Error: ", D[1])
print("Cuadraturas Gausseanas,", "Resultado: ", E[0], "Error: ", E[1])
print("Regla de Boole,", "Resultado: ", F[0], "Error: ", F[1])

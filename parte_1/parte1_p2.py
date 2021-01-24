"""
Instituto Tecnológico de Costa Rica

Área Académica de Ingeniería en Computadores

Curso:
    * CE3102 - Análisis Numérico para Ingeniería

Profesor:
    * Juan Pablo Soto Quirós

Estudiantes:
    * Cristian Marín Murillo
    * Fiorella Delgado León
    * Karla Rivera Sanchez
    * Randy Martínez Sandí

Evaluación:
    * Tarea 3

Archivo:
    * parte1_p2.py: módulo de la pregunta 2 del punto 1.
    * Código de la implementación de las funciones que
    aproximan el valor de una integral.

Fecha de Entrega:
    * Miércoles 27 de enero del 2021.

Semestre:
    * Semestre II - 2020
"""

# ------------------------------------------------------------------- #
#                             librerias                               #
# ------------------------------------------------------------------- #

import numpy as np
import sympy as sym
from sympy import solve


# ------------------------------------------------------------------- #
#                         variable simbolica x                        #
# ------------------------------------------------------------------- #
x = sym.Symbol('x')


# ------------------------------------------------------------------- #
#                         regla del trapecio                          #
# ------------------------------------------------------------------- #
def regla_trapecio(f, a, b):
    """
    Recibe función evaluable 'f', valores iniciales 'a' y 'b' como
    límites de la integral.

    Realiza el cálculo de la integral 'I' mediante la Regla del Trapecio.

    Retorna el valor 'I' y el error 'er' de tal aproximación, en una lista
    como flotantes.

    :param f: string
    :param a: int
    :param b: int
    :return: [I, er]
    """
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

    # obtener el error
    er = ((b - a) ** 3) / 12 * max(s1)
    return [I, er]


# ------------------------------------------------------------------- #
#                     regla del trapecio compuesto                    #
# ------------------------------------------------------------------- #
def regla_trapecio_compuesto(f, a, b, N):
    """
    Recibe función evaluable 'f', valores iniciales 'a' y 'b' como
    límites de la integral y cantidad de puntos 'N'.

    Realiza el cálculo de la integral 'I' mediante la Regla del
    Trapecio Compuesto.

    Retorna el valor 'I' y el error 'er' de tal aproximación,
    en una lista como flotantes.

    :param f: string
    :param a: int
    :param b: int
    :param N: int
    :return: [I, er]
    """
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

    # obtener el error
    er = ((b - a) * h ** 2) / 12 * max(s1)

    return [I, er]


# ------------------------------------------------------------------- #
#                          regla de simpson                           #
# ------------------------------------------------------------------- #
def regla_simpson(f, a, b):
    """
    Recibe función evaluable 'f', valores iniciales 'a' y 'b' como
    límites de la integral.

    Realiza el cálculo de la integral 'I' mediante la Regla de Simpson.

    Retorna el valor 'I' y el error 'er' de tal aproximación, en una
    lista como flotantes.

    :param f: string
    :param a: int
    :param b: int
    :return: [I, er]
    """
    f1 = sym.sympify(f)
    I = 0
    er = 0
    # definir los puntos evaluables
    x1 = a
    x2 = ((a + b) / 2)
    x3 = b
    # definir las integrales para el calculo del error.
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

    # calcular el valor de la integral
    I = ((b - a) / 6) * (f1.subs(x, x1) + 4 * f1.subs(x, x2) + f1.subs(x, x3))

    # calcular el error
    er = (((b - a) ** 5) / 2880) * max(s1)

    return [I, er]


# ------------------------------------------------------------------- #
#                      regla de simpson compuesto                     #
# ------------------------------------------------------------------- #
def regla_simpson_compuesto(f, a, b, N):
    """
    Recibe función evaluable 'f', valores iniciales 'a' y 'b' como
    límites de la integral y cantidad de puntos 'N'.

    Realiza el cálculo de la integral 'I' mediante la Regla de
    Simpson Compuesto.

    Retorna el valor 'I' y el error 'er' de tal aproximación, en
    una lista como flotantes.

    :param f: string
    :param a: int
    :param b: int
    :param N: int
    :return: [I, er]
    """
    # N debe ser impar y mayor a 5
    if N <= 5 and N % 2 == 1:
        print("El valor de m debe ser un entero impar mayor o igual a 5")
        return None
    f1 = sym.sympify(f)
    I = 0
    er = 0
    h = ((b - a) / (N - 1))
    # definir los puntos evaluables
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

    I = (h / 3) * (f1.subs(x, a) + 2 * suma_pares +
                   4 * suma_impares + f1.subs(x, b))

    # definir las integrales para el calculo del error
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

    # calcular el error
    er = (((b - a) * h ** 4) / 180) * max(s1)

    return [I, er]


# ------------------------------------------------------------------- #
#                     cuadraturas guassianas                          #
# ------------------------------------------------------------------- #
def polinomio(n):
    """
    Devuelve un polinomio.

    :param n:
    :return: y
    """
    f = (x ** 2 - 1) ** n
    k = 1
    while k <= n:
        f = sym.diff(f, x)
        k += 1
    y = f / (np.math.factorial(n) * (2 ** n))
    return y


def cuadraturas_aux(f, N):
    """
    Recibe función evaluable 'f' y una cantidad de puntos 'N'.

    Realiza el cálculo de la integral 'I' mediante la Regla de
    las Cuadratruas Gaussianas.

    Retorna el valor 'I' y el error 'er' de tal aproximación,
    en una lista como flotantes.

    :param f: sym
    :param N: int
    :return: [I, er]
    """
    f1 = sym.sympify(f)
    # P es el polinomio de grado N
    P = polinomio(N)
    # p es la derivada de P
    p = sym.diff(P, x)

    I = 0
    er = 0
    # se ordenan las soluciones del polinomio
    S = sorted(solve(P))

    for i in range(len(S)):
        Wi = 2 / ((1 - (S[i]) ** 2) * (p.subs(x, S[i])) ** 2)
        I = I + (Wi * f1.subs(x, S[i]))

    return float(I)


def cuadraturas_gaussianas(f, a, b, N):
    """
    Recibe función evaluable 'f', valores iniciales 'a' y 'b' como
    límites de la integral y cantidad de puntos 'N'.

    Hace invocación del método cuadraturas_aux(f, N), el cual le
    envía 'f' y 'N' como parámetros. Este devuelve el valor 'I'
    de la aproximación y el error 'er', como una lista de
    flotantes.

    Retorna 'I' y 'er'.

    :param f: string
    :param a: int
    :param b: int
    :param N: int
    :return: [I, er]
    """
    f1 = sym.sympify(f)
    g1 = ((b - a) / 2) * f1.subs(x, ((b - a) * x + (b + a)) / 2)

    res = cuadraturas_aux(g1, N)
    I = float(res)

    # definir las integrales para el calculo del error
    dx = sym.diff(g1, x)
    dx2 = sym.diff(dx, x)
    dx3 = sym.diff(dx2, x)
    dx4 = sym.diff(dx3, x)
    dx5 = sym.diff(dx4, x)

    # resolver f(5)(x) igual a cero
    s0 = solve(dx5)

    if not s0:
        s1 = [abs(dx4.subs(x, -1)), abs(dx4.subs(x, 1))]
    else:
        # evaluar en la cuarta derivada en valor absoluto
        s1 = [abs(dx4.subs(x, s0))]

    # calcular el error
    er = max(s1)/135

    return [float(I), er]


# ------------------------------------------------------------------- #
#                          regla del boole                            #
# ------------------------------------------------------------------- #
def regla_boole(f, a, b):
    """
    Recibe función evaluable 'f', valores iniciales 'a' y 'b' como
    límites de la integral.

    Realiza el cálculo de la integral 'I' mediante el Regla de
    Boole.

    Retorna el valor 'I' y el error 'er' de tal aproximación, en
    una lista como flotantes.

    :param f: string
    :param a: int
    :param b: int
    :return: [I, er]
    """
    f1 = sym.sympify(f)
    N = 5
    h = (b - a) / (N - 1)

    # definir los puntos evaluables
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

    # obtener el error
    er = ((b - a) / N) ** 7 * (8 / 945) * max(s1)
    return [I, er]

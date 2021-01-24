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
        Wi = 2 / ((1 - (S[i]) ** 2) * (p.subs(x, S[i])) ** 2)
        I = I + (Wi * f1.subs(x, S[i]))

    return float(I)


# Entradas:
# Funcion evaluable f, valores iniciales a,b limites de la integral y grado de P(n)
# Salidas:
# I: resultado de la integral, error de aproximacion
def cuadraturas_gausseana(f, a, b, N):
    f1 = sym.sympify(f)
    g1 = ((b - a) / 2) * f1.subs(x, ((b - a) * x + (b + a)) / 2)

    res = cuadraturas_aux(g1, N)
    I = float(res)

    # Definir las integrales para el calculo del error.
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

    # Calcular el error
    er = max(s1)/135

    return [float(I), er]


########################################################################################################################

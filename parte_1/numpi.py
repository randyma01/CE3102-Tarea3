from sympy import *

func = 'exp(x)-x-2'
x = Symbol('x')

f1 = sympify(func)
fa = f1.subs('x', 9)
fb = f1.subs('x', 2)

print(f1.evalf(subs={'x': 2}))
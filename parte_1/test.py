from sympy import Symbol, S, exp, log, pi, sqrt, sin, tan
# from sympy import *
from sympy.sets import Interval
from sympy.calculus.util import function_range
import sympy as sym

x = Symbol('x')

f = 1/x
f_sym = sym.sympify(f)

print(f_sym)

a = 3
b = 17

print(Interval(a, b).intersection(function_range(f_sym, x, S.Reals)) != Interval(a, b))

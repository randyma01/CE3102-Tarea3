import sympy as sym

func = "13/(7x+11)"

try:
    func_sym = sym.sympify(func)
    print(func_sym)
except sym.core.SympifyError:
    print("error")
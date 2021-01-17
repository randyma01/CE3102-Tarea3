import sympy as sym
"""#x = sym.Symbol('x')

func = "13/(7*u*x+11)"

try:
    if 'x' in func:
        pass
    else:
        raise SyntaxError

    func_sym = sym.sympify(func)
    print(func_sym)

except SyntaxError:
    print("¡Error!", "La función entrada únicamente debe contener la variable 'x'.")
except Exception:
    print("¡Error!", "La sintaxis de la entrada fue incorrecto.")

new_func = (func_sym.subs(x, 2))
print(new_func)"""


func = "13/(7*u*x+11)"


def validate_variable(func):
    variables = []
    for x in func:
        if type(x) == int:
            variables.append(x)
            print(x)
    return variables


validate_variable(func)

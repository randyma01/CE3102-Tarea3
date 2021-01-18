import sympy as sym

x = sym.Symbol('x')

func = "13/(7*y*x+11)"


def have_only_x(entry):
    letter = "abcdefghijklmnopqrstuvwyz"

    for x in entry:
        if x in letter:
            print("it has invalid char:", x)
            return False
    return True


try:
    if 'x' in func and have_only_x(func):
        pass
    else:
        raise SyntaxError

    func_sym = sym.sympify(func)
    print(func_sym)
    ans = (func_sym.subs(x, 2))
    print(ans)

except SyntaxError:
    print("¡Error!", "La función entrada únicamente debe contener la variable 'x'.")
except Exception:
    print("¡Error!", "La sintaxis de la entrada fue incorrecto.")


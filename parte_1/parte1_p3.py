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
    * parte1_p3.py: módulo de la pegunta 3 del punto 1.
    * Código de la interfaz gráfica (GUI) de la calculadora.

Fecha de Entrega:
    * Miércoles 27 de enero del 2021.

Semestre:
    * Semestre II - 2020
"""
# ------------------------------------------------------------------- #
#                             libraries                               #
# ------------------------------------------------------------------- #

# methods for approx integrals#
import parte1_p2 as metodo

# gui tools #
from tkinter import *
from tkinter import ttk

# image tools #
from PIL import Image, ImageTk

# sympy and math tools #
from sympy import Symbol, S
from sympy.sets import Interval
from sympy.calculus.util import function_range
import sympy as sym

# utilizar navegador web#
import webbrowser


# ------------------------------------------------------------------- #
#                             misc funcs                              #
# ------------------------------------------------------------------- #
def load_image(file):
    """
    Receives the name of an image, loads it from the imgs/.
    Then return the image.

    :param file: string
    :return: image
    """
    load = Image.open(file)
    image = ImageTk.PhotoImage(load)
    return image


def open_documentation():
    """
    Open online documentation/manual of the program.
    """
    new = 1
    url = "https://drive.google.com/file/d/13COWbbNmauyPg5QLmRtyWObpEQR-6rnI/view?usp=sharing"

    webbrowser.open(url, new=new)


def visit_repo():
    """
    Open online repository of the source code.
    """
    new = 1
    url = "https://github.com/randyma01/CE3102-Tarea3/tree/master/parte_1"

    webbrowser.open(url, new=new)


def have_only_x(entry):
    """
    Validates that the entry must only have the char 'x',
    any other char is invalid.

    :param entry: string
    :return: boolean
    """
    alphabet = "abcdefghijklmnñopqrstuvwyzABCDEFGHIJKLMNÑOPQRSTUVWZY"

    for x in entry:
        if x in alphabet:
            print("ERROR - Carácter inválido detectado:", x)
            return False

    return True


def is_domain_valid(f, a, b):
    """
    Validates that the function's domain is continuous
    in the interval given by 'a' and 'b'.

    :param f: sym
    :param a: float
    :param b: float
    :return: boolean
    """
    x = Symbol('x')

    if Interval(a, b).intersection(function_range(f, x, S.Reals)) == Interval(a, b):
        return True

    # print("Error - La función no es continua con el dominio.")
    return False


def is_points_valid(n):
    """
    Validates that the entry must be bigger than 5 and
    odd.

    :param n: int
    :return: boolean
    """
    if n % 2 != 0 and 5 <= n:
        return True

    return False


# ------------------------------------------------------------------- #
#                             main funcs                              #
# ------------------------------------------------------------------- #
def get_func_entry():
    """
    Get entry of the value 'function'.

    If the entry is empty, show message box with error.
    If the entry is not does not contain a variable 'x',
    show message box with error.
    If the entry contains any variable rather than 'x',
    show message box with error.
    If the entry has invalid sym.sympify (symbolic) char,
    show message message box with error.

    :return: sym
    """
    func = func_entry.get()

    if func == "":
        print("Error - #1 ")
        text_error = "Error: #1. La entrada de la función no puede estar vacía."
        approx_cal_label.config(text=text_error)
        return

    try:
        if not ('x' in func):  # and have_only_x(func)):
            raise SyntaxError
        func_sym = sym.sympify(func)
        print("IMPRESIÓN - Función Simbólica:", func_sym)
        return func_sym
    except SyntaxError:
        print("Error - #2 ")
        text_error = "Error: #2. La función entrada únicamente debe contener la variable 'x'."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return
    except:
        print("Error - #3 ")
        text_error = "Error: #3. La sintaxis de la entrada fue incorrecta."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return


def get_a_entry():
    """
    Get entry of the value 'a'.

    If the entry is empty, show message box with error.
    If the entry is not an integer, show message box with error.

    :return: int
    """
    a = a_entry.get()

    if a == "" or None:
        print("Error - #4 ")
        text_error = "Error: #4. La entrada del valor 'a' no puede estar vacía."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return

    try:
        a = float(a)
        return a
    except ValueError:
        print("Error - #5 ")
        text_error = "Error: #5. La entrada del valor 'a' debe ser un número."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return


def get_b_entry():
    """
    Get entry of the value 'b'.

    If the entry is empty, show message box with error.
    If the entry is not an integer, show message box with error.

    :return: int
    """
    b = b_entry.get()

    if b == "" or None:
        print("Error - #4 ")
        text_error = "Error: #4. La entrada del valor 'a' no puede estar vacía."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return

    try:
        b = float(b)
        return b
    except ValueError:
        print("Error - #5 ")
        text_error = "Error: #5. La entrada del valor 'a' debe ser un número."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return


def get_points_entry():
    """
    Get entry of the value 'points'.

    If the entry is empty, show message box with error.
    If the entry is not an integer, show message box with error.

    :return: int
    """
    points = str(points_entry.get())

    if points == "" or None:
        print("Error - #4 ")
        text_error = "Error: #4. La entrada del valor 'a' no puede estar vacía."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return

    try:
        points = int(points)
        return points
    except ValueError:
        print("Error - #5 ")
        text_error = "Error: #5. La entrada del valor 'a' debe ser un número."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return


def method_selection():
    """
    Gets the value of the radio button selected
    for the methods.

    Sets variable 'method' with the value of
    the option selected.

    :return: method
    """
    variable = method_selected.get()
    method = ""

    if variable == 1:
        method = "trapecio"
    elif variable == 2:
        method = "simpson"
    elif variable == 3:
        method = "boole"
    elif variable == 4:
        method = "trapecio_compuesto"
    elif variable == 5:
        method = "simpson_compuesto"
    elif variable == 6:
        method = "gaussianas"

    print("IMPRESIÓN - Método seleccionado:", method)
    return method


def calculate():
    approx_cal_label.config(text="")
    error_cal_label.config(text="")
    try:
        method = method_selection()
        f = get_func_entry()
        a = get_a_entry()
        b = get_b_entry()
        print("IMPRESIÓN - Datos colectados (método, f, a, b): ",
              method, ",", f, ",", a, ",", b)

        if not is_domain_valid(f, a, b):
            print("Error - #8 ")
            text_error = "Error: #8. La función no es continua en el intervalo de intregación."
            approx_cal_label.config(text=text_error)
            error_cal_label.config(text="N/A")
            return

        if b <= a:
            print("Error - #6 ")
            text_error = "Error: #6. La entrada de 'a' no puede ser igual o mayor que la de 'b'."
            approx_cal_label.config(text=text_error)
            error_cal_label.config(text="N/A")
            return

        if method == "trapecio":
            ans = metodo.regla_trapecio(f, a, b)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])
            return

        elif method == "simpson":
            ans = metodo.regla_simpson(f, a, b)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])
            return

        elif method == "boole":
            ans = metodo.regla_boole(f, a, b)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])
            return

        elif method == "trapecio_compuesto":
            n = get_points_entry()
            ans = metodo.regla_trapecio_compuesto(f, a, b, n)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])
            return

        elif method == "simpson_compuesto":
            n = get_points_entry()
            print("IMPRESIÓN - Cantidad de Puntos: ", n)
            print(is_points_valid(n))
            if not is_points_valid(n):
                print("Error - #7 ")
                text_error = "Error: #7. La entrada del valor 'puntos' debe ser un número mayor a cinco e impar."
                approx_cal_label.config(text=text_error)
                error_cal_label.config(text="N/A")
                return

            else:
                ans = metodo.regla_simpson_compuesto(f, a, b, n)
                approx_cal_label.config(text=ans[0])
                error_cal_label.config(text=ans[1])
                return

        elif method == "gaussianas":
            n = get_points_entry()
            print("IMPRESIÓN - Cantidad de Puntos: ", n)
            ans = metodo.cuadraturas_gaussianas(f, a, b, n)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])
            return

    except:
        print("Error - #9 ")
        text_error = "Error: #9. No se posible calcular la respuesta. Vuelva a ingresar los datos."
        approx_cal_label.config(text=text_error)
        error_cal_label.config(text="N/A")
        return


# ------------------------------------------------------------------- #
#                              help window                            #
# ------------------------------------------------------------------- #
# help window #
def help_me():
    """
    About window. Contains information of the authors and link to
    see the documentation/manual of the program.
    """

    # secondary window #
    help_window = Toplevel()
    help_window.title("Guía de Uso")
    help_window.minsize(600, 500)
    help_window.resizable(width=NO, height=NO)

    # title #
    help_view = Label(help_window, text="Guía de Ayuda", font=("Times New Roman", 25))
    help_view.place(x=200, y=20)

    # version #
    help_view = Label(help_window, text="CID v.1.0.0", font=("Times New Roman", 16))
    help_view.place(x=235, y=70)

    # horizontal line 1 #
    help_line_1 = Frame(help_window, width=580, height=1, bg="black")
    help_line_1.place(x=10, y=100)

    # authors title #
    authors_title = Label(help_window, text="Autores:", font=("Times New Roman", 18))
    authors_title.place(x=250, y=125)

    # author 1 #
    authors_1 = Label(help_window, text="Cristian Marín", font=("Times New Roman", 18))
    authors_1.place(x=120, y=155)

    # author 2 #
    authors_2 = Label(help_window, text="Fiorella Delgado", font=("Times New Roman", 18))
    authors_2.place(x=320, y=155)

    # author 3 #
    authors_3 = Label(help_window, text="Karla Rivera", font=("Times New Roman", 18))
    authors_3.place(x=120, y=210)

    # author 4 #
    authors_4 = Label(help_window, text="Randy Martínez", font=("Times New Roman", 18))
    authors_4.place(x=320, y=210)

    # horizontal line 2 #
    help_line_2 = Frame(help_window, width=580, height=1, bg="black")
    help_line_2.place(x=10, y=270)

    # contact label #
    contact = Label(help_window, text="Contacto: randyma01@gmail.com", font=("Times New Roman", 18))
    contact.place(x=160, y=300)

    # warning label #
    warning = Label(help_window, text="Programa con fines académicos.", font=("Times New Roman", 18))
    warning.place(x=170, y=330)

    # horizontal line 3 #
    help_line_3 = Frame(help_window, width=580, height=1, bg="black")
    help_line_3.place(x=10, y=390)

    # documentation/manual #
    doc_button = Button(help_window, command=open_documentation, borderwidth=0, text="Ver Manual", bg="#FF0000",
                        fg="#000000", font=("Times New Roman", 20))
    doc_button.place(x=100, y=420)

    # source code #
    code_button = Button(help_window, command=visit_repo, borderwidth=0, text="Ver Código Fuente",
                         bg="#FF0000", fg="#000000", font=("Times New Roman", 20))
    code_button.place(x=300, y=420)


# ------------------------------------------------------------------- #
#                              main window                            #
# ------------------------------------------------------------------- #
# main window #
root = Tk()
root.title("ANPI")
root.geometry("1000x910")
root.minsize(1000, 910)
root.resizable(width=NO, height=NO)

# main canvas #
root_canva = Canvas(root, width=1000, height=1000, bg="#FFFFFF")
root_canva.place(x=0, y=0)

# title #
root_title = Label(root_canva, text="Calculadora de Integrales Definidas", bg="#FFFFFF", fg="#000000",
                   font=("Times New Roman", 25))
root_title.place(x=320, y=25)

# image integrals #
image_integ = load_image("imgs/integ_1.png")
img = Label(root_canva, image=image_integ, bg="#FFFFFF")
img.place(x=330, y=65)

# ------------------------------------------------------------------- #
#                               entries                               #
# ------------------------------------------------------------------- #
# function entry #
func_label = Label(root_canva, text="f (x) = ", bg="#FFFFFF", fg="#000000",
                   font=("Times New Roman", 18))
func_label.place(x=330, y=170)
func_entry = Entry(root_canva, width=25, bg="#FFFFFF", fg="#000000")
func_entry.place(x=400, y=170)

# limit a entry #
a_label = Label(root_canva, text="a =", bg="#FFFFFF", fg="#000000",
                font=("Times New Roman", 18))
a_label.place(x=350, y=230)
a_entry = Entry(root_canva, width=5, bg="#FFFFFF", fg="#000000")
a_entry.place(x=400, y=230)

# limit b entry #
b_label = Label(root_canva, text="b =", bg="#FFFFFF", fg="#000000",
                font=("Times New Roman", 18))
b_label.place(x=500, y=230)
b_entry = Entry(root_canva, width=5, bg="#FFFFFF", fg="#000000")
b_entry.place(x=550, y=230)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 1 #
line_1 = Frame(root_canva, width=980, height=1, bg="black")
line_1.place(x=10, y=280)

# ------------------------------------------------------------------- #
#                               tabs                                  #
# ------------------------------------------------------------------- #
# tabs #
tab_control = ttk.Notebook(root_canva, width=500, height=250)
tab_control.place(x=230, y=300)

# variable for selecting the radio button #
method_selected = IntVar()

# ------------------------------------------------------------------- #
#                           simple methods                            #
# ------------------------------------------------------------------- #
# tab for simple methods #
sim_tab = Frame(tab_control, bg="#FFFFFF")
tab_control.add(sim_tab, text='Métodos Simples')

# simple trap radio button#
sim_trap = Radiobutton(sim_tab, command=method_selection, variable=method_selected, text="Trapecio",
                       bg="#FFFFFF", value=1)
sim_trap.place(x=200, y=50)

# simple simp radio button #
sim_simp = Radiobutton(sim_tab, command=method_selection, variable=method_selected, text="Simpson",
                       bg="#FFFFFF", value=2)
sim_simp.place(x=200, y=100)

# boole radio button #
sim_boole = Radiobutton(sim_tab, command=method_selection, variable=method_selected, text="Regla de Boole",
                        bg="#FFFFFF", value=3)
sim_boole.place(x=200, y=150)

# ------------------------------------------------------------------- #
#                             comp methods                            #
# ------------------------------------------------------------------- #
# tabs for comp methods #
comp_tab = Frame(tab_control, bg="#FFFFFF")
tab_control.add(comp_tab, text='Métodos Compuestos')

# comp trap radio button#
comp_trap = Radiobutton(comp_tab, command=method_selection, variable=method_selected, text="Trapecio Compuesto",
                        bg="#FFFFFF", value=4)
comp_trap.place(x=70, y=50)

# comp simp radio button #
comp_simp = Radiobutton(comp_tab, command=method_selection, variable=method_selected, text="Simpson Compuesto",
                        bg="#FFFFFF", value=5)
comp_simp.place(x=70, y=100)

# cuad gaus radio button #
cuad_gau = Radiobutton(comp_tab, command=method_selection, variable=method_selected, text="Cuadraturas Gaussianas",
                       bg="#FFFFFF", value=6)
cuad_gau.place(x=70, y=150)

# points entry #
points_label = Label(comp_tab, text="Puntos a Utilizar =",
                     bg="#FFFFFF", fg="#000000")
points_label.place(x=280, y=100)
points_entry = Entry(comp_tab, width=5, bg="#FFFFFF", fg="#000000")
points_entry.place(x=400, y=100)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 2 #
line_2 = Frame(root_canva, width=980, height=1, bg="black")
line_2.place(x=10, y=630)

# ------------------------------------------------------------------- #
#                              calculator                             #
# ------------------------------------------------------------------- #
# calculate button #
calculate_button = Button(root_canva, command=calculate, borderwidth=0, text="Calcular", bg="#FF0000", fg="#FF0000",
                          font=("Times New Roman", 20))
calculate_button.place(x=440, y=650)

# approximation label #
approx_title_label = Label(root_canva, text="Aproximación =", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 18))
approx_title_label.place(x=240, y=700)

# calculated answer label #
approx_cal_label = Label(root_canva, bg="#FFFFFF", fg="#000000",
                         font=("Times New Roman", 18))
approx_cal_label.place(x=375, y=700)

# error label #
error_title_label = Label(root_canva, text="Error =", bg="#FFFFFF", fg="#000000",
                          font=("Times New Roman", 18))
error_title_label.place(x=305, y=750)

# calculated error label #
error_cal_label = Label(root_canva, bg="#FFFFFF", fg="#000000",
                        font=("Times New Roman", 18))
error_cal_label.place(x=375, y=750)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 2 #
line_2 = Frame(root_canva, width=980, height=1, bg="black")
line_2.place(x=10, y=830)

# ------------------------------------------------------------------- #
#                             help window                             #
# ------------------------------------------------------------------- #
# help button #
help_button = Button(root_canva, command=help_me, text="Ayuda", borderwidth=0, bg="#FFFFFF", fg="#0000FF",
                     font=("Times New Roman", 20))
help_button.place(x=445, y=850)

# ------------------------------------------------------------------- #
#                               mainloop                              #
# ------------------------------------------------------------------- #
if __name__ == '__main__':
    root.mainloop()

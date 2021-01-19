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

import parte1_p2 as metodo
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sympy as sym


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
        messagebox.showinfo(
            "Error: #1", "La entrada de la función no puede estar vacía.")
        return

    try:
        if not('x' in func and have_only_x(func)):
            raise SyntaxError
        func_sym = sym.sympify(func)
        print("IMPRESIÓN - Función Simbólica:", func_sym)
        return func_sym
    except SyntaxError:
        messagebox.showinfo(
            "Error: #2", "La función entrada únicamente debe contener la variable 'x'.")
    except:
        messagebox.showinfo(
            "Error: #3", "La sintaxis de la entrada fue incorrecta.")


def get_a_entry():
    """
    Get entry of the value 'a'.

    If the entry is empty, show message box with error.
    If the entry is not an integer, show message box with error.

    :return: int
    """
    a = a_entry.get()

    if a == "" or None:
        messagebox.showinfo(
            "Error: #4", "La entrada del valor 'a' no puede estar vacía.")
        return

    try:
        a = int(a)
        return a
    except ValueError:
        messagebox.showinfo(
            "Error: #5", "La entrada del valor 'a' debe ser un número entero.")


def get_b_entry():
    """
    Get entry of the value 'b'.

    If the entry is empty, show message box with error.
    If the entry is not an integer, show message box with error.

    :return: int
    """
    b = b_entry.get()

    if b == "" or None:
        messagebox.showinfo(
            "Error: #4", "La entrada del valor 'b' no puede estar vacía.")
        return

    try:
        b = int(b)
        return b
    except ValueError:
        messagebox.showinfo(
            "Error: #5", "La entrada del valor 'b' debe ser un número entero.")


def get_points_entry():
    """
    Get entry of the value 'points'.

    If the entry is empty, show message box with error.
    If the entry is not an integer, show message box with error.

    :return: int
    """
    points = str(points_entry.get())

    if points == "" or None:
        messagebox.showinfo(
            "Error: #4", "La entrada de 'Puntos a Utilizar' no puede estar vacía.")
        return

    try:
        points = int(points)
        return points
    except ValueError:
        messagebox.showinfo(
            "Error: #5", "La entrada del valor 'Puntos a Utilizar' debe ser un número entero.")


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
    try:
        method = method_selection()
        f = get_func_entry()
        a = get_a_entry()
        b = get_b_entry()
        print("IMPRESIÓN - Datos colectados (método, f, a, b): ",
              method, ",", f, ",", a, ",", b)

        if b <= a:
            raise ValueError

        if method == "trapecio":
            ans = metodo.regla_trapecio(f, a, b)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])

        elif method == "simpson":
            ans = metodo.regla_simpson(f, a, b)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])

        elif method == "boole":
            ans = metodo.regla_boole(f, a, b)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])

        # TODO: Validación de metodo que solo recibe una cantidad impar de puntos. #

        elif method == "trapecio_compuesto":
            n = get_points_entry()
            ans = metodo.regla_trapecio_compuesto(f, a, b, n)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])

        elif method == "simpson_compuesto":
            n = get_points_entry()
            ans = metodo.regla_simpson_compuesto(f, a, b, n)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])

        elif method == "gaussianas":
            n = get_points_entry()
            ans = metodo.cuadraturas_gaussianas(f, a, b, n)
            approx_cal_label.config(text=ans[0])
            error_cal_label.config(text=ans[1])
    except ValueError:
        messagebox.showinfo(
            "Error: #6", "La entrada de 'a' no puede ser igual o mayor que la de 'b'.")
    except:
        print("EXCEPCIÓN - Error en la ejecucción de métodos.")
        pass


# ------------------------------------------------------------------- #
#                              help window                            #
# ------------------------------------------------------------------- #
# help window #
def help_me():
    """
    TODO: Realizar ventana de ayuda.
    """
    # secondary window #
    help_window = Toplevel()
    help_window.title("Guía de Uso")
    help_window.minsize(500, 600)
    help_window.resizable(width=NO, height=NO)

    help_canva = Canvas(help_window, width=500, height=600, bg="#FFFFFF")
    help_canva.place(x=0, y=0)

    # title #
    help_view = Label(help_canva, text="Guía de Ayuda", bg="#FFFFFF", fg="#000000",
                      font=("Times New Roman", 25))
    help_view.place(x=170, y=25)

    print("Help me!")


# ------------------------------------------------------------------- #
#                              main window                            #
# ------------------------------------------------------------------- #
# main window #
root = Tk()
root.title("ANPI")
root.geometry("800x900")
root.minsize(800, 900)
root.resizable(width=NO, height=NO)

# main canvas #
root_canva = Canvas(root, width=800, height=900, bg="#FFFFFF")
root_canva.place(x=0, y=0)

# title #
root_title = Label(root_canva, text="Calculadora de Integrales Definidas", bg="#FFFFFF", fg="#000000",
                   font=("Times New Roman", 25))
root_title.place(x=220, y=25)

# image integrals #
image_integ = load_image("imgs/integ_1.png")
img = Label(root_canva, image=image_integ, bg="#FFFFFF")
img.place(x=230, y=65)

# ------------------------------------------------------------------- #
#                               entries                               #
# ------------------------------------------------------------------- #
# function entry #
func_label = Label(root_canva, text="f (x) = ", bg="#FFFFFF", fg="#000000",
                   font=("Times New Roman", 18))
func_label.place(x=230, y=170)
func_entry = Entry(root_canva, width=25, bg="#FFFFFF", fg="#000000")
func_entry.place(x=300, y=170)

# limit a entry #
a_label = Label(root_canva, text="a =", bg="#FFFFFF", fg="#000000",
                font=("Times New Roman", 18))
a_label.place(x=250, y=230)
a_entry = Entry(root_canva, width=5, bg="#FFFFFF", fg="#000000")
a_entry.place(x=300, y=230)

# limit b entry #
b_label = Label(root_canva, text="b =", bg="#FFFFFF", fg="#000000",
                font=("Times New Roman", 18))
b_label.place(x=400, y=230)
b_entry = Entry(root_canva, width=5, bg="#FFFFFF", fg="#000000")
b_entry.place(x=450, y=230)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 1 #
line_1 = Frame(root_canva, width=780, height=1, bg="black")
line_1.place(x=10, y=280)

# ------------------------------------------------------------------- #
#                               tabs                                  #
# ------------------------------------------------------------------- #
# tabs #
tab_control = ttk.Notebook(root_canva, width=500, height=250)
tab_control.place(x=130, y=300)

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
line_2 = Frame(root_canva, width=780, height=1, bg="black")
line_2.place(x=10, y=630)

# ------------------------------------------------------------------- #
#                              calculator                             #
# ------------------------------------------------------------------- #
# calculate button #
calculate_button = Button(root_canva, command=calculate, borderwidth=0, text="Calcular", bg="#FF0000", fg="#FF0000",
                          font=("Times New Roman", 20))
calculate_button.place(x=340, y=650)

# approximation label #
approx_title_label = Label(root_canva, text="Aproximación =", bg="#FFFFFF", fg="#000000",
                           font=("Times New Roman", 18))
approx_title_label.place(x=220, y=700)

# calculated answer label #
approx_cal_label = Label(root_canva, bg="#FFFFFF", fg="#000000",
                         font=("Times New Roman", 18))
approx_cal_label.place(x=345, y=700)

# error label #
error_title_label = Label(root_canva, text="Error =", bg="#FFFFFF", fg="#000000",
                          font=("Times New Roman", 18))
error_title_label.place(x=285, y=750)

# calculated error label #
error_cal_label = Label(root_canva, bg="#FFFFFF", fg="#000000",
                        font=("Times New Roman", 18))
error_cal_label.place(x=345, y=750)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 2 #
line_2 = Frame(root_canva, width=780, height=1, bg="black")
line_2.place(x=10, y=830)

# ------------------------------------------------------------------- #
#                             help window                             #
# ------------------------------------------------------------------- #
# help button #
help_button = Button(root_canva, command=help_me, text="Ayuda", borderwidth=0, bg="#FFFFFF", fg="#0000FF",
                     font=("Times New Roman", 20))
help_button.place(x=345, y=850)

# ------------------------------------------------------------------- #
#                               mainloop                              #
# ------------------------------------------------------------------- #
if __name__ == '__main__':
    root.mainloop()

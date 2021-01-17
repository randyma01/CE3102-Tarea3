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


# TODO: corregir posibles errores a la hora de obtener la funcion #
def get_func_entry():
    func = func_entry.get()

    if func == "":
        messagebox.showinfo("¡Error!", "La entrada de la función no puede estar vacía.")
        return
    try:
        func_sym = sym.sympify(func)
    except SyntaxError:
        messagebox.showinfo("¡Error!", "La sintaxis de la entrada fue incorrecto. ")

    return func_sym


def get_a_entry():
    """
    Get entry of the value 'a'.

    If the entry is empty, show message box with error.
    If the entry is not a integer, show message box with error.

    :return: int
    """
    a = a_entry.get()

    if a == "":
        messagebox.showinfo("¡Error!", "La entrada del valor 'a' no puede estar vacía.")
        return

    try:
        a = int(a)
    except ValueError:
        messagebox.showinfo("¡Error!", "La entrada del valor 'a' debe ser un número entero.")
        return

    return a


def get_b_entry():
    """
    Get entry of the value 'b'.

    If the entry is empty, show message box with error.
    If the entry is not a integer, show message box with error.

    :return: int
    """
    b = b_entry.get()

    if b == "":
        messagebox.showinfo("¡Error!", "La entrada del valor 'b' no puede estar vacía.")
        return

    try:
        b = int(b)
    except ValueError:
        messagebox.showinfo("¡Error!", "La entrada del valor 'b' debe ser un número entero.")
        return

    return b


def get_points_entry():
    """
    Get entry of the value 'points'.

    If the entry is empty, show message box with error.
    If the entry is not a integer, show message box with error.

    :return: int
    """
    points = str(points_entry.get())

    if points == "":
        messagebox.showinfo("¡Error!", "La entrada de 'Puntos a Utilizar' no puede estar vacía.")
        return

    try:
        points = int(points)
    except ValueError:
        messagebox.showinfo("¡Error!", "La entrada del valor 'b' debe ser un número entero.")
        return

    return points


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

    print(method)
    return method


def calculate():
    method = method_selection()
    f = get_func_entry()
    a = get_a_entry()
    b = get_b_entry()

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

    # TODO: Validacion de metodo que solo recibe una cantidad impar de puntos #

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
        ans = metodo.cuadraturas_gausseana(f, a, b, n)
        approx_cal_label.config(text=ans[0])
        error_cal_label.config(text=ans[1])

    return


# ------------------------------------------------------------------- #
#                              help window                            #
# ------------------------------------------------------------------- #
# help window #
def help_me():
    """
    Printing function
    """
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
main_canva = Canvas(root, width=800, height=900, bg="#FFFFFF")
main_canva.place(x=0, y=0)

# title #
root_title = Label(main_canva, text="Calculadora de Integrales Definidas", bg="#FFFFFF", fg="#000000",
                   font=("Courier", 25, "bold"))
root_title.place(x=150, y=25)

# image integrals #
image_integ = load_image("imgs/integ_1.png")
img = Label(main_canva, image=image_integ, bg="#FFFFFF")
img.place(x=230, y=65)

# ------------------------------------------------------------------- #
#                               entries                               #
# ------------------------------------------------------------------- #
# function entry #
func_label = Label(main_canva, text="f(x)= ", bg="#FFFFFF", fg="#000000",
                   font=("Courier", 18))
func_label.place(x=230, y=170)
func_entry = Entry(main_canva, width=25, bg="#FFFFFF", fg="#000000")
func_entry.place(x=300, y=170)

# limit a entry #
a_label = Label(main_canva, text="a =", bg="#FFFFFF", fg="#000000",
                font=("Courier", 18))
a_label.place(x=250, y=230)
a_entry = Entry(main_canva, width=5, bg="#FFFFFF", fg="#000000")
a_entry.place(x=300, y=230)

# limit b entry #
b_label = Label(main_canva, text="b =", bg="#FFFFFF", fg="#000000",
                font=("Courier", 18))
b_label.place(x=400, y=230)
b_entry = Entry(main_canva, width=5, bg="#FFFFFF", fg="#000000")
b_entry.place(x=450, y=230)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 1 #
line_1 = Frame(main_canva, width=780, height=1, bg="black")
line_1.place(x=10, y=280)

# ------------------------------------------------------------------- #
#                               tabs                                  #
# ------------------------------------------------------------------- #
# tabs #
tab_control = ttk.Notebook(main_canva, width=500, height=250)
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
points_label = Label(comp_tab, text="Puntos a Utilizar =", bg="#FFFFFF", fg="#000000")
points_label.place(x=280, y=100)
points_entry = Entry(comp_tab, width=5, bg="#FFFFFF", fg="#000000")
points_entry.place(x=400, y=100)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 2 #
line_2 = Frame(main_canva, width=780, height=1, bg="black")
line_2.place(x=10, y=630)

# ------------------------------------------------------------------- #
#                              calculator                             #
# ------------------------------------------------------------------- #
# calculate button #
calculate_button = Button(main_canva, command=calculate, borderwidth=0, text="Calcular", bg="#FFFFFF", fg="#0000FF",
                          font=("Courier", 20, "italic"))
calculate_button.place(x=340, y=650)

# approximation label #
approx_title_label = Label(main_canva, text="Aproximación =", bg="#FFFFFF", fg="#000000",
                           font=("Courier", 18))
approx_title_label.place(x=150, y=700)

# calculated answer label #
approx_cal_label = Label(main_canva, bg="#FFFFFF", fg="#000000",
                         font=("Courier", 18))
approx_cal_label.place(x=345, y=700)

# error label #
error_title_label = Label(main_canva, text="Error =", bg="#FFFFFF", fg="#000000",
                          font=("Courier", 18))
error_title_label.place(x=150, y=750)

# calculated error label #
error_cal_label = Label(main_canva, bg="#FFFFFF", fg="#000000",
                        font=("Courier", 18))
error_cal_label.place(x=345, y=750)

# ------------------------------------------------------------------- #
#                           division line                             #
# ------------------------------------------------------------------- #
# horizontal line 2 #
line_2 = Frame(main_canva, width=780, height=1, bg="black")
line_2.place(x=10, y=830)

# ------------------------------------------------------------------- #
#                             help window                             #
# ------------------------------------------------------------------- #
# help button #
help_button = Button(main_canva, command=help_me, text="Ayuda", borderwidth=0, bg="#FFFFFF", fg="#FF0000",
                     font=("Courier", 20, "italic"))
help_button.place(x=345, y=850)

# ------------------------------------------------------------------- #
#                               mainloop                              #
# ------------------------------------------------------------------- #
if __name__ == '__main__':
    root.mainloop()

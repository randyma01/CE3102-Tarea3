"""
TODO: Encabezado
"""

# ------------------------------------------------------------------- #
#                             libraries                               #
# ------------------------------------------------------------------- #

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from sympy import *


# ------------------------------------------------------------------- #
#                             misc funcs                              #
# ------------------------------------------------------------------- #

def load_image(file):
    """
    Loads and return the image.
    :param file: name of the image
    :return: image
    """
    load = Image.open(file)
    image = ImageTk.PhotoImage(load)
    return image


# ------------------------------------------------------------------- #
#                             misc funcs                              #
# ------------------------------------------------------------------- #

def help_me():
    """
    Printing function
    """
    print("Help me!")


def get_a_entry():
    """
    Get entry a.
    :return: A
    """
    a = str(a_entry.get())
    return a


def get_b_entry():
    """
    Get entry b.
    :return: b
    """
    b = str(b_entry.get())
    return b


def get_func_entry():
    if func_entry.get() == "":
        f1_eval = "Entry is empty."
    else:
        func = str(func_entry.get())
        f1 = sympify(func)
        f1_eval = str(f1.evalf(subs={'x': 2}))
    return f1_eval


def get_entry_po():
    """
    Get entry b.
    :return: b
    """
    b = str(b_entry.get())
    return b


def get_points_entry():
    """
    Get entry points.
    :return: points
    """
    points = points_entry.get()
    return points


# ############## #
def simp_selection():
    variable = simp_var.get()
    option = ""
    if variable == 1:
        option = "trapecio"
    elif variable == 2:
        option = "simpson"
    elif variable == 3:
        option = "boole"

    selection = " Opción seleccionada: " + option
    simp_sel_label.config(text=selection)


# ############## #


# ############## #
def comp_selection():
    variable = comp_var.get()
    option = ""
    if variable == 1:
        option = "trapecio compuesto"
    elif variable == 2:
        option = "simpson compuesto"
    elif variable == 3:
        option = "cuadraturas gaussianas"

    selection = " Opción seleccionada: " + option
    comp_sel_label.config(text=selection)


# ############## #


# ############## #
def show():
    f1 = get_func_entry()
    ans_label.config(text=f1)
    err_label.config(text="Error Label")
# ############## #


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

# ------------------------------------------------------------------- #
#                           simple methods                            #
# ------------------------------------------------------------------- #
# variable for control #
simp_var = IntVar()

# tab for simple methods #
sim_tab = Frame(tab_control, bg="#FFFFFF")
tab_control.add(sim_tab, text='Métodos Simples')

# simple trap radio button#
sim_trap = Radiobutton(sim_tab, command=simp_selection, variable=simp_var, text="Trapecio", bg="#FFFFFF", value=1)
sim_trap.place(x=200, y=50)

# simple simp radio button #
sim_simp = Radiobutton(sim_tab, command=simp_selection, variable=simp_var, text="Simpson", bg="#FFFFFF", value=2)
sim_simp.place(x=200, y=100)

# boole radio button #
sim_boole = Radiobutton(sim_tab, command=simp_selection, variable=simp_var, text="Regla de Boole", bg="#FFFFFF",
                        value=3)
sim_boole.place(x=200, y=150)

# ############## #
simp_sel_label = Label(tab_control, bg="#FFFFFF")
simp_sel_label.place(x=200, y=250)
# ############## #

# ------------------------------------------------------------------- #
#                             comp methods                            #
# ------------------------------------------------------------------- #
# variable for control #
comp_var = IntVar()

# tabs for comp methods #
comp_tab = Frame(tab_control, bg="#FFFFFF")
tab_control.add(comp_tab, text='Métodos Compuestos')

# comp trap radio button#
comp_trap = Radiobutton(comp_tab, command=comp_selection, variable=comp_var, text="Trapecio Compuesto", bg="#FFFFFF",
                        value=1)
comp_trap.place(x=70, y=50)

# comp simp radio button #
comp_simp = Radiobutton(comp_tab, command=comp_selection, variable=comp_var, text="Simpson Compuesto", bg="#FFFFFF",
                        value=2)
comp_simp.place(x=70, y=100)

# cuad gaus radio button #
cuad_gau = Radiobutton(comp_tab, command=comp_selection, variable=comp_var, text="Cuadraturas Gaussianas", bg="#FFFFFF",
                       value=3)
cuad_gau.place(x=70, y=150)

# points entry #
points_label = Label(comp_tab, text="Puntos a Utilizar =", bg="#FFFFFF", fg="#000000")
points_label.place(x=280, y=100)
points_entry = Entry(comp_tab, width=5, bg="#FFFFFF", fg="#000000")
points_entry.place(x=400, y=100)

# ############## #
comp_sel_label = Label(tab_control, bg="#FFFFFF")
comp_sel_label.place(x=200, y=250)
# ############## #


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
calculate_button = Button(main_canva, command=show, borderwidth=0, text="Calcular", bg="#FFFFFF", fg="#0000FF",
                          font=("Courier", 20, "italic"))
calculate_button.place(x=340, y=650)

# approximation label #
approx_label = Label(main_canva, text="Aproximación =", bg="#FFFFFF", fg="#000000",
                     font=("Courier", 18))
approx_label.place(x=150, y=700)

# calculated answer label #
ans_label = Label(main_canva, bg="#FFFFFF", fg="#000000",
                  font=("Courier", 18))
ans_label.place(x=345, y=700)

# error label #
error_label = Label(main_canva, text="Error =", bg="#FFFFFF", fg="#000000",
                    font=("Courier", 18))
error_label.place(x=150, y=750)

# calculated error label #
err_label = Label(main_canva, bg="#FFFFFF", fg="#000000",
                  font=("Courier", 18))
err_label.place(x=345, y=750)

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

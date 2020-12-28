"""
TODO: Encabezado
"""

# ------------------------------------------------------------------- #
#                             libraries                               #
# ------------------------------------------------------------------- #

from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from sympy import *


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


def get_func_entry():
    """
    Get the entry of the 'function' as a string. Validates it.
    Then return it as a symbolic function, using sympify()
    from Sympy.

    If the entry is invalid, show message box.

    Restriction: Only accepts functions with the variable 'x'.
    :return: symbolic
    """
    func = str(func_entry.get())
    if func == "":
        messagebox.showinfo("¡Error!", "La entrada de la función no puede estar vacía.")
        return
    f_x = sympify(func)
    return f_x


def get_a_entry():
    """
    Get entry of the value 'a' as a string. Validates it. Then return it as
    a integer.

    If the entry is invalid, show message box.
    :return: int
    """
    a = str(a_entry.get())
    if a == "":
        messagebox.showinfo("¡Error!", "La entrada del valor 'a' no puede estar vacía.")
        return
    a = int(a)
    return a


def get_b_entry():
    """
    Get entry of the value 'b' as a string. Validates it. Then return it as
    a integer.

    If the entry is invalid, show message box.
    :return: int
    """
    b = str(b_entry.get())
    if b == "":
        messagebox.showinfo("¡Error!", "La entrada del valor 'b' no puede estar vacía.")
        return
    b = int(b)
    return b


def get_points_entry():
    """
    Get entry of the value 'points' as a string. Validates it. Then return it as
    a integer.

    If the entry is invalid, show message box.
    :return: int
    """
    points = str(b_entry.get())
    if points == "":
        messagebox.showinfo("¡Error!", "La entrada de 'Puntos a Utilizar' no puede estar vacía.")
        return
    points = int(points)
    return points


def simp_selection():
    variable = simp_var.get()
    f_x = get_func_entry()
    a = get_a_entry()
    b = get_b_entry()
    """if variable == 1:
        ans = parte1_p2.trapecio(f_x, a, b)
        show_results(ans[0], ans[1]) 
        return
    elif variable == 2:
        ans = parte1_p2.simpson(f_x, a, b)
        show_results(ans[0], ans[1]) 
        return
    elif variable == 3:
        ans = parte1_p2.boole(f_x, a, b)
        show_results(ans[0], ans[1])
        return"""


def comp_selection():
    variable = simp_var.get()
    f_x = get_func_entry()
    a = get_a_entry()
    b = get_b_entry()
    points = get_points_entry()
    """if variable == 1:
            ans = parte1_p2.trapecio_compuesto(f_x, a, b, points)
            show_results(ans[0], ans[1]) 
            return
        elif variable == 2:
            ans = parte1_p2.simpson_compuesto(f_x, a, b, points)
            show_results(ans[0], ans[1]) 
            return
        elif variable == 3:
            ans = parte1_p2.caudraturas_gaussianas(f_x, a, b, points)
            show_results(ans[0], ans[1]) 
            return"""


def show_results(approx, error):
    """
    Display in the main window the values of the approximation and error
    result inside each corresponding label.
    :param approx: int
    :param error: int
    :return: None
    """
    app_label.config(text=approx)
    err_label.config(text=error)


# ############## #
def show():
    f1 = get_func_entry()
    temp = f1.evalf(subs={'x': 2})
    app_label.config(text=temp)

# ############## #


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
                        value=4)
comp_trap.place(x=70, y=50)

# comp simp radio button #
comp_simp = Radiobutton(comp_tab, command=comp_selection, variable=comp_var, text="Simpson Compuesto", bg="#FFFFFF",
                        value=5)
comp_simp.place(x=70, y=100)

# cuad gaus radio button #
cuad_gau = Radiobutton(comp_tab, command=comp_selection, variable=comp_var, text="Cuadraturas Gaussianas", bg="#FFFFFF",
                       value=6)
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
calculate_button = Button(main_canva, command=show, borderwidth=0, text="Calcular", bg="#FFFFFF", fg="#0000FF",
                          font=("Courier", 20, "italic"))
calculate_button.place(x=340, y=650)

# approximation label #
approx_label = Label(main_canva, text="Aproximación =", bg="#FFFFFF", fg="#000000",
                     font=("Courier", 18))
approx_label.place(x=150, y=700)

# calculated answer label #
app_label = Label(main_canva, bg="#FFFFFF", fg="#000000",
                  font=("Courier", 18))
app_label.place(x=345, y=700)

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

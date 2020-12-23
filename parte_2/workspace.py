from tkinter import *
import sys

"""
TODO: 
"""


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title('ANPI')
        self.root.minsize(800, 800)
        self.root.geometry('800x800')
        # self.root.mainloop()
        self.root.resizable(width=NO, height=NO)

        root_canva = Canvas(self.root, width=1000, height=800, bg='#FFFFFF')
        root_canva.place(x=0, y=0)

        root_title = Label(root_canva, text='Calculadora de Integrales Definidas', fg='#000000', bg='#FFFFFF',
                           font=("Courier", 25))
        root_title.place(x=125, y=25)

        def exit_calc(self):
            return sys.exit()

        exit_button = Button(root_canva, command=exit_calc, text="SALIDA", bg="#FFFFFF", fg="#000000",
                             font=("Courier", 20))
        exit_button.place(x=345, y=475)


if __name__ == '__main__':
    master = Tk()
    calc = Calculator(master)
    master.mainloop()

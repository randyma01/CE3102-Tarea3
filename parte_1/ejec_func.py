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
    * ejec_func.py: ejecuciones de las funciones del módulo
    parte1_p2.py

Fecha de Entrega:
    * Miércoles 27 de enero del 2021.

Semestre:
    * Semestre II - 2020
"""

# ------------------------------------------------------------------- #
#                             librerias                               #
# ------------------------------------------------------------------- #

import parte1_p2 as metodo

# ------------------------------------------------------------------- #
#                      ejecuccion de las funcs                        #
# ------------------------------------------------------------------- #
# funciones #
A = metodo.regla_trapecio('13/(7*x+11)', 1, 2)
B = metodo.regla_trapecio_compuesto('13/(7*x+11)', 1, 2, 10)
C = metodo.regla_simpson('13/(7*x+11)', 1, 2)
D = metodo.regla_simpson_compuesto('13/(7*x+11)', 1, 2, 11)
E = metodo.cuadraturas_gaussianas('13/(7*x+11)', 1, 2, 10)
F = metodo.regla_boole('13/(7*x+11)', 1, 2)

# impresion de los resultados #
print("---------------------------------------------------------------------------------------------")
print("Regla Trapecio =>", "Resultado: ", A[0], "Error: ", A[1])
print("---------------------------------------------------------------------------------------------")
print("Regla Trapecio Compuesto =>", "Resultado: ", B[0], "Error: ", B[1])
print("---------------------------------------------------------------------------------------------")
print("Regla Simpson =>", "Resultado: ", C[0], "Error: ", C[1])
print("---------------------------------------------------------------------------------------------")
print("Regla Simpson Compuesto =>", "Resultado: ", D[0], "Error: ", D[1])
print("---------------------------------------------------------------------------------------------")
print("Cuadraturas Gaussianas =>", "Resultado: ", E[0], "Error: ", E[1])
print("---------------------------------------------------------------------------------------------")
print("Regla de Boole =>", "Resultado: ", F[0], "Error: ", F[1])
print("---------------------------------------------------------------------------------------------")


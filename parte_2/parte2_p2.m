pkg load symbolic;
warning('off','all');

%Instituto Tecnol�gico de Costa Rica

%�rea Acad�mica de Ingenier�a en Computadores

%Curso:
%    * CE3102 - An�lisis Num�rico para Ingenier�a

%Profesor:
%    * Juan Pablo Soto Quir�s

%Estudiantes:
%    * Cristian Mar�n Murillo
%    * Fiorella Delgado Le�n
%    * Karla Rivera Sanchez
%    * Randy Mart�nez Sand�

%Evaluaci�n:
%    * Tarea 3

%Archivo:
%    * parte2_p2.m: script de la pregunta 2 del punto 2.
    
%Fecha de Entrega:
%    * Mi�rcoles 27 de enero del 2021.

%Semestre:
%    * Semestre II - 2020


% Funcion dependiente de x que multiplica al y'
p = '-1/x';
% Funcion dependiente de x que multiplica al y
q = '1/(4*(x^2))-1';
% Funcion dependiente de x
f = '0';
% N�mero de puntos
N = 8;
% Valor inicial del intervalo
a = 1;
% Valor final del intervalo
b = 6;
% Valor inicial y0
y0 = 1;
% Valor inicial yn
yn = 0;

[x,y,pn] = edo2(p, q, f, N, a, b, y0, yn);
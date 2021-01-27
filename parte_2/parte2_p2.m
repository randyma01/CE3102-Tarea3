pkg load symbolic;
warning('off','all');

%Instituto Tecnológico de Costa Rica

%Área Académica de Ingeniería en Computadores

%Curso:
%    * CE3102 - Análisis Numérico para Ingeniería

%Profesor:
%    * Juan Pablo Soto Quirós

%Estudiantes:
%    * Cristian Marín Murillo
%    * Fiorella Delgado León
%    * Karla Rivera Sanchez
%    * Randy Martínez Sandí

%Evaluación:
%    * Tarea 3

%Archivo:
%    * parte2_p2.m: script de la pregunta 2 del punto 2.
    
%Fecha de Entrega:
%    * Miércoles 27 de enero del 2021.

%Semestre:
%    * Semestre II - 2020


% Funcion dependiente de x que multiplica al y'
p = '-1/x';
% Funcion dependiente de x que multiplica al y
q = '1/(4*(x^2))-1';
% Funcion dependiente de x
f = '0';
% Número de puntos
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
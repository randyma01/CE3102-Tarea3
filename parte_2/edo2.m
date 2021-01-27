%Función edo2(p, q, f, N, a, b, y0, yn)

%Entradas:
%   p: funcion dependiente de x que multiplica al y'
%   q: funcion dependiente de x que multiplica al y
%   f: funcion dependiente de x
%   N: número de puntos
%   a: valor inicial del intervalo
%   b: valor final del intervalo
%   y0: valor inicial y0
%   yn: valor inicial yn

%Salidas:
%   x: es el vector que contiene los puntos x
%   y: es el vector que contiene los puntos y
%   pn: polinomio de interpolación

function [x,y,pn] = edo2(p, q, f, N, a, b, y0, yn)
    
    syms x;
    
    % Cálculo de la constante h
    h = (b-a) / N;
    
    % Creación de los puntos dentro del intervalo [a,b]
    % para formar el vector de las x
    x0= a;
    for(i=1:1:N-1)
        x(i) = x0 + i * h;
    end
    
    p = sym(p);
    q = sym(q);
    f = sym(f);
    
    % Cálculo del primer elemento de los vectores m y n
    m(1) =  2 + (h^2 * subs(q,x(1)));
    n(1) = ((h/2) * subs(p,x(1)))-1;

    % Cálculo de valor de e0 y el primer elemento del vector d
    e0 = (((h/2) * subs(p,x(1)))+1) * y0;
    d(1) = -h^2 * subs(f,x(1)) + e0;
    
    % Ciclo iterativo para formar los vectores de las diagonales
    for (i=2:1:N-1)
    
        % Cálculo del último elemento de cada vector
        if (i == N-1)
            l(i-1) = ((-h/2) * subs(p,x(i)))-1;
            m(i) = 2 + h^2 * subs(q,x(i));
            en = ((-h/2) * subs(p,x(i))+1) * yn;
            d(i) = (-h^2 * subs(f,x(i))) + en;
        end 
        
        % Cálculo de todos los elementos de los vectores, menos el último 
        % y menos los primeros de los vectores m y n
        l(i-1) = ((-h/2) * subs(p,x(i)))-1;
        m(i) = 2 + h^2 * subs(q,x(i));
        n(i) = (h/2) * subs(p,x(i))-1;
        d(i) = -h^2 * subs(f,x(i));
    end
    
    % Se forma la matriz A
    for (i=1:1:N-2)
    
        if (i == N-2)
            A(i+1,i+1)= m(i+1);
        end
        % Diagonal de A con los m elementos
        A(i,i)= m(i);
        % Linea debajo de diagonal de A con l elementos
        A(i+1,i) = l(i);
        % Linea arriba de diagonal de A con n elementos
        A(i,i+1) = n(i);
    end
    
    % Agregar el valor 0 al inicio del vector de la diagonal inferior
    l = [0 l];
    
    % Agregar el valor 0 al final del vector de la diagonal superior
    n = [n 0];
    
    % Calculo del yector y, ingresando a Thomas la matriz A
    % y el vector d
    y = thomas(A,d);
    
    % Calculo del polinomio de interpolación y 
    % visualización de la gráfica del polinomio
    pn = lagrange(x,y);
    
end
% Funcion Metodo de Thomas para resolver sistema de ecuaciones  
% de forma Ax=d
%
% A: Matriz de coeficientes de entrada, debe ser tridiagonal
% d: vector de constantes del sistema de ecuaciones
%
% x: vector resultante con los valores del sistema

function x = thomas(A, d)
    [m, n] = size(A);
    
    % Verifica si matriz no es cuadrada
    if (m != n)
        display("La matriz A no es cuadrada")
        x = 0;
        return;
    end
       
    
    % Verifica si matriz no es invertible
    if(det(A) == 0)
        display("La matriz A no es invertible")
        x = 0;
        return;
    end
    
    % Fila debado de la diagonal con un 0 en la primer posicion
    a = [0];
    % Con el 0, le agrega los demas valores
    a = [a diag(A, -1)'];
    
    % Diagonal
    b = [diag(A)'];
    
    % Fila arriba de la diagonal con un 0 en la ultima posicion
    c = [diag(A, 1)'];
    % Le agrega el 0 al final
    c = [c 0];
    
    % Valores iniciales de p y q
    p(1) = c(1) / b(1);
    q(1) = d(1) / b(1);
    
    % Iteracion a partir de i=2 para valores de p y q
    for (i = 2 : n)
        p(i) = c(i)/ (b(i) - a(i) * p(i - 1));
        q(i) = (d(i) - a(i) * q(i - 1)) / (b(i) - a(i) * p(i - 1));
    end
    
    % Ultimo elemento de vector resultante x
    x(n) = q(n);

    % Iteracion decreciente para valores de vector resultante x
    for (i = n - 1 : -1 : 1)
        x(i) = q(i) - p(i)*x(i+1);
    end
    
end
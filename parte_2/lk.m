function L = lk(vx,k)
    syms x;
    n = length(vx) - 1;
    L = 1;
    
    
    % Se define la variable "x" de tipo simbólico
    % Se define el grado del polinomio (n)
    % Se define el valor inicial del polinomio "L" (neutro multiplicativo = 1)
    
    for j = 0 : n
        if j ~= k
            L = L*(x - vx(j + 1))/(vx(k+1) - vx(j+1));
        end
    end
    L = simplify(L);
end
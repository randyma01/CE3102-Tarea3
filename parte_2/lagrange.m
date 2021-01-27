%Funci�n lagrange(vx,vy)

%Entradas:
%   vx: es el vector que contiene los puntos x
%   vy: es el vector que contiene los puntos y

%Salidas:
%   La funci�n retorna el polinomio que pasa por los puntos que fueron descritos con el 
%   vector vx y vy.
%   Retorna sim, que esto es el polinomio simplificado
pkg load symbolic

%Faltan las condiciones de las x

function pn = lagrange(vx,vy)

    % Se define la variabla "x" de tipo simb�lico
    % Se define el grado del polinomio (n)
    % Se define el valor inicial del polinomio (neutro aditivo = 0)
    syms x;
    n = length(vx) - 1;
    pn = 0;
    
    
    % Condici�n por si ambos vectores son de diferente tama�o
    
    if length(vx) ~= length (vy)
        print ("Los dos vectores deben contener el mismo numero de elementos");
    end
    

    
    % Si ambos vectores est�n bien, se calcula el polinomio que pasa por los puntos
    % pn: polinomio que pasa por los puntos
    
    for k=0:n
        pn = pn + vy(k+1)*lk(vx,k);
    end
    
    % Se simplifica el polinomio y se pone 
    p = matlabFunction(simplify(sym(pn)));
    
    % Distancia entre los puntos para graficar el polinomio de interpolaci�n
    h = 0.01; 
    
    % Valor inicial del vector de las x
    x1= 1;
    
    % Definici�n del vector de las x, para graficar el polinomio
    x=zeros(1,500);
    
    % Definici�n del vector de las x, para graficar el polinomio
    y=zeros(1,500);
    
    % Definir i = 1
    i= 1;
    
    % Ciclo para completar el vector de las "x" y de las "y", con una distancia de h
    while x1< 6
    
      % Guardar la x en el vector de las "x"
      x(i)= x1; 
      
      % Evaluaci�n de la x actual en el polinomio de interpolaci�n
      % para completar el vector de las y
      y(i) = p(x1);
      
      % Incrementar el �ndice para el ciclo
      i = i +1;
      
      % Actualizar el valor de las x por x+h
      x1=x1+h;
      
    end

    % Gr�fico del polinomio de interpolaci�n
    plot (x(1:501),y(1:501));
    xlabel("X");
    ylabel("P(x)");
    title("Polinomio de interpolacion");
    
    pn = simplify(pn);   

end
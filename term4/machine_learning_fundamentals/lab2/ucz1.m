function [ Wpo ] = ucz1 ( Wprzed , P , T , n )
liczbaPrzykladow = size ( P , 2 ) ;
W = Wprzed;
wspUcz = 0.1; beta = 5;

for i = 1 : n ,
  nrPrzykladu = randi ( liczbaPrzykladow ) ;

  X = P ( : , nrPrzykladu ) ;
  Y = dzialaj1 ( W , X ) ;

  D = T ( : , nrPrzykladu ) - Y ;
  E = D .* beta.*Y.*(1-Y) ;

  % oblicz poprawki wag
  dW = wspUcz * X * D' ;

  % dodaj poprawki do wag
  W = W + dW ;
end
Wpo = W ;


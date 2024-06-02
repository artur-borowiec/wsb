function [ Y ] = dzialaj1 ( W , X )

beta = 5;
U = W' * X;
Y = 1 ./ ( 1 + exp ( -beta * U ) ) ;


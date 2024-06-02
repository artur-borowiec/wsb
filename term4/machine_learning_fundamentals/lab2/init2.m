function [ W1 , W2 ] = init2 ( S , K1 , K2 )
% funkcja tworzy sieæ dwuwarstwow¹
% i wype³nia jej macierze wag wartoœciami losowymi
% z zakresu od -0.1 do 0.1
% parametry: S – liczba wejœæ do sieci / liczba wejœæ warstwy 1
% K1 – liczba neuronów w warstwie 1
% K2 – liczba neuronów w warstwie 2 / liczba wyjœæ sieci
% wynik: W1 – macierz wag warstwy 1 sieci
% W2 – macierz wag warstwy 2 sieci

W1 = rand( S+1, K1 ) * 0.2 -0.1;
W2 = rand( K1+1, K2 ) * 0.2 - 0.1;



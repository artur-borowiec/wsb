function [ W1 , W2 ] = init2 ( S , K1 , K2 )
% funkcja tworzy sie� dwuwarstwow�
% i wype�nia jej macierze wag warto�ciami losowymi
% z zakresu od -0.1 do 0.1
% parametry: S � liczba wej�� do sieci / liczba wej�� warstwy 1
% K1 � liczba neuron�w w warstwie 1
% K2 � liczba neuron�w w warstwie 2 / liczba wyj�� sieci
% wynik: W1 � macierz wag warstwy 1 sieci
% W2 � macierz wag warstwy 2 sieci

W1 = rand( S+1, K1 ) * 0.2 -0.1;
W2 = rand( K1+1, K2 ) * 0.2 - 0.1;



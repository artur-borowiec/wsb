P = [ 4 2 -1 ; % we 1 - ile ma nóg
0.01 -1 3.5 ; % we 2 - czy ¿yje w wodzie
0.01 2 0.01 ; % we 3 - czy umie lataæ
-1 2.5 -2 ; % we 4 - czy ma pióra
-1.5 2 1.5 ] % we 5 - czy jest jajorodny

% ¿¹dane wyjœcia sieci:
T = [ 1 0 0 ; % ssak
0 1 0 ; % ptak
0 0 1 ] % ryba

Wprzed = init1 ( 5 , 3 )
Yprzed = dzialaj1 ( Wprzed , P )

Wpo = ucz1 ( Wprzed , P , T , 100 )
Ypo = dzialaj1 ( Wpo , P )


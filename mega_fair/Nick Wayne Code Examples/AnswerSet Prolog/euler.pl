%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%problem 1
% num(1..999).
% p1a(X) :- num(X), #mod(X,3,0).
% p1a(X) :- num(X), #mod(X,5,0).
% p1b(X) :- #sum{Y : p1a(Y)} = X.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%problem 2
% #maxint=100000000.
% num(3..1000).
% fib(1, 1).
% fib(2, 2).
% fib(X, Y) :- num(X),
%              B1 = X-1,
%              B2 = X-2,
%              fib(B1, E),
%              fib(B2, R),
%              Y = E + R,
%              Y < 4000000.
% fin(T) :- #sum{Y : fib(X,Y), #mod(Y, 2, 0)} = T.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%problem 3


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%problem 9
#maxint = 10000000.
num(1..700).
pyth(A, B, C) :- num(A),num(B),num(C),
                 T1 = A * A,
                 T2 = B * B,
                 T3 = C * C,
                 T3 = T1 + T2.

total(A, B, C) :- pyth(A, B, C),
                  T1 = A + B,
                  T2 = T1 + C,
                  T2 = 1000,
                  A < B,
                  B < C.

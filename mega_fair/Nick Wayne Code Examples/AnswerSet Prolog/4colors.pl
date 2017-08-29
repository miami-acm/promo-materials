country(por). country(spa). country(fra). country(ita).
country(swi). country(lux). country(bel). country(hol).
borders(fra, spa).
borders(por, spa).
borders(fra, ita).
borders(fra, swi).
borders(fra, bel).
borders(fra, lux).
borders(ita, swi).
borders(lux, bel).
borders(bel, hol).

color(X, green) | color(X, red) | color(X, blue) :- country(X).
:- borders(X, Y), color(X, C), color(Y, C).

response(unknown). 
response(rarely). 
response(no). 
response(yes). 
response(sometimes). 

types(animal). 
types(vegetable). 
types(mineral). 
types(concept). 
types(unknown). 

ans(q9, no). 
ans(q4, no). 
ans(q5, no). 
ans(q3, no). 
ans(q1, no). 

amount(X, Y) :- name(X), #count{Q : ans(Q, A), answer(X, Q, A)} = Y. 

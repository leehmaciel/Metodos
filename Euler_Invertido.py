from mpmath import *
from sympy import *

entrada = "0 0 0.1 20 1-t+4*y"

aux = entrada.split()

y0= sympify(aux[0])
t0= sympify(aux[1])
h= sympify(aux[2])
n= sympify(aux[3])
funct= sympify(aux[4])
y = symbols("y")
t = symbols("t")

for x in range(1, n+1):
	y_prox = y0 + funct.subs([(y, y0), (t, t0)]) *h 
	y_prox = y0 + funct.subs([(y, y_prox), (t, t0+h)]) * h
	y0 = y_prox
	t0 = t0 + h
	print (str(x) + '. ' + str(y_prox))

from mpmath import *
from sympy import *
class Euler_Aprimorado:

	def __init__(self, info):
		self.entrada = info

	def method(self):	
		aux = self.entrada

		y0= sympify(aux[0])
		t0= sympify(aux[1])
		h= sympify(aux[2])
		n= sympify(aux[3])
		funct= sympify(aux[4])
		y = symbols("y")
		t = symbols("t")

		for x in range(1, n+1):
			resul = funct.subs([(y, y0), (t, t0)])
			resul2 = funct.subs([(y, resul*h + y0), (t, t0+h)])
			y_prox = y0 + (h/2)*(resul + resul2)
			y0 = y_prox
			t0 = t0 + h
			print (str(x) + '. ' + str(y_prox))

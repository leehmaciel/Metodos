from mpmath import *
from sympy import *
class Runge_Kutta:

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
			k1 = funct.subs([(y, y0), (t, t0)])
			k2 = funct.subs([(y, y0 + 0.5*h*k1), (t, t0 + 0.5*h)])
			k3 = funct.subs([(y, y0 + 0.5*h*k2), (t, t0 + 0.5*h)])
			k4 = funct.subs([(y, y0 + h*k3), (t, t0+h)])
			y_prox = y0 + (h/6)*(k1+ 2*k2 + 2*k3 + k4)
			y0 = y_prox
			t0 = t0+h
			print (str(x) + '. ' + str(y_prox))

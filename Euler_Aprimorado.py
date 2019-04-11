from mpmath import *
from sympy import *
class Euler_Aprimorado:

	def __init__(self, info):
		self.entrada = info

	def method(self):	
		aux = self.entrada

		y0= sympify(aux[1])
		t0= sympify(aux[2])
		h= sympify(aux[3])
		n= sympify(aux[4])
		funct= sympify(aux[5])
		y = symbols("y")
		t = symbols("t")
		f=[0.0]

		print("Metodo Euler Aprimorado")
		print("y(" + str(t0) + ") = " + str(y0) )
		print("h = "+ str(round(h,2)))

		for x in range(0, n+1):
			resul = funct.subs([(y, y0), (t, t0)])
			resul2 = funct.subs([(y, resul*h + y0), (t, t0+h)])
			y_prox = y0 + (h/2)*(resul + resul2)
			f.append(y_prox)
			print (str(x) + '. ' + str(f[x]))
			y0 = y_prox
			t0 = t0 + h


from mpmath import *
from sympy import *
class Multon_Euler_Aprimorado:

	def __init__(self, info):
		self.entrada = info

	def ordem2(self, t0, k, h, n, f, funct): #k=1
		y_prox = symbols("y_prox")
		y = symbols("y")
		t = symbols("t")

		for x in range(k, n+1):
			resul = 0.5*funct.subs([(y, y_prox), (t, t0)])
			resul2 = 0.5*funct.subs([(y, f[0]), (t, t0 + h)])
			teste = f[1] + h*(resul - resul2) - y_prox
			teste = solve(teste, y_prox)
			f[0] = f[1]
			f[1] = teste[0]
			print(str(x)+'. '+ str(f[1]))
			t0 = t0 + h

	def ordem3(self, t0, k, h, n, f, funct): #k=2
		y_prox = symbols("y_prox")
		y = symbols("y")
		t = symbols("t")

		for x in range(k, n+1):
			resul = (5./12.)*funct.subs([(y, y_prox), (t, t0)])
			resul2 = (2./3.)*funct.subs([(y, f[1]), (t, t0 + h)])
			resul3 = (1./12.)*funct.subs([(y, f[0]), (t, t0 + 2*h)])
			teste = f[2] + h*(resul + resul2 - resul3) - y_prox
			teste = solve(teste,y_prox)
			f[0] = f[1]
			f[1] = f[2]
			f[2] = teste[0]
			print(str(x)+'. '+ str(f[2]))
			t0 = t0 + h

	def ordem4(self, t0, k, h, n, f, funct): #k=3
		y_prox = symbols("y_prox")
		y = symbols("y")
		t = symbols("t")

		for x in range(k, n+1):
			resul = (3./8.)*funct.subs([(y, y_prox), (t, t0)])
			resul2 = (19./24.)*funct.subs([(y, f[2]), (t, t0 + h)])
			resul3 = (5./24.)*funct.subs([(y, f[1]), (t, t0 + 2*h)])
			resul4 = (1./24.)*funct.subs([(y, f[0]), (t, t0 + 3*h)])
			teste = f[3] + h*(resul + resul2 - resul3 + resul4) - y_prox
			teste = solve(teste, y_prox)
			f[0] = f[1]
			f[1] = f[2]
			f[2] = f[3]
			f[3] = teste[0]
			print(str(x)+'. '+ str(f[3]))
			t0 = t0 + h

	def ordem5(self, t0, k, h, n, f, funct): #k=4
		y_prox = symbols("y_prox")
		y = symbols("y")
		t = symbols("t")

		for x in range(k, n+1):
			resul = (251./720.)*funct.subs([(y, y_prox), (t, t0)])
			resul2 = (323./360.)*funct.subs([(y, f[3]), (t, t0 + h)])
			resul3 = (11./30.)*funct.subs([(y, f[2]), (t, t0 + 2*h)])
			resul4 = (53./360.)*funct.subs([(y, f[1]), (t, t0 + 3*h)])
			resul5 = (19./720.)*funct.subs([(y, f[0]), (t, t0  + 4*h)])
			teste = f[3] + h*(resul + resul2 - resul3 + resul4 - resul5) - y_prox
			teste = solve(teste, y_prox)
			f[0] = f[1]
			f[1] = f[2]
			f[2] = f[3]
			f[3] = f[4]
			f[4] = teste[0]
			print(str(x)+'. '+ str(f[4]))
			t0 = t0 + h

	def ordem6(self, t0, k, h, n, f, funct):  #k=5
		y_prox = symbols("y_prox")
		y = symbols("y")
		t = symbols("t")

		for x in range(k, n):
			resul = (95./288.)*funct.subs([(y, y_prox), (t, t0)])
			resul2 = (1427./1440.)*funct.subs([(y, f[4]), (t, t0 + h)])
			resul3 = (133./240.)*funct.subs([(y, f[3]), (t, t0 + 2.*h)])
			resul4 = (241./720.)*funct.subs([(y, f[2]), (t, t0 + 3.*h)])
			resul5 = (173./1440.)*funct.subs([(y, f[1]), (t, t0 + 4.*h)])
			resul6 = (3./160.)*funct.subs([(y, f[0]), (t, t0 + 5.*h)])
			teste = f[4] + h*(resul + resul2 - resul3 + resul4 - resul5 + resul6) - y_prox
			teste= solve(teste, y_prox)
			f[0] = f[1]
			f[1] = f[2]
			f[2] = f[3]
			f[3] = f[4]
			f[4] = f[5]
			f[5] = teste[0]
			print(str(x+1)+'. '+ str(f[5]))
			t0 = t0 + h

	def ordem7(self, t0, k, h, n, f, funct):  #k=6
		y_prox = symbols("y_prox")
		y = symbols("y")
		t = symbols("t")

		for x in range(k, n+1):
			resul = (19087./60480.)* funct.subs([(y, y_prox), (t, t0 + h)])
			resul2 = (2713./2520.)*funct.subs([(y, f[5]), (t, t0)])
			resul3 = -(15487./20160.)*funct.subs([(y, f[4]), (t, t0 - h)])
			resul4 = (586./945.)*funct.subs([(y, f[3]), (t, t0 - 2*h)])
			resul5 = -(6737./20160.)*funct.subs([(y, f[2]), (t, t0 - 3*h)])
			resul6 = (263./2520.)*funct.subs([(y, f[1]), (t, t0 - 4*h)])
			resul7 = -(863./60480.)*funct.subs([(y, f[0]), (t, t0  - 5*h)])
			teste = f[5] + h*(resul + resul2 - resul3 + resul4 - resul5 + resul6 - resul7) - y_prox
			teste = solve(teste, y_prox)
			f[0] = f[1]
			f[1] = f[2]
			f[2] = f[3]
			f[3] = f[4]
			f[4] = f[5]
			f[5] = f[6]
			f[6] = teste[0]
			print(str(x)+'. '+ str(f[6]))
			t0 = t0 + h

	def method(self):	
		aux = self.entrada
	
		y0= sympify(aux[1])
		t0= sympify(aux[2])
		h= sympify(aux[3])
		n= sympify(aux[4])
		funct= sympify(aux[5])
		k = sympify(aux[6])
		y = symbols("y")
		t = symbols("t")
		f = [0.0]

		print("Metodo Multon by Euler Aprimorado")
		print("y(" + str(t0) + ") = " + str(y0) )
		print("h = "+ str(round(h,2)))

		#Conseguir todos os f por Euler
		for x in range(0, k):
			resul = funct.subs([(y, y0), (t, t0)])
			resul2 = funct.subs([(y, resul*h + y0), (t, t0+h)])
			y_prox = y0 + (h/2)*(resul + resul2)
			f.append(y_prox)
			print(str(x)+'. '+str(f[x]))
			y0 = y_prox
			t0 = t0 + h


		if(k==1):
			self.ordem2(t0, k, h, n, f, funct)

		elif(k==2):
			self.ordem3(t0, k, h, n, f, funct)

		elif(k==3):
			self.ordem4(t0, k, h, n, f, funct)

		elif(k==4):
			self.ordem5(t0, k, h, n, f, funct)

		elif(k==5):
			self.ordem6(t0, k, h, n, f, funct)

		elif(k==6):
			self.ordem7(t0, k, h, n, f, funct)
			
		elif(k>=7):
			print("Error")
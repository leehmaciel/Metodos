from mpmath import *
from sympy import *

entrada = "0 0 0.1 20 1-t+4*y 6"


def ordem2(t0, k, h, n, f, funct):
	for x in range(0, n+1):
		resul = funct.subs([(y, f[0]), (t, t0)])
		y_prox = f[0] + h*resul
		f[0] = y_prox
		print(y_prox)
		t0 = t0 + h

def ordem3(t0, k, h, n, f, funct):
	for x in range(1, n+1):
		resul = 3*funct.subs([(y, f[1]), (t, t0)])
		resul2 = funct.subs([(y, f[0]), (t, t0 -h)])
		y_prox = f[1] + (h/float(12))*(resul - resul2)
		f[0] = f[1]
		f[1] = y_prox
		print(y_prox)
		t0 = t0 + h

def ordem4(t0, k, h, n, f, funct):
	for x in range(1, n+1):
		resul = (23/12)*funct.subs([(y, f[2]), (t, t0)])
		resul2 = (16/12)*funct.subs([(y, f[1]), (t, t0 - h)])
		resul3 = (5/12)*funct.subs([(y, f[0]), (t, t0 - 2*h)])
		y_prox = f[2] + h*(resul - resul2 + resul3)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = y_prox
		print(y_prox)
		t0 = t0 + h

def ordem5(t0, k, h, n, f, funct):
	for x in range(1, n+1):
		resul = 55*funct.subs([(y, f[3]), (t, t0)])
		resul2 = 59*funct.subs([(y, f[2]), (t, t0-h)])
		resul3 = 37*funct.subs([(y, f[1]), (t, t0 - 2*h)])
		resul4 = 9*funct.subs([(y, f[0]), (t, t0 - 3*h)])
		y_prox = f[3] + (h/float(24))*(resul - resul2 + resul3 - resul4)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = f[3]
		f[3] = y_prox
		t0 = t0 + h

def ordem6(t0, k, h, n, f, funct):
	#print("Entrei aq")
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x2 in range(k+1, n+1):
		resul = (1901)*funct.subs([(y, f[4]), (t, t0)])
		resul2 = (2774)*funct.subs([(y, f[3]), (t, t0 - h)])
		resul3 = (2616)*funct.subs([(y, f[2]), (t, t0 - 2*h)])
		resul4 = (1274)*funct.subs([(y, f[1]), (t, t0 - 3*h)])
		resul5 = (251)*funct.subs([(y, f[0]), (t, t0  - 4*h)])
		y_prox = f[4] + (h/float(720))*(resul - resul2 + resul3 - resul4 + resul5)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = f[3]
		f[3] = f[4]
		f[4] = y_prox
		print(str(x2)+'. '+ str(y_prox))
		t0 = t0 + h


aux = entrada.split()

y0= sympify(aux[0])
t0= sympify(aux[1])
h= sympify(aux[2])
n= sympify(aux[3])
funct= sympify(aux[4])
k = sympify (aux[5])
y = symbols("y")
t = symbols("t")
f = []

#Conseguir todos os f por Euler
for x in range(1, k+1):
	resul = funct.subs([(y, y0), (t, t0)])
	y_prox = y0 + (h* resul)
	f.append(y_prox)
	#print(f)
	y0 = y_prox
	t0 = t0 + h


if(k==1):
	#Quando a ordem for 1, Euler
	print(f[0])

elif(k==2):
	#Quando a ordem for 2
	
	ordem2(t0, k, h, n, f, funct)

elif(k==3):
	#Quando a ordem for 3
	ordem3(t0, k, h, n, f, funct)

elif(k==4):
	#Quando a ordem for 4
	ordem4(t0, k, h, n, f, funct)

elif(k==5):
	#Quando a ordem for 5
	ordem5(t0, k, h, n, f, funct)

elif(k==6):
	ordem6(t0, k, h, n, f, funct)

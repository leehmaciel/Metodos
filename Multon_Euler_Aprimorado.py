from mpmath import *
from sympy import *

entrada = "0 0 0.1 20 1-t+4*y 6"

def ordem1(t0, k, h, n, f, funct): #k=1
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x in range(1, n+1):
		resul = funct.subs([(y, f[1]), (t, t0+h)])
		resul2 = funct.subs([(y, f[0]), (t, t0)])
		y_prox = f[1] + (h/float(2))*(resul - resul2)
		f[0] = f[1]
		f[1] = y_prox
		print(str(x)+'. '+ str(y_prox))
		t0 = t0 + h

def ordem2(t0, k, h, n, f, funct): #k=2
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x in range(1, n+1):
		resul = 5*funct.subs([(y, f[2]), (t, t0 + h)])
		resul2 = 8*funct.subs([(y, f[1]), (t, t0)])
		resul3 = funct.subs([(y, f[0]), (t, t0 - h)])
		y_prox = f[2] + (h/float(12))*(resul + resul2 - resul3)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = y_prox
		print(str(x)+'. '+ str(y_prox))
		t0 = t0 + h

def ordem3(t0, k, h, n, f, funct): #k=3
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x in range(k, n+1):
		resul = 9*funct.subs([(y, f[3]), (t, t0 + h)])
		resul2 = 19*funct.subs([(y, f[2]), (t, t0)])
		resul3 = 5*funct.subs([(y, f[1]), (t, t0 - h)])
		resul4 = funct.subs([(y, f[0]), (t, t0 - 2*h)])
		y_prox = f[3] + (h/float(24))*(resul + resul2 - resul3 + resul4)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = f[3]
		f[3] = y_prox
		print(str(x)+'. '+ str(y_prox))
		t0 = t0 + h

def ordem4(t0, k, h, n, f, funct): #k=4
	#print("Entrei aq")
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x in range(k+1, n+1):
		resul = 251*funct.subs([(y, f[4]), (t, t0+h)])
		resul2 = 646*funct.subs([(y, f[3]), (t, t0)])
		resul3 = 264*funct.subs([(y, f[2]), (t, t0 - h)])
		resul4 = 106*funct.subs([(y, f[1]), (t, t0 - 2*h)])
		resul5 = 19*funct.subs([(y, f[0]), (t, t0  - 3*h)])
		y_prox = f[4] + (h/float(720))*(resul + resul2 - resul3 + resul4 - resul5)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = f[3]
		f[3] = f[4]
		f[4] = y_prox
		print(str(x)+'. '+ str(y_prox))
		t0 = t0 + h

def ordem5(t0, k, h, n, f, funct):  #k=5
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x in range(k, n+1):
		resul = 475*funct.subs([(y, f[5]), (t, t0 + h)])
		resul2 = 1427*funct.subs([(y, f[4]), (t, t0)])
		resul3 = 798*funct.subs([(y, f[3]), (t, t0 - h)])
		resul4 = 482*funct.subs([(y, f[2]), (t, t0 - 2*h)])
		resul5 = 173*funct.subs([(y, f[1]), (t, t0 - 3*h)])
		resul6 = 27*funct.subs([(y, f[0]), (t, t0  - 4*h)])
		y_prox = f[5] + (h/float(1440))*(resul + resul2 - resul3 + resul4 - resul5 + resul6)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = f[3]
		f[3] = f[4]
		f[4] = f[5]
		f[5] = y_prox
		print(str(x)+'. '+ str(y_prox))
		t0 = t0 + h

def ordem6(t0, k, h, n, f, funct): #k=6
	y_prox = symbols("y_prox")
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))

	for x in range(k, n+1):
		resul = 19087* funct.subs([(y, f[6]), (t, t0 + h)])
		resul2 = (2713*24)*funct.subs([(y, f[5]), (t, t0)])
		resul3 = (15487*3)*funct.subs([(y, f[4]), (t, t0 - h)])
		resul4 = (586*64)*funct.subs([(y, f[3]), (t, t0 - 2*h)])
		resul5 = (6737*3)*funct.subs([(y, f[2]), (t, t0 - 3*h)])
		resul6 = (263*24)*funct.subs([(y, f[1]), (t, t0 - 4*h)])
		resul7 = 863*funct.subs([(y, f[0]), (t, t0  - 5*h)])
		y_prox = f[6] + (h/float(60480))*(resul + resul2 - resul3 + resul4 - resul5 + resul6 - resul7)
		f[0] = f[1]
		f[1] = f[2]
		f[2] = f[3]
		f[3] = f[4]
		f[4] = f[5]
		f[5] = f[6]
		f[6] = y_prox
		print(str(x)+'. '+ str(y_prox))
		t0 = t0 + h

def ordem7(t0, k, h, n, f, funct): #k=7
	for x in range (0, k):
		print(str(x)+'. '+str(f[x]))



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
for x in range(1, k+2):
	resul = funct.subs([(y, y0), (t, t0)])
	resul2 = funct.subs([(y, resul*h + y0), (t, t0+h)])
	y_prox = y0 + (h/2)*(resul + resul2)
	f.append(y_prox)
	#print(f)
	y0 = y_prox
	t0 = t0 + h


if(k==1):
	#Quando a ordem for 1, Euler
	ordem1(t0, k, h, n, f, funct)

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

elif(k==7):
	ordem7(t0, k, h, n, f, funct)
from mpmath import *
from sympy import *
from Euler import Euler
from Euler_Aprimorado import Euler_Aprimorado
from Euler_Inverso import Euler_Inverso
from Runge_Kutta import Runge_Kutta
from Bashforth import Bashforth
from Bashforth_Euler import Bashforth_Euler
from Bashforth_Euler_Aprimorado import Bashforth_Euler_Aprimorado
from Bashforth_Euler_Inverso import Bashforth_Euler_Inverso
from Bashforth_RungeKutta import Bashforth_RungeKutta
from Multon_Euler import Multon_Euler
from Multon_Euler_Inverso import Multon_Euler_Inverso
from Multon_Euler_Aprimorado import Multon_Euler_Aprimorado
from Multon_RungeKutta import Multon_RungeKutta


def main():
	#out = open('out_put.txt', 'a') 
	#out.close()

	with open('input.txt') as arquivo:
		for line in arquivo:
			in_put = line
			in_put = in_put.split()
			
			if(in_put[0] == "euler"):
				metodo = Euler(in_put)
				print("\n")

			if(in_put[0] == "euler_inverso"):
				metodo = Euler_Inverso(in_put)
				print("\n")

			if(in_put[0] == "euler_aprimorado"):
				metodo = Euler_Aprimorado(in_put)
				print("\n")

			if(in_put[0] == "runge_kutta"):
				metodo = Runge_Kutta(in_put)
				print("\n")

			if(in_put[0] == "adam_bashforth"):
				metodo = Bashforth(in_put)
				print("\n")

			if(in_put[0] == "adam_bashforth_by_euler"):
				metodo = Bashforth_Euler(in_put)
				print("\n")

			if(in_put[0] == "adam_bashforth_by_euler_inverso"):
				metodo = Bashforth_Euler_Inverso(in_put)
				print("\n")

			if(in_put[0] == "adam_bashforth_by_euler_aprimorado"):
				metodo = Bashforth_Euler_Aprimorado(in_put)
				print("\n")

			if(in_put[0] == "adam_bashforth_by_runge_kutta"):
				metodo = Bashforth_RungeKutta(in_put)
				print("\n")

			if(in_put[0] == "adam_multon"):
				metodo = Multon(in_put)	
				print("\n")

			if(in_put[0] == "adam_multon_by_euler"):
				metodo = Multon_Euler(in_put)
				print("\n")

			if(in_put[0] == "adam_multon_by_euler_inverso"):
				metodo = Multon_Euler_Inverso(in_put)
				print("\n")

			if(in_put[0] == "adam_multon_by_euler_aprimorado"):
				metodo = Multon_Euler_Aprimorado(in_put)
				print("\n")

			if(in_put[0] == "adam_multon_by_runge_kutta"):
				metodo = Multon_RungeKutta(in_put)
				print("\n")

			metodo.method()	
	arquivo.close()

if __name__ == '__main__':
	main()
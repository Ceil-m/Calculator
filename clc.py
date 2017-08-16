#!/usr/bin/python3
import os,sys
from math import *

#Try to set title
try:
	sys.stdout.write("\x1b]2;Calculator by Ceil\x07")
except:
	pass
	
#List of safe functions
safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 
'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']

#Make it easier to clear the screen
cls_ = 'os.system("clear")'

#Clear the screen
exec(cls_)

#Head
head = '+=========================+\n| "x" to clear the screen |\n+=========================+'

safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
safe_dict['abs'] = abs

print(head)
#Calculations
def main():

	try:

		op = input("\n[Math]: ") #Evaluate the mathematical input
		
		if op == 'x': #Clear the screen
			exec(cls_)
			print(head)
			main()
		if op == 'None':
			raise SyntaxError
		for x in range(1):
			# add x in
			
			print(eval(op,{"__builtins__":None}))
			main()

	#Handle any errors
	except(KeyboardInterrupt):
		exec(cls_)
		exit()	
	except(NameError,SyntaxError,TypeError,ZeroDivisionError):
		print("\n\nInvalid Input: "+op+"\n")
		main()

main()




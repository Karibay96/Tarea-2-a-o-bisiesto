print("Indique el año que desea comprobar: ")
año = int(input()) #el año que queremos comprobar

if año % 4 != 0: #no divisible entre 4
	print("El año", año, "No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("El año", año, "Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("El año", año, "No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
	print("El año", año, "Es bisiesto")
import math
a = float(input("Insira o valor de A:"))
b = float(input("Insira o valor de B:"))
c = float(input("Insira o valor de C:"))
 
delta = b**2-4*a*c

if delta > 0:
    raiz1 = (-b + math.sqrt(delta))/(2*a) 
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    print ("A primeira raiz é: %.2f. A segunda raiz é: %.2f" %(raiz1, raiz2))
else:
    print ("Não há raízes")

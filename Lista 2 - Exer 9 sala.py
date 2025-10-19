A = int(input("Entre com um número inteiro para A:"))
B = int(input("Entre com um número inteiro para B:"))


if A % 4 == 0:
    print ("%i é divisivel por 4" %(A))
elif A % 5 == 0:
    print ("%i é divisivel por 5" %(A))
else:
    print ("%i não é divisivel por 4 e nem 5" %(A))

if B % 4 == 0:
    print ("%i é divisivel por 4" %(B))
elif B % 5 == 0:
    print ("%i é divisivel por 5" %(B))
else:
    print ("%i não é divisivel por 4 e nem 5" %(B))
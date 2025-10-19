a = float(input("Digite o valor do lado A do triângulo:"))
b = float(input("Digite o valor do lado B do triângulo:"))
c = float(input("Digite o valor do lado C do triângulo:"))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print ("Equilátero")
    elif a == b or a == c or b == c:
        print ("Isósceles")
    else:
        print ("Escaleno")
else:
    print ("Os lados fornecidos não formam um triângulo")
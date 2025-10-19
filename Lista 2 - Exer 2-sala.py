nota1 = float(input("Insira a primeria nota:"))
nota2 = float(input("Insira a segunda nota:"))

media = (nota1 + nota2)/2

if media >= 6.0:
    print ("Parábens! Voce foi aprovado com média: %.2f" %(media))
else:
    exame = float(input("Você foi reprovado. Insira a nota do exame para nova média:"))
    media2 = (media + exame)/2
    if media2 >= 5.0:
        print ("Parábens! Você foi aprovado com média: %.2f" %(media2))
    else:
        print ("Infelizmente você não foi aprovado, com média: %.2f" %(media2))
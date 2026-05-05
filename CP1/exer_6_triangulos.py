l1 = float(input("Digite o valor do primeiro lado: "))
l2 = float(input("Digite o valor do segundo lado: "))
l3 = float(input("Digite o valor do terceiro lado: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    tri = True
else:
    tri = False
    print("Erro: Seu triângulo é inválido.")

if tri:
    if l1 == l2 == l3:
        print("Seu triângulo é Equilátero (todos os lados iguais).")


    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Seu triângulo é Isósceles (dois lados iguais).")


    else:
        print("Seu triângulo é Escaleno (todos os lados diferentes).")




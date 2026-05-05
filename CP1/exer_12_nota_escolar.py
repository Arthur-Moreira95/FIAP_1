nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o numero da porcentagem de faltas: "))

if faltas > 25 :
    media = None

else:
    media = (nota_1 + nota_2) / 2

if media is None:
    print("Reprovado por falta")
elif media >= 7:
    print("Aprovado")
elif 5 <= media <= 6.9:
     print("Recuperação")
elif media < 5:
    print("Reprovado por nota")

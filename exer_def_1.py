n1 = int(input("Digite uma nota: "))    
n2 = int(input("Digite outra nota: "))

def media(n1, n2):
    media = (n1 + n2) / 2
    if media >= 6:
        print(f"Aprovado com média {media:.2f}")
    else:
        print(f"Reprovado com média {media:.2f}")

media(n1, n2)

    
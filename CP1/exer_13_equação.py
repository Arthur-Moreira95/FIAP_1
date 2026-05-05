import math

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if A == 0:
    print("Não é uma equação do segundo grau ")
else:
    delta = (B ** 2) - 4 * A * C
    if delta < 0:
       print("Não há raizes reais")
    if delta == 0:
        raiz_unica = -B / (2 * A)
        print(f"A equação possui apenas uma raiz real: x = {raiz_unica:.2f}")

    if delta > 0:
        raiz_delta = math.sqrt(delta)
        x1 = (-B + raiz_delta) / (2 * A)
        x2 = (-B - raiz_delta) / (2 * A)
        print(f"A equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")

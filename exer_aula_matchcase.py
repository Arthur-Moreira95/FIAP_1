numero = float(input("Digite um numero: "))
print("1 - o dobro")
print("2 - a metade")
print("3 - 10% do numero")
tipo_calculo = input("Digite 1, 2 ou 3 para escolher um tipo de calculo: ")

match tipo_calculo:
    case "1":
        numero = numero * 2
        print(f"Seu número é {numero:.2f}")
    case "2":
        numero = numero / 2
        print(f"Seu número é {numero:.2f}")
    case "3":
        numero = numero * 0.1
        print(f"Seu número é {numero:.2f}")







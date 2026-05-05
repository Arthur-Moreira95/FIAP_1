salario = int(input("Digite o seu salário: "))

if salario <= 2112:
    print("Isento de imposto")

elif 2112 < salario < 2826.65:
    salario = salario*0.925
    print(f"Seu salario é {salario:.2f}")
elif salario > 2826.65:
    salario = salario*0.89
    print(f"Seu salario é {salario:.2f}")
else:
    print("Erro no calculo do imposto de renda")





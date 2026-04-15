valor_saque = int(input("Qual o valor do saque: "))

if valor_saque <= 0 or valor_saque == 1 or valor_saque == 3:
    print("Valor indisponível.")
else:
    print(f"Calculando notas para R$ {valor_saque}")

    restante = valor_saque

    n100 = restante // 100
    restante = restante % 100

    n50 = restante // 50
    restante = restante % 50

    n20 = restante // 20
    restante = restante % 20

    n10 = restante // 10
    restante = restante % 10

    n5 = restante // 5
    restante = restante % 5

    n2 = restante // 2
    restante = restante % 2

    if n100 > 0: print(f"{n100} nota(s) de R$ 100")
    if n50 > 0:  print(f"{n50} nota(s) de R$ 50")
    if n20 > 0:  print(f"{n20} nota(s) de R$ 20")
    if n10 > 0:  print(f"{n10} nota(s) de R$ 10")
    if n5 > 0:   print(f"{n5} nota(s) de R$ 5")
    if n2 > 0:   print(f"{n2} nota(s) de R$ 2")

    if restante > 0:
        print(f"Atenção: Sobrou R$ {restante} que não pôde ser sacado com as notas disponíveis.")
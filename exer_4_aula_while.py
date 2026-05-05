lista = []
lista_errada = []
cont = 0
while cont < 10:
    numero = int(input("Insira um numero inteiro: "))

    if 100 < numero < 200:
        lista.append(numero)
        print(f"Seu numero {lista} está entre 100 e 200")
    else:
        lista_errada.append(numero)
        print(f"Seu numero {lista_errada} não está entre 100 e 200")

    cont += 1



if cont == 10:
    print(f"Sua lista de números certos: {lista} \n Sua lista de números errados: {lista_errada}")
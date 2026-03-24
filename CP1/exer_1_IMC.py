nome = input("Qual é o seu nome: ")
peso = int(input("Qual é o seu peso em Kg: "))
altura = float(input("Qual é a sua altura em metros: "))

imc = peso/(altura*altura)

if imc < 18.5:
    print(f"{nome} seu imc é {imc:.2f} e você está abaixo do peso")

if 18.5 < imc < 24.9:
    print(f"{nome} seu imc é {imc:.2f} e você está normal")

if 25 < imc < 29.9:
    print(f"{nome} seu imc é {imc:.2f} e você está com sobrepeso")

if 30 < imc < 34.9:
    print(f"{nome} seu imc é {imc:.2f} e você está com obesidade grau 1")

if 35 < imc < 39.9:
    print(f"{nome} seu imc é {imc:.2f} e você está com obesidade grau 2")

if 40 < imc:
    print(f"{nome} seu imc é {imc:.2f} e você está com obesidade grau 3")
numero = int(input("Insira um número inteiro: "))

if numero % 2 == 0:
    print("Seu número é par")
else:
    print("Seu número é impar")

if numero > 0:
    print("Além disso seu número é positivo")
elif numero == 0:
    print("Além disso seu número é zero")
elif numero < 0:
    print("Além disso seu número é negativo")

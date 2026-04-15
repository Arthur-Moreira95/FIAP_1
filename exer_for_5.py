import math

lista = []

for n in range(1,16):
   i = int(input("Digite um numero: "))
   lista.append(round(math.sqrt(i),2))

print(lista)
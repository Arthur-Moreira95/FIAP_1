lista_par = []
lista_impar = []

for _ in range(10):
    numero = int(input("Digite um numero inteiro: "))
    if numero % 2 == 0:
        lista_par.append(numero)
    else :
        lista_impar.append(numero)

print(f"{lista_par} <--- Lista de numeros pares")
print(f"{lista_impar} <--- Lista de numeros impares")
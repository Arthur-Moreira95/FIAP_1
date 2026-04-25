lista_media = []
lista_soma_par = []
soma_par = 0
soma_media = 0

for _ in range(10):
   numero = int(input("Digite um numero: "))
   soma_media += numero
   if numero % 2 == 0:
    soma_par += numero

media = soma_media / 10
lista_media.append(media)
lista_soma_par.append(soma_par)
print(f"{lista_soma_par} <-- Lista da soma dos numeros pares")
print(f"{lista_media} <-- Lista da média aritmética dos numeros")









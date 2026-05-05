idade = int(input("Qual a sua idade? "))
anos_contribuidos = int(input("Quantos anos de carreira profissional? "))

if idade >= 65 or anos_contribuidos >= 30:
    print("Já pode se aposentar")

elif idade == 60 and anos_contribuidos == 25:
    print("Já pode se aposentar")
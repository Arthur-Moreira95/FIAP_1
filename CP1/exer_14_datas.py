dia = int(input("Digite dia: "))
mes = int(input("Digite mês: "))
ano = int(input("Digite ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    bissexto = True
else:
    bissexto = False

if mes in [1,3,5,7,8,10,12]:
   limite_dias = 31

elif mes in [4,6,9,11]:
   limite_dias = 30

elif mes == 2:
    if bissexto:
        limite_dias = 29
    else:
        limite_dias = 28


if mes < 1 or mes > 12:
    print("Erro: data inválida")
elif dia < 1 or dia > limite_dias:
    print(f"Erro: data inválida")
else:
    print(f"Sucesso! A data {dia}/{mes}/{ano} é válida.")










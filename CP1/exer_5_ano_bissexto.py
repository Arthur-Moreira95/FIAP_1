ano = int(input("Digite um ano para verificar se é bissexto ou não: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é bissexto")

else:
    print(f"O {ano} não é bissexto")
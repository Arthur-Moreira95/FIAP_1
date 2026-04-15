dia = int(input("Digite o dia de nascimento (1-31): "))
mes = int(input("Digite o mês de nascimento (1-12): "))

if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "áries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "touro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "gêmeos"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "câncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "leão"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "virgem"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "escorpião"
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "sagitário"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    signo = "capricórnio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "aquário"
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "peixes"
else:
    signo = "Data Inválida"

print(f"Seu signo é: {signo}")
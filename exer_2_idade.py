nascimento_ano = int(input("Insira o ano do seu nascimento: "))
idade = 2026 - nascimento_ano
if 18 <= idade < 65:
    print(f"Você tem {idade} e é adulto")
if idade <18:
    print(f"Você tem {idade} e é menor de idade")
if idade >=65:
    print(f"Você tem {idade} e é idoso")
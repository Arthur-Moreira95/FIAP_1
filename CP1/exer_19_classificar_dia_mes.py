mes = int(input("Digite um número correspondente a um mês: "))
match mes:
    case 1:
        print("Esse número corresponde a Janeiro, esse mês tem 31 dias")
    case 2:
        print("Esse número corresponde a Fevereiro, esse mês tem 28/29 dias")
    case 3:
        print("Esse número corresponde a Março, esse mês tem 31 dias")
    case 4:
        print("Esse número corresponde a Abril, esse mês tem 30 dias")
    case 5:
        print("Esse número corresponde a Maio, esse mês tem 31 dias")
    case 6:
        print("Esse número corresponde a Junho, esse mês tem 30 dias")
    case 7:
        print("Esse número corresponde a Julho, esse mês tem 31 dias")
    case 8:
        print("Esse número corresponde a Agosto, esse mês tem 31 dias")
    case 9:
        print("Esse número corresponde a Setembro, esse mês tem 30 dias")
    case 10:
        print("Esse número corresponde a Outubro, esse mês tem 31 dias")
    case 11:
        print("Esse número corresponde a Novembro, esse mês tem 30 dias")
    case 12:
        print("Esse número corresponde a Dezembro, esse mês tem 31 dias")
    case _:
        print("Mês inexistente. Tente novamente")
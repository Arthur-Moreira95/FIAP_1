opcao = int(input("Digite o veiculo que você está utilizando: "))
match opcao:
    #inventei os valores do pedagio e do eixo
    case "carro":
        print("O valor do pedágio do carro será de 10 reais.")
    case "moto":
        print("O valor do pedágio da moto será de 5 reais.")
    case "onibus":
        print("O valor do pedágio do ônibus será de 20 reais.")
    case "caminhao":
        eixos = int(input("Quantos eixos o caminhão possui? (de 2 a 7): "))
        match eixos:
            case 2:
                print("O pedágio será de 10 reais.")
            case 3:
                print("O pedágio será de 20 reais.")
            case 4:
                print("O pedágio será de 30 reais.")
            case 5:
                print("O pedágio será de 35 reais.")
            case 6:
                print("O pedágio será de 40 reais.")
            case 7:
                print("O pedágio será de 45 reais.")
            case _:
                print("Valor inválido.")
    case _:
        print("Valor inválido.")
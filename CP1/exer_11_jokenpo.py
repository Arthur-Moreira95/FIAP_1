j1 = input("Digite qual jogada você quer fazer\n[PE] para pedra, [PA] para papel e [T] para tesoura: ").strip().upper()
j2 = input("Digite qual jogada você quer fazer\n[PE] para pedra, [PA] para papel e [T] para tesoura: ").strip().upper()

print(f"Jogador 1: {j1} | Jogador 2: {j2}")

match (j1, j2):
    case (j1, j2) if j1 == j2:
        print("Resultado: Empate!")


    case ("PE", "T") | ("PA", "PE") | ("T", "PA"):
        print("Resultado: Jogador 1 venceu!")


    case _:
        print("Resultado: Jogador 2 venceu!")
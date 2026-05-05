def limpar_dados(lista_bruta):
    lista_final = []

    for item in lista_bruta:
        item = item.strip()  # remove espaços

        if item != "":  # evita vazio
            try:
                numero = float(item)
                lista_final.append(numero)
            except:
                pass  # ignora valores inválidos

    media = sum(lista_final) / len(lista_final) if lista_final else 0

    return lista_final, media


# entrada do usuário
entrada = input("Digite as temperaturas separadas por vírgula: ")
lista = entrada.split(",")

limpa, media = limpar_dados(lista)

print("Lista limpa:", limpa)
print("Média:", media)

# IA fez
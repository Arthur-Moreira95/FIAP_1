lados = int(input("Digite o número de lados do polígono: "))

def tipo_poligono(lados):
    if lados == 3:
        print("Triângulo")
    elif lados == 4:
        print("Quadrado")
    elif lados == 5:
        print("Pentágono")
    else:
        print("Valor inválido")
    
tipo_poligono(lados)
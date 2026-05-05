altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo (M/F): ").upper()

def peso_ideal(altura, sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58 
        
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        return "Sexo inválido"

resultado = peso_ideal(altura, sexo)
print("O peso ideal é:", resultado)

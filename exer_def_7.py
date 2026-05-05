def ler_numero ():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    def tabuada (numero):
        print(f"Tabuada do {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")


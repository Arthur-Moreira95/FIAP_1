n1 = float(input("Digite o primeiro digito: "))
n2 = float(input("Digite o segundo digito: "))
operacao = input("Digite um operador como:\n[+],[-],[/]: ")

match operacao:

            case "+":
               resultado = n1 + n2
               print(f"Sucesso: {resultado}")
            case "-":
               resultado = n1 - n2
               print(f"Sucesso: {resultado}")
            case "*":
               resultado = n1 * n2
               print(f"Sucesso: {resultado}")
            case "/":
                 if n2 != 0:
                  resultado = n1 / n2
                  print(f"Sucesso: {resultado}")
                 else:
                  print("O divisor não pode ser zero!")






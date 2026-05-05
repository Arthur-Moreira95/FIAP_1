valor_produto = float(input("Digite o valor do produto: "))
print("Digite 1 para [PIX], digite 2 para [Cartão de crédito], digite 3 para [Crédito parcelado]")
forma_pagamento =  int(input("Digite o tipo de pagamento: "))

if forma_pagamento != 1 or 2 or 3:
    print("Forma de pagamento inválido")

match forma_pagamento:
    case 1:
        valor_produto = valor_produto*0.9
        print(f"O valor final do produto no pix fica {valor_produto:.2f}")

    case 2:
        print(f"O valor final do produto no crédtito fica {valor_produto:.2f}")

    case 3:
        valor_produto = valor_produto*1.05
        print(f"O valor final do produto parcelado no crédito fica  {valor_produto:.2f}")





print("Códigos comuns de HTTP: 200|400|401|403|404|500")
http = int(input("Insira um dos códigos acima: "))
match http:
    case 200:
        print("A página ou o dado solicitado foi carregado corretamente.")
    case 400:
        print("O servidor não entendeu o pedido por causa de um erro de sintaxe ou URL mal escrita.")
    case 401:
        print("Você precisa fazer login para ver este conteúdo.")
    case 403:
        print("O servidor entendeu quem você é, mas você não tem permissão para acessar essa área específica.")
    case 404:
        print("Página não encontrada. O endereço digitado não existe no servidor.")
    case 500:
        print("Algo deu errado no código do site e o servidor não sabe explicar exatamente o quê.")
    case _:
        print("Codigo não encontrado.")


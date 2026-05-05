usuario_salvo = "admin"
senha = "1234"

while True:
    print("Login")
    user = input("Nome de usuário: ")
    password = input("Senha: ")
    if user == usuario_salvo and password == senha:
        print("Login efetuado com sucesso")
        break
    else:
        print("Usuário ou senha incorreto. Tente novamente.")
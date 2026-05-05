def validar(senha):
    return (
        len(senha) >= 8 and
        any(caractere.isupper() for caractere in senha) and
        any(caractere.isdigit() for caractere in senha) and
        any(not caractere.isalnum() for caractere in senha)
    )

while True:
    senha = input("Digite uma senha: ")

    if validar(senha):
        print("Senha válida ✅")
        break
    else:
        print("Senha inválida ❌")
        print("A senha precisa ter:")
        print("- Pelo menos 8 caracteres")
        print("- Uma letra maiúscula")
        print("- Um número")
        print("- Um caractere especial\n")

# IA fez
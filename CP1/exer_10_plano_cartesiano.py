x = int(input("Digite um numero para a coordenada x: "))
y = int(input("Digite um numero para a coordenada y: "))

if x == 0 and y == 0:
    print("O ponto está na origem")
elif x == 0:
    print("O ponto está sobre o Eixo Y.")
elif y == 0:
    print("O ponto está sobre o Eixo X.")
elif x > 0 and y > 0:
    print("O ponto está no primeiro Quadrante")
elif x < 0 and y > 0:
    print("O pónto está está no segundo Quadrante")
elif x < 0 and y < 0:
    print("O ponto está no terceiro Quadrante")
elif x > 0 and y < 0:
    print("O ponto está no quarto Quadrante")


# existe a forma de fazer somente com matchcase

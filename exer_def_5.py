raio = int(input("Digite o raio do círculo para calcular a área: "))
def area_circulo(raio):
    area = 3.14 * raio ** 2
    print(f"A área do círculo com raio {raio} é {area:.2f}")


area_circulo(raio)

def perimetro_circulo(raio):
    perimetro = 2 * 3.14 * raio
    print(f"O perímetro do círculo com raio {raio} é {perimetro:.2f}")

perimetro_circulo(raio)

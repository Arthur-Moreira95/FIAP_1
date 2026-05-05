temp = int(input("Qual é a temperatura:  "))
escala = input("A temperatura está em Celsius ou Fahrenheit?\n[F] para fahrenheit ou [C] para celcius: ").strip().upper()

if escala == 'C':

    resultado = temp * 1.8 + 32
    print(f"{temp}°C equivale a {resultado:.2f}°F")
elif escala == 'F':

    resultado = (temp - 32) * 5/9
    print(f"{temp}°F equivale a {resultado:.2f}°C")
else:
    print("Escala inválida! Por favor, use 'C' ou 'F'.")









temp = int(input("Qual é a temperatura:  "))
escala = input("Você deseja que a escala seja em Fahrenheit ou celcius?\n[F] para fahrenheit ou [C] para celcius: ").upper()
print("Agora ")
if escala == "F":
    temp = temp * 1.8 + 32

elif escala == "C":
    temp = (temp - 32) * 1.8


print(f"A temperatura convertida {temp}")







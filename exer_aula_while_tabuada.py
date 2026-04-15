n = int(input("Digite seu numero: "))
multiplica = 0
while n > 0:
   multiplica += 1
   resultado = n * multiplica
   print(f"{n} x {multiplica} = {resultado}")
   if multiplica == 10:
       break
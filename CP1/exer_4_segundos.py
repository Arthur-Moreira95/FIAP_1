segundos_pedidos = int(input("Quantos segundos deseja converter? "))
horas = segundos_pedidos // 3600
resto = segundos_pedidos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} horas e {minutos} minutos e {segundos} segundos")
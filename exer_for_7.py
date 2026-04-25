n = int(input("Insira um numero para verificar se é primo ou não: "))
i = 2
x = 0
for i in range(i, n):
    if n % i == 0:
        x+=1
        break
if x == 0:
    print("O número é primo")
else:
    print("O número não é primo")
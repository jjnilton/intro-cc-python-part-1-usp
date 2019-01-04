n = int(input("Digite um número inteiro: "))
total = 0
while n != 0:
    c = n % 10
    n = n // 10
    total = total + c
print(total)

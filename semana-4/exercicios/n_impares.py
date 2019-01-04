n = int(input("Digite o valor de n: "))
numero = 0
while n >= 1:
    numero = numero + 1
    if numero % 2 != 0:
        print(numero)
        n = n - 1

n = int(input("Digite um número inteiro: "))
c = 0
if n == 2 or n == 3:
    print("primo")
elif (not n % 3 == 0) and (not n % 2 == 0):
    print("primo")
else:
    print("não primo")

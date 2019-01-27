lista = []
numero = -1
while (numero != 0):
    numero = int(input("Digite um número: "))
    lista.append(numero)
lista.reverse()

for i in lista[1:]:
    print(i)
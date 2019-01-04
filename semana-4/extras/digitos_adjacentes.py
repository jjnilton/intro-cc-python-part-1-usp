n = int(input("Digite um número inteiro: "))

ultimo = 0
penultimo = 0

indicador = False

while not indicador:
    ultimo = n % 10
    n = n // 10
    penultimo = n % 10
    if (ultimo == penultimo) and n != 0:
        print("sim")
        indicador = True
    elif (n == 0):
        print("não")
        indicador = True
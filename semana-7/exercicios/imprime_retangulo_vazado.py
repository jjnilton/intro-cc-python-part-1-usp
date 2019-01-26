largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

linha = 0
coluna = 0

while (linha < altura):
    linha = linha + 1
    while (coluna < largura):
        coluna = coluna + 1
        if (linha != 1 and coluna != 1 and linha != altura and coluna != largura):
            print(" ", end="")
        else:
            print("#", end="")
    print()
    coluna = 0
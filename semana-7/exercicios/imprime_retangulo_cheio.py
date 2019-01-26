largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

linha = 0
coluna = 0

while (linha < altura):
    linha = linha + 1
    while (coluna < largura):
        print("#", end="")
        coluna = coluna + 1
    print()
    coluna = 0
        
        
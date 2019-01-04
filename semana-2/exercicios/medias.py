#nota = []
nota_final = 0
for n in range(0,4):
    if n == 0:
        palavra = "primeira"
    elif n == 1:
        palavra = "segunda"
    elif n == 2:
        palavra = "terceira"
    else:
        palavra = "quarta"
    nota = input("Digite a " + palavra +" nota: ")
    nota_final += int(nota)
print("A média aritmética é", nota_final/4)
    #nota[n] = print("Digite a nota", n)

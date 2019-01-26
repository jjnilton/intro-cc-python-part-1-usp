
def e_hipotenusa(numero):
    retorno = False
    a = numero
    b = 1
    c = 1
    while (numero > b):
        if retorno:
            break
        b = b + 1
        while (numero > c):
            # print ("se %d^2 = %d^2 + %d^2" % (a, b, c))
            if (a**2 == b**2 + c**2):
                retorno = True
                # print("hipotenusa:", a)
                # print("cateto 1:", b)
                # print("cateto 2:", c)
                break
            c = c + 1
        c = 1
    return retorno


# print(e_hipotenusa(12))

def soma_hipotenusas(numero):
    contador = 0
    total = 0
    while (numero >= contador):
        if (e_hipotenusa(contador)):
            # print(contador)
            total = total + contador
        contador = contador + 1
    return total


soma_hipotenusas(25)

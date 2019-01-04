import math

a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

delta = (b ** 2) - (4 * a * c)

if delta == 0:
    #print("delta é 0, duas raízes reais e iguais")
    raiz1 = (-b)/(2*a)
    raiz2 = raiz1
    print("a raiz desta equação é", raiz2)
elif delta > 0:
    #print("delta maior que zero")
    raiz1 = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    if (raiz1 < raiz2):
        print("as raízes da equação são", raiz1, "e", raiz2)
    else:
        print("as raízes da equação são", raiz2, "e", raiz1)
else:
    #print("delta menor que zero")
    #raiz1 = (-b/2*a) + (math.sqrt(4*a*c - b**2))/(2*a)
    #raiz2 = (-b/2*a) - (math.sqrt(4*a*c - b**2))/(2*a)
    print("esta equação não possui raízes reais")


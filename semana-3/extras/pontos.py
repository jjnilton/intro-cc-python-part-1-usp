import math

ax = int(input("Número 1: "))
ay = int(input("Número 2: "))
bx = int(input("Número 3: "))
by = int(input("Número 4: "))

d = math.sqrt((ax - ay)**2 + (bx-by)**2)
if d >= 10:
    print("longe")
else:
    print("perto")

def primo(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 != 0 and x % 3 != 0 and x > 1:
        return True
    else:
        return False   

def maior_primo(x):
    if primo(x):
        return x
    elif x < 2:
        return "Não é primo"
    else:
        while not primo(x):
            x = x - 1
            if primo(x):
                return x

n = int(input("type a number: "))
print(maior_primo(n))

def vogal(x):
    x = x.lower()
    if x == "a" or x == "e" or x == "i" or x == "o" or x =="u":
        return True
    else:
        return False

def teste_vogal():
    assert vogal("a") == True
    assert vogal("E") == True
    assert vogal("b") == False

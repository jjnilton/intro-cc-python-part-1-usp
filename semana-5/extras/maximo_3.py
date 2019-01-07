def maximo(x, y, z):
    if x > y:
        maior = x
    else:
        maior = y
    if maior > z:
        maior = maior
    else:
        maior = z
    return maior

def test_maximo():
    assert maximo(3,4,5) == 5
    assert maximo(2,5,3) == 5
    assert maximo(-1,0,3) == 3
    assert maximo(-10,0,-5) == 0

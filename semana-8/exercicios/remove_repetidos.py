def remove_repetidos(lista):
    lista.sort()
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                del lista[j]
            else:
                j = j + 1
        i = i + 1
    return lista


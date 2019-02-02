import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    a = as_a
    b = as_b

    total = 0

    for i in range(0,6):
        soma = a[i] - b[i]
        if soma < 0:
            soma = soma * -1
        total = total + soma
    total = total / 6
    return total


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    lista_sentencas = sentencas(texto)
    lista_frases = frases(lista_sentencas)
    lista_palavras = palavras(lista_frases)

    ass = []
    ass.append(tamanho_medio_palavras(lista_palavras))
    ass.append(relacao_token_type(lista_palavras))
    ass.append(razao_haplax_logomana(lista_palavras))
    ass.append(tamanho_medio_sentenca(lista_sentencas))
    ass.append(complexidade_sentenca(lista_sentencas))
    ass.append(tamanho_medio_frase(lista_frases))
    return ass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    grau_atual = 0
    menor_grau = compara_assinatura(calcula_assinatura(textos[0]), ass_cp)

    for texto in textos:
        grau_atual = compara_assinatura(calcula_assinatura(texto), ass_cp)
        if grau_atual < menor_grau:
            indice = textos.index(texto) + 1
            menor_grau = grau_atual
    return indice



def n_total_palavras(lista_palavras):
    return len(lista_palavras)

def soma_tamanhos_palavras(lista_palavras):
    total = 0
    for palavra in lista_palavras:
        total = total + len(palavra)
    return total


def tamanho_medio_palavras(lista_palavras):
    return soma_tamanhos_palavras(lista_palavras) / n_total_palavras(lista_palavras)


def relacao_token_type(lista_palavras):
    total = n_palavras_diferentes(lista_palavras) / n_total_palavras(lista_palavras)
    return total


def razao_haplax_logomana(lista_palavras):
    return n_palavras_unicas(lista_palavras) / n_total_palavras(lista_palavras)


def n_sentencas(lista_sentencas):
    return len(lista_sentencas)


def soma_caracteres_sentencas(lista_sentencas):
    sentencas = lista_sentencas
    total = 0
    for i in sentencas:
        total = total + len(i)
    return total

def tamanho_medio_sentenca(lista_sentencas):
    return soma_caracteres_sentencas(lista_sentencas) / n_sentencas(lista_sentencas)

def n_total_frases(lista_frases):
    return len(lista_frases)

def complexidade_sentenca(lista_sentencas):
    
    return n_total_frases(frases(lista_sentencas)) / len(lista_sentencas)

def soma_caracteres_frases(lista_frases):
    total = 0
    for i in lista_frases:
        total = total + len(i)
    return total

def tamanho_medio_frase(lista_frases):
    return soma_caracteres_frases(lista_frases) / n_total_frases(lista_frases)


def sentencas(texto):
    lista_sentencas = separa_sentencas(texto)
    return lista_sentencas


def frases(sentencas):
    lista_sentencas = sentencas
    frases = []
    for sentenca in lista_sentencas:
        frases.append(separa_frases(sentenca))
    # lista_frases = [frase for sublista in frases for frase in sublista]
    lista_frases = []
    for sublista in frases:
        for frase in sublista:
            lista_frases.append(frase)
    return lista_frases


def palavras(frases):
    lista_frases = frases
    palavras = []
    for frase in lista_frases:
        palavras.append(separa_palavras(frase))
    #lista_palavras = [palavra for sublista in palavras for palavra in sublista]
    lista_palavras = []
    for sublista in palavras:
        for palavra in sublista:
            lista_palavras.append(palavra)
    return lista_palavras


def main():

    assinatura = le_assinatura()

    textos = le_textos()


    autor_infectado = avalia_textos(textos, assinatura)
    print("O autor do texto", autor_infectado, "está infectado com COH-PIAH")


main()
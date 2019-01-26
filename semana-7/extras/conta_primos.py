# percorre os inteiros em ordem crescente até determinado número informado como parâmetro
# verificando se esses números são divisíveis pelo parâmetro
# caso o número seja divisível, um contador é incrementado
def e_primo(numero):
    """verifica se um número é primo e retorna um booleano"""
    resultado = True
    numero_teste = 1
    contador = 0
    while (numero_teste <= numero):
        if (numero % numero_teste == 0):
            contador = contador + 1
        if (contador > 2):
            resultado = False
            break 
        numero_teste = numero_teste + 1
    return resultado

# percorre de forma decrescente os números maiores ou iguais 2
# incrementando um contador caso o número seja primo 
def n_primos(numero):
    """informa quantos números primos existem até o número informado"""
    contador = 0
    while (numero >= 2):
        if (e_primo(numero)):
            contador = contador + 1
        numero = numero - 1
    return contador

n_primos(6)

def main():
    jogo()

def computador_escolhe_jogada(n, m):

    jogada = 0
    resto_simulado = 0
    while (jogada <= m and jogada <= n):
        jogada = jogada + 1
        if (jogada > m or jogada > n):
            break
        resto_simulado = n - jogada
        if (resto_simulado % (m+1) == 0):
            if (jogada == 1):
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou",jogada,"peças.")
            return jogada
            
    
    if (n < m):
        jogada = n
    else:
        jogada = m
    if (jogada == 1):
        print("O computador tirou uma peca.")
    else:
        print("O computador tirou",jogada,"pecas.")
    return jogada
            

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while (not jogada_valida):
        jogada = int(input("Quantas peças você vai tirar? "))
        if (jogada <= m and jogada <= n and jogada > 0):
            jogada_valida = True
        else:
            print("Jogada invalida, tente novamente")
    if(jogada == 1):
        print("\nVocê tirou uma peça.")
    else:
        print("\nVocê tirou",jogada,"peças.")
    return jogada

def partida():
    n = 0
    m = 0
    while (n < 1 and m < 1):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de pecas por jogada? "))
        if (n < 1 and m < 1):
            print("Oops! Jogada inválida! Tente de novo.")
    if (n % (m+1) == 0):
        primeiro_jogador = "usuário"
        segundo_jogador = "computador"
        primeiro_a_jogar = usuario_escolhe_jogada
        segundo_a_jogar = computador_escolhe_jogada
        print ("\nVocê começa!\n")
        
    else:
        primeiro_jogador = "computador"
        segundo_jogador = "usuário"
        primeiro_a_jogar = computador_escolhe_jogada
        segundo_a_jogar = usuario_escolhe_jogada
        print ("Computador começa!\n")
        
    vencedor = ""
    pecas_restantes = n
    while (pecas_restantes > 0):
        pecas_tiradas_pelo_primeiro = primeiro_a_jogar(n, m)
        ultimo_jogador = primeiro_jogador
        pecas_restantes = pecas_restantes - pecas_tiradas_pelo_primeiro
        n = pecas_restantes
        if (pecas_restantes == 1):
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam",pecas_restantes,"no tabuleiro.\n")
        # inverte função
        aux_a_jogar = primeiro_a_jogar
        primeiro_a_jogar = segundo_a_jogar
        segundo_a_jogar = aux_a_jogar
        # inverte jogador
        aux_jogador = primeiro_jogador
        primeiro_jogador = segundo_jogador
        segundo_jogador = aux_jogador

        vencedor = ultimo_jogador
    print("Fim do jogo! O", vencedor, "ganhou!\n")
        
        
def campeonato():
    print("Você escolheu campeonato\n")
    rodada = 1
    while (rodada <= 3):
        print("**** Rodada",rodada,"****\n")
        partida()
        rodada = rodada + 1
    print("Placar: Você 0 X 3 Computador")
        
def jogo():    
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    opcao = int(input("2 - para jogar um campeonato "))
    
    if (opcao == 1):
        partida()
    elif(opcao == 2):
        campeonato()
    else:
        print("Opção inválida, tente novamente.")

main()
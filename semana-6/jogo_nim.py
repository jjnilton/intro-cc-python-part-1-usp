def main():
    jogo()

def computador_escolhe_jogada(n, m):
    #print("Vez do computador")
    #print("n do pc", n)
    #print("m do pc", m)
    jogada = 0
    resto_simulado = 0
    while (jogada <= m and jogada <= n):
        jogada = jogada + 1
        if (jogada > m or jogada > n):
            break
        resto_simulado = n - jogada
        #print(jogada)
        if (resto_simulado % (m+1) == 0):
            #print("jogada_do_pc:",jogada)
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
        #print(n,"é múltiplo de",m+1)
        pc_comeca = False
        primeiro_a_jogar = "Você"
        segundo_a_jogar = "Computador"
        print ("\nVocê começa!\n")
        
    else:
        pc_comeca = True
        #print(n,"não é múltiplo de",m+1)
        primeiro_a_jogar = "\nComputador"
        segundo_a_jogar = "Você"
        print (primeiro_a_jogar, "começa!\n")
        
    pecas_inicial = n
    max_pecas_por_jogada = m
    #print("Numero total de pecas:", n)
    #print("Pecas que podem ser tiradas por jogada:", m)
    vencedor = "computador"
    # jogadas
    pecas_restantes = n
    #print(">pecas_restantes",pecas_restantes)
    while (pecas_restantes > 0):
        if (pc_comeca):
            pecas_tiradas_pelo_computador = computador_escolhe_jogada(n, m)
            pecas_restantes = pecas_restantes - pecas_tiradas_pelo_computador
            n = pecas_restantes
            if (pecas_restantes == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam",pecas_restantes,"no tabuleiro.\n")
            #print(">pecas_restnates depois do computador tirar",pecas_restantes)
            if (pecas_restantes == 0):
                vencedor = "computador"
                break
            pecas_tiradas_pelo_jogador = usuario_escolhe_jogada(n, m)
            pecas_restantes = pecas_restantes - pecas_tiradas_pelo_jogador
            n = pecas_restantes
            if (pecas_restantes == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif (pecas_restantes > 1):
                print("Agora restam",pecas_restantes,"no tabuleiro.\n")
        elif (not pc_comeca):
            pecas_tiradas_pelo_jogador = usuario_escolhe_jogada(n, m)
            pecas_restantes = pecas_restantes - pecas_tiradas_pelo_jogador
            n = pecas_restantes
            if (pecas_restantes == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            else:
                print("Agora restam",pecas_restantes,"no tabuleiro.\n")
            if (pecas_restantes == 0):
                vencedor = "usuário"
                break
            pecas_tiradas_pelo_computador = computador_escolhe_jogada(n, m)
            pecas_restantes = pecas_restantes - pecas_tiradas_pelo_computador
            n = pecas_restantes
            if (pecas_restantes == 1):
                print("Agora resta apenas uma peça no tabuleiro.\n")
            elif(pecas_restantes > 1):
                print("Agora restam",pecas_restantes,"no tabuleiro.\n")
            #print(">pecas_restnates depois do pc tirar",pecas_restantes)
    print("Fim do jogo! O",vencedor,"ganhou!\n")
        
        
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




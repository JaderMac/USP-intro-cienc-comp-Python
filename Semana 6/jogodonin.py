def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    p=0
    while p!=1 and p!=2:
        p=int(input("Escolha um número: "))
    if p==1:
        print("Você escolheu uma partida isolada")
        return 1
    else:
        print("Você escolheu um campeonato 2")
        return 3

def pegaPeca():
    pecas=int(input("Quantas Peças? "))
    return pecas

def pegaLimite(pecas):
    limite=0
    while limite==0 or limite>=pecas:
        limite = int(input("Limite de peças por jogada? "))
    return limite

def quemComeca(limite,pecas):
    if (((limite+1)%pecas) != 0):        
        print("Você começa.")
        return True
    else:
        print("O Computador começa.")
        return False

def usuario_escolhe_jogada(pecasnotabuleiro, limiteporjogada):
    ok=False
    while ok==False:
        retira=int(input("Quantas peças você vai tirar? "))   
        if(retira>=pecasnoTabuleiro):
            print("Oops! Jogada inválida! Tente de novo.")
            ok=False
        else:
            ok=True
            print("Você retirou",retira,"peças.")
            return -retira

def computador_escolhe_jogada(pecasnotabuleiro, limiteporjogada):
    if(pecasnotabuleiro <= limiteporjogada):
        print("O computador retirou",pecasnotabuleiro,"peças.")
        return pecasnotabuleiro
    else:
        quantia = pecasnotabuleiro % (limiteporjogada+1)
        if quantia > 0:
            return quantia
        else:
            return limiteporjogada

def pecasnoTabuleiro(pecas):
    print("Agora restam",pecas,"no tabuleiro.")

def placar(voce, PC):
    print("Placar: Você",voce,"X",PC,"Computador")
    if voce > PC:
        return voce
    else:
        return PC

def fim(jogos):
    if (jogos==3):
        print("***** Final do Campeonato! *****")
    else:
        print("***** Fim de Jogo! *****")

def partida():
    
    if pecasnotabuleiro % (limiteporjogada+1) == 0:
        print('Voce começa!')
    else:
        print('Computador começa!')
        ComputadorJoga = True

    while pecasnotabuleiro > 0:
        if ComputadorJoga:
            computadorRemove = computador_escolhe_jogada(pecasnotabuleiro, limiteporjogada)
            pecasnotabuleiro = pecasnotabuleiro - computadorRemove
            if computadorRemove == 1:
                print('O computador tirou uma peça')
            else:
                print('O computador tirou', computadorRemove, 'peças')
            ComputadorJoga = False
        else:
            jogadorRemove = usuario_escolhe_jogada(pecasnotabuleiro, limiteporjogada)
            pecasnotabuleiro = pecasnotabuleiro - jogadorRemove
            if jogadorRemove == 1:
                print('Você tirou uma peça')
            else:
                print('Você tirou', jogadorRemove, 'peças')
            ComputadorJoga = True

        if pecasnotabuleiro == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            if pecasnotabuleiro != 0:
                print('Agora restam,', pecasnotabuleiro, 'peças no tabuleiro.')

    print('Fim do jogo! O computador ganhou!')

    
jogada = inicio()
pecasnotabuleiro = pegaPeca()
limiteporjogada = pegaLimite(pecasnotabuleiro)
quemComeca(limiteporjogada,pecasnotabuleiro)

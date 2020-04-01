def computador_escolhe_jogada(pecasNoTab, limitePorJogada):
    computadorTira = 1
    while computadorTira != limitePorJogada: 
        if (pecasNoTab - computadorTira) % (limitePorJogada+1) == 0:
            return computadorTira
        else:
            computadorTira += 1
    return computadorTira

def usuario_escolhe_jogada(pecasNoTab, limitePorJogada):
    jogadaValida = False
    while jogadaValida == False:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > limitePorJogada or jogadorRemove < 1:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            jogadaValida = True
    return jogadorRemove

def campeonato():
    Rodada = 1
    while Rodada <= 3:
        print('**** Rodada', Rodada, '****')
        JogoNiM()
        Rodada += 1
    print('Placar: Você 0 X 3 Computador')

def JogoNiM():
    pecasNoTab = int(input('Quantas peças? '))
    limitePorJogada = int(input('Limite de peças por jogada? '))
    PCjoga = False

    if pecasNoTab % (limitePorJogada+1) == 0:
        print()
        print('Voce começa!')
    else:
        print()
        print('Computador começa!')
        PCjoga = True

    while pecasNoTab > 0:
        if  PCjoga:
            computadorRemove = computador_escolhe_jogada(pecasNoTab, limitePorJogada)
            pecasNoTab = pecasNoTab - computadorRemove
            if computadorRemove == 1:
                print('O computador tirou uma peça')
            else:
                print('O computador tirou', computadorRemove, 'peças')
            PCjoga = False
        else:
            jogadorRemove = usuario_escolhe_jogada(pecasNoTab, limitePorJogada)
            pecasNoTab = pecasNoTab - jogadorRemove
            if jogadorRemove == 1:
                print('Você tirou uma peça')
            else:
                print('Você tirou', jogadorRemove, 'peças')
            PCjoga = True

        if pecasNoTab == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        else:
            if pecasNoTab != 0:
                print('Agora restam,', pecasNoTab, 'peças no tabuleiro.')

    print('Fim do jogo! O computador ganhou!')

def inicio():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    NumeroPartidas = 0

    while NumeroPartidas !=1 and NumeroPartidas != 2:
        NumeroPartidas = int(input("Escolha um número válido (1/2): "))

    if NumeroPartidas == 1:
        print("Você escolheu uma partida isolada")
        return 1
    else:
        print("Você escolheu um campeonato 2")
        return 2

jogodonin = inicio()

if jogodonin == 1:
    JogoNiM()
else:
    print('Voce escolheu um campeonato!')
    campeonato()





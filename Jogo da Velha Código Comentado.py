##As variáveis definem as casas do tabuleiro:

cs1 = "1"
cs2 = "2"
cs3 = "3"
cs4 = "4"
cs5 = "5"                 
cs6 = "6"
cs7 = "7"
cs8 = "8"
cs9 = "9"

##Printa o tabuleiro:

def tabuleiro(cs1, cs2, cs3, cs4, cs5, cs6,  cs7, cs8, cs9): 
    print(("     |     |     \n" + \
          "  %s  |  %s  |  %s  \n" + \
          "     |     |     \n" + \
          "-----+-----+-----\n" + \
          "     |     |     \n" + \
          "  %s  |  %s  |  %s  \n" + \
          "     |     |     \n" + \
          "-----+-----+-----\n" + \
          "     |     |     \n" + \
          "  %s  |  %s  |  %s  \n" + \
          "     |     |   \n") % (cs1, cs2, cs3, cs4, cs5, cs6,  cs7, cs8, cs9))

##Define as possiveis formas de ganhar e informa o ganhador na tela:

def indicaGanhador(JOGADA):
    if cs1 == cs2 == cs3 or cs4 == cs5 == cs6 or cs7 == cs8 == cs9 or\
       cs1 == cs4 == cs7 or cs2 == cs5 == cs8 or cs3 == cs6 == cs9 or\
       cs1 == cs5 == cs9 or cs3 == cs5 == cs7:
        (tabuleiro(cs1, cs2, cs3, cs4, cs5, cs6,  cs7, cs8, cs9))
        print("O jogador %s venceu!!" % JOGADA)
        return True
    else:
        (tabuleiro(cs1, cs2, cs3, cs4, cs5, cs6,  cs7, cs8, cs9))
        return False

##Define as diferentes formas em que não há um jogador e informa na tela que deu velha:

def testador_deVelha():
    if cs1 != '1' and cs2 != '2' and cs3 != '3' and\
       cs4 != '4' and cs5 != '5' and cs6 != '6' and\
       cs7 != '7' and cs8 != '8' and cs9 != '9':
        print("Deu velha!!")
        return True
    return False

##Mostra na tela os valores X ou O quando os jogadores jogam:

def validador_deJogada(casa):
    if (casa == '1' and cs1 != '1') or \
       (casa == '2' and cs2 != '2') or \
       (casa == '3' and cs3 != '3') or \
       (casa == '4' and cs4 != '4') or \
       (casa == '5' and cs5 != '5') or \
       (casa == '6' and cs6 != '6') or \
       (casa == '7' and cs7 != '7') or \
       (casa == '8' and cs8 != '8') or \
       (casa == '9' and cs9 != '9'):
        return False
    return True

JOGADA = ' '

##Da a opção para o jogador iniciar o jogo sair do mesmo:

inicio = int(input("Digite '1' para iniciar ou '2' para sair: ")) 

##Certifica que o usuário digite o somente os valores X ou O e 1 ou 2 sejam escolhidos pelo jogador no incio
##exibindo uma mensagem até que o jogador digite corretamente:

while inicio != 1 and inicio != 2:
    inicio = int(input("Dado invalido! Digite '1' ou '2': "))
else:
    if inicio == 1:
    	inicio = 1
    elif inicio == 2:
        inicio = 2

##Da a opção de escolher o simbolo do jogador e deixa o modo de digitar os valores
##de forma maiúscula ou minúscula no teclado:

while inicio == 1:
    simbolo = input("Escolha seu simbolo - 'X' ou 'O': ")
    while simbolo != 'x' and simbolo != 'X' and simbolo != 'o' and simbolo != 'O':
    	simbolo = input("Dado invalido! Digite 'X' ou 'O': ")
    else:
        if simbolo == 'x' or simbolo == 'X':
            JOGADA = 'X'
        elif simbolo == 'o' or simbolo == 'O':
            JOGADA = 'O'

##Alterna entre os jogadores para escolherem as casas para jogar e certifica que o jogador digitem
##somente X ou O durante o jogo:

    while not indicaGanhador("O" if JOGADA == "X" else "X") and not testador_deVelha():
        casa = input("Jogador %s escolha sua jogada: " % JOGADA)
        while casa != '1' and casa != '2' and casa != '3' and casa != '4' and casa != '5' and casa != '6' and casa != '7' and casa != '8' and casa != '9':
            casa = input("Jogador %s escolha sua jogada: " % JOGADA)
        else:
            pass
    
        if validador_deJogada(casa):
            if (casa == '1'): cs1 = JOGADA
            elif (casa == '2'): cs2 = JOGADA
            elif (casa == '3'): cs3 = JOGADA
            elif (casa == '4'): cs4 = JOGADA
            elif (casa == '5'): cs5 = JOGADA
            elif (casa == '6'): cs6 = JOGADA
            elif (casa == '7'): cs7 = JOGADA
            elif (casa == '8'): cs8 = JOGADA
            elif (casa == '9'): cs9 = JOGADA
            if JOGADA == "X":
                JOGADA = "O"
            else:
                JOGADA = "X"
        else:
            print("Jogada Invalida!!")

##Da a opção do jogador jogar novamente ou sair após o termino de uma uma partida
##e deixa o modo de digitar os valores em letra maiúscula ou minúscula:            

    jogarNovamente = input("Você deseja jogar novamente? [Y(Yes)/N(No)]: ")

    while jogarNovamente != 'Y' and jogarNovamente != 'y' and jogarNovamente != 'N' and jogarNovamente != 'n':
        jogarNovamente = input("Dado invalido. Digite 'Y'(Yes) ou 'N'(No): ")
    else:
        if jogarNovamente == 'Y' or jogarNovamente == 'y':
            inicio = 1
            cs1, cs2, cs3, cs4, cs5, cs6,  cs7, cs8, cs9 = ("1", "2", "3", "4", "5", "6", "7", "8", "9")    
        elif jogarNovamente == 'N' or jogarNovamente == 'n':
            inicio = 2

else:
    print(1 * ("Saindo..."))
    pass

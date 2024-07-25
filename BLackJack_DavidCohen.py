import os
import sys
import time
import random

def exit(): #Função que sai do Programa
    time.sleep(1)
    os.system('cls')
    print ('Fim da execução do programa!')
    time.sleep(1)
    os.system('cls')
    sys.exit()

def error(cause): #Mensagem de erro
    print ('Erro! {}!'.format(cause))
    time.sleep (1)
    while True:
        os.system('cls')
        print('---solucão de erros---')
        print('(1)-> Tentar novamente')
        print('(2)-> Sair')
        choice=input('O que deseja fazer: ')
        if choice == '1':
            break
        elif choice == '2':
            exit()
        else:
            error('escolha invalida')
            continue

def deal(a): #Subprograma que compra uma carta para o jogador
    global deck 
    #Normalmente, variaveis chamadas dentro de uma função, elas não atualizam nada fora dela.
    #a palavra chave "global", serve para permitir a função de alterar variaveis no programa base
    print('dando uma carta para o jogador...')
    i=random.randint(0,len(deck)) # Escolhe um número aleatório entre 0 e o numero de cartas restantes no deck.
    card = deck.pop(i-1) # Retira a carta do deck com base no indice
    if card == '10': #Se o número tiver 2 digitos, desenha a carta de modo ficar alinhada
    
        print("""
            |    |
            | {} |
            |    |""".format(card))
    else: #Caso contrario, desenha de uma forma diferente
        print("""
            |    |
            | {}  |
            |    |""".format(card))

    time.sleep(1) #Espera um segundo
    if card == 'A': #Se a carta for um ás, um algoritmo que deixa voce escolher entre o valor 1 e 11
        if a > 10:
            return 1
        else:
            while True:
                print('(1)-> 1\n(2)-> 11')
                choice = input('Escolha uma opção: ')
                if choice == '1':
                    return 1
                elif choice == '2':
                    return 11
                else:
                    error('Escolha invalida')
                    pass
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return int(card)
    
def deal_dealer(a): #Subprograma que compra uma carta para o dealer (unica diferença sendo que o algoritmo que determina o valor do ás é automático, e não depende de escolha do jogador)
    global deck
    print('Dealer compra uma carta...')
    i=random.randint(0,len(deck))
    card = deck.pop(i-1)
    if card == '10':
    
        print("""
            |    |
            | {} |
            |    |""".format(card))
    else:
        print("""
            |    |
            | {}  |
            |    |""".format(card))
    time.sleep(1)
    if card == 'A':
        if a >10:
            return 1
        else:
            return 11
    elif card == 'J' or card == 'Q' or card == 'K':
        return 10
    else:
        return int(card)
choice = '' #Variável placeholder que vai ser sobreescrita em cada menu.

while True: #Loop do jogo
    while True: #Menu inicial
        os.system('cls')
        print ('------BlackJack------')
        print('(1)-> Iniciar o jogo')
        print('(2)-> Sair')
        choice=input('O que deseja fazer: ')
        if choice == '1': #Se o jogador escolher (1)...
            #Fornece os chips para ambos
            chips = 500
            chips_dealer = 500
            break
        elif choice == '2': #Se o jogador escolher (2)...
            exit() #Sair do programa
            pass
        else:
            error('Escolha invalida')
            pass
    while True: #JOGO
        while True: #Menu dos chips
            os.system('cls')
            print ('------BlackJack------')
            print('Seus chips = {}'.format(chips))
            print('Chips da mesa = {}'.format(chips_dealer))
            if chips > chips_dealer: #se o jogador tiver mais chips que o dealer, a aposta máxima sera igual ao numero de chips do dealer
                maxbet = chips_dealer
            else: #Caso contrario, a aposta máxima sera igual ao número de chips do jogador
                maxbet = chips
            bet = int(input('Digite o valor da sua aposta (max:{}): '.format(maxbet)))
            if bet > maxbet or bet <= 0: #Se o jogador fez uma aposta maior que a máxima ou menor que 0...
                error('Aposta inválida')
                continue
            else: #Caso contrário, peça confirmação da aposta
                confirm = input('Voce deseja apostar {}? Digite S para confirmar.\n'.format(bet))
                if confirm.lower() == 's':
                    chips -= bet
                    chips_dealer += bet
                    game = True
                    break
                else:
                    continue
        #setup do jogo
        print ('iniciando o jogo...')
        time.sleep(1)
        deck = ['A','A','A','A','2','2','2','2','3','3','3','3','4','4','4','4', #Deck de cartas
                '5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8',
                '9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q',
                'K','K','K','K']
        soma_dealer = 0 #Pontuação do dealer
        soma = 0 #Pontuação do jogador
        
        #Dar uma carta para os dois
        soma += deal(soma) 
        soma += deal(soma) 
        soma_dealer += deal_dealer(soma_dealer)
        wincond = False #Variavel booleana que determina se houve condição de fim de jogo automática (alguem estourou ou pontuou 21)
        input('Pressione enter para continuar...')
        os.system('cls')

        while game == True: #O jogo em si (21)
            os.system('cls')
            print ('------BlackJack------')
            print('Sua pontuação atual: {}'.format(soma))
            print('A pontuação  do dealer: {}'.format(soma_dealer))
            print('(1)-> Receber mais uma carta')
            print('(2)-> Parar')
            choice=input('O que deseja fazer: ')
            if choice == '1': #Se o jogador escolher (1)...
                soma += deal(soma) #Dar mais uma carta para o jogador
                #checkar condição de fim de jogo
                if soma > 21: #Se a soma dos pontos do jogador der maior que 21, ele 'estoura'
                    print('Jogador estourou')
                    wincond = True
                    win = 2
                    game = False
                elif soma == 21: #Se a soma dos pontos do jogador der 21, ele vence   
                    print('BlackJack!')
                    wincond = True
                    win = 1
                    game = False
                else: #Caso contrario, o jogo continua
                    continue
            elif choice == '2': #Se o jogador escolher (2)...
                #fase do dealer
                time.sleep (2)
                os.system('cls')
                print ('------BlackJack------')
                print ('turno do Dealer...')
                while soma_dealer < soma: #enquanto os pontos do dealer são menores que os do jogador...
                    os.system('cls')
                    print ('------BlackJack------')
                    soma_dealer += deal_dealer(soma_dealer) #Dê mais uma carta para o dealer
                    print('Sua pontuação atual: {}'.format(soma))
                    print('A pontuação  do dealer: {}'.format(soma_dealer))
                    #checkar condição de fim de jogo
                    if soma_dealer == 21:
                        print('Dealer venceu!') #Se a soma dos pontos do dealer der 21, ele vence
                        wincond = True
                        win = 2
                        game = False
                    elif soma_dealer > 21:
                        print('Dealer estourou!') #Se a soma dos pontos do jogador der maior que 21, ele 'estoura'
                        wincond = True
                        win = 1
                        game = False
                    else: #Caso contrario, o jogo continua
                        pass
                game = False 
            else:
                error('Escolha invalida')
                pass

        if wincond == False: #Se precisar comparar... (ou seja, não houve condição de fim de jogo instantâneo)
            print ('Sua pontuação = {}'.format(soma))
            print('pontuação do Dealer = {}'.format(soma_dealer))
            if soma > soma_dealer:
                win = 1
            else:
                win = 2

        if win == 1: #Jogador vence e recebe seus chips
            print ('jogador venceu! Ganhou {} chips!'.format(bet*2))
            input('Pressione enter para continuar...')
            os.system('cls')
            chips += 2*bet
            chips_dealer -= 2*bet
        else: #Jogador perde e não recebe chips
            print ('Jogador perdeu!')
            input('Pressione enter para continuar...')
            os.system('cls')
        

        print ('Seus chips: {}'.format(chips))
        print('Chips da mesa = {}'.format(chips_dealer))
        time.sleep(1)

        if chips_dealer <= 0: #Se o dealer não tem mais chips...
            Gend =True
            print ('PARABENS!!! Você VENCEU!!')
            input('Pressione enter para continuar...')
            os.system('cls')
        elif chips <=0: #se o jogador não tem mais chips...
            Gend = True
            print('Voce está sem chips! Derrota!')
            input('Pressione enter para continuar...')
            os.system('cls')
        else: #caso contrário, o jogo não acabou
            Gend = False


        if Gend == False: #Se o jogo não acabou ainda...
            #Retorno
            while True: #Menu de retorno (Jogo não acabou ainda)
                os.system('cls')
                print ('------BlackJack------')

                print ('Seus chips: {}'.format(chips))
                print('Chips da mesa = {}'.format(chips_dealer))

                print ('(1)-> Jogar novamente')
                print ('(2) -> Voltar ao menu inicial')
                print ('(3) -> Sair')
                choice = input('O que deseja fazer: ')
                if choice == '1':
                    break
                elif choice == '2':
                    break
                elif choice == '3':
                    exit()
                    pass
                else:
                    error('Escolha invalida')
                    pass
            
            if choice == '1': #Mais uma partida (Voltar para o #JOGO)
                continue
            else: #Voltar ao menu inicial
                break 
        
        else: #Menu de retorno (Jogo acabou)
            while True:
                os.system('cls') 
                print ('------BlackJack------')
                print ('(1) -> Voltar ao menu inicial')
                print ('(2) -> Sair')
                choice = input('O que deseja fazer: ')
                if choice == '1':
                    break
                elif choice == '2':
                    exit()
                    pass        
                else:
                    error('Escolha invalida')
                    pass
            break
        
        
                

                









        














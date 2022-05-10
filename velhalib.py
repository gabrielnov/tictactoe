VAZIA = '.'
MAQUINA = 'O'
HUMANO = 'X'
JOGADAS_VALIDAS = [MAQUINA, HUMANO]
ST_CONTINUA = 1
ST_MAQUINA_GANHOU = 2
ST_HUMANO_GANHOU = 3
ST_EMPATOU = 4

dic_jogadas = {-1: 3, -2: 2, 0: 1, 1:2, 2:3 }

def gerar():
    return [[VAZIA,VAZIA,VAZIA],[VAZIA,VAZIA,VAZIA],[VAZIA,VAZIA,VAZIA]]

def mostrar(tab):
    for i in range(3):
        print(f'{tab[i][0]}|{tab[i][1]}|{tab[i][2]}')
    print()

def jogada_humano(tab):
    valida = False
    while not valida:
        linha = int(input('Linha da sua jogada: '))
        coluna = int(input('Coluna da sua jogada: '))
        if linha>=1 and linha<=3 and coluna>=1 and coluna<=3 and tab[linha-1][coluna-1] == VAZIA:
            valida = True
        else:
            print('Jogada inválida!')
    return [linha, coluna]

def jogada_maquina(tab): 
    
    for i in range(3):
        for j in range(3):
              if tab[i][j] == HUMANO:

                # linha
                if tab[i][j - 1] == HUMANO:
                    if tab[i][j-2] not in JOGADAS_VALIDAS:                        
                        return [i, j - 2]
                if tab[i][j - 2] == HUMANO:
                    if tab[i][j-1] not in JOGADAS_VALIDAS:
                        return [i, j - 1]

                # coluna
                if tab[i-1][j] == HUMANO:
                    if tab[i-2][j] not in JOGADAS_VALIDAS:                        
                        return [i-2, j]
                if tab[i-2][j] == HUMANO:
                    if tab[i-1][j] not in JOGADAS_VALIDAS:                       
                        return [i-1, j]

                # diagonal
                if tab[1][1] == HUMANO:
                    if tab[i-2][j-1] not in JOGADAS_VALIDAS:                        
                        return [i-2, j-1]
                if tab[i-1][j-1] == HUMANO:
                    if tab[1][1] not in JOGADAS_VALIDAS:                        
                        return [1, 1]        
                if tab[i-2][j-1] == HUMANO:
                    if tab[1][1] not in JOGADAS_VALIDAS:                        
                        return [1, 1]
    
    for i in range(3):
        for j in range(3):
            if tab[i][j] == '.':
                return [i,j]
                    

def atualizar(tab, jogada, jogador):
    if jogador == MAQUINA:
        i = jogada[0]
        j = jogada[1]
    if jogador == HUMANO:
        i = jogada[0] -1
        j = jogada[1] -1
    tab[i][j] = jogador

def ganhou(t, jogador):
    for i in range(3):
        if t[i][0]==jogador and t[i][1]==jogador and t[i][2]==jogador:
            return True
        if t[0][i]==jogador and t[1][i]==jogador and t[2][i]==jogador:
            return True
    if t[0][0]==jogador and t[1][1]==jogador and t[2][2]==jogador:
        return True
    if t[0][2]==jogador and t[1][1]==jogador and t[2][0]==jogador:
        return True
    return False

def todas_ocupadas(t):
    for i in range(3):
        for j in range(3):
            if t[i][j]==VAZIA:
                return False
    return True
    
def verificar(tab):
    if ganhou(tab, HUMANO):
        return ST_HUMANO_GANHOU
    elif ganhou(tab, MAQUINA):
        return ST_MAQUINA_GANHOU
    elif todas_ocupadas(tab):
        return ST_EMPATOU
    else:
        return ST_CONTINUA

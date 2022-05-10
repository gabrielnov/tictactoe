VAZIA = '.'
MAQUINA = 'O'
HUMANO = 'X'
ST_CONTINUA = 1
ST_MAQUINA_GANHOU = 2
ST_HUMANO_GANHOU = 3
ST_EMPATOU = 4

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
                if tab[i][j - 2] == HUMANO:
                    return [i, j - 3]
                if tab[i][j - 3] == HUMANO:
                    return [i, j - 2]

                # coluna
                if tab[i-1][j] == HUMANO:
                    return [i-3, j]
                if tab[1-2][j] == HUMANO:
                    return [i-2, j]

                # diagonal
                if tab[1][1] == HUMANO:
                    return [i-3, j-3]
    
    for i in range(3):
        for j in range(3):
            if tab[i][j] == '.':
                return [i,j]
                    

def atualizar(tab, jogada, jogador):
    i = jogada[0]-1
    j = jogada[1]-1
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


import random

from velhalib import *
    
tabuleiro = gerar()

sorteio = random.randint(1,2)
if sorteio == 1:
    jogador = HUMANO
else:
    jogador = MAQUINA

status = ST_CONTINUA
while status == ST_CONTINUA:
    mostrar(tabuleiro)
    if jogador == HUMANO:
        jogada = jogada_humano(tabuleiro)
    elif jogador == MAQUINA:
        jogada = jogada_maquina(tabuleiro)
        print(f'Joguei na linha {dic_jogadas[jogada[0]]} e na coluna {dic_jogadas[jogada[1]]}...')
    atualizar(tabuleiro, jogada, jogador)
    
    status = verificar(tabuleiro)
    if jogador == HUMANO:
        jogador = MAQUINA
    elif jogador == MAQUINA:
        jogador = HUMANO

mostrar(tabuleiro)

if status == ST_HUMANO_GANHOU:
    print('Você me venceu!')
elif status == ST_MAQUINA_GANHOU:
    print('Eu venci!')
elif status == ST_EMPATOU:
    print('Empatamos...')
    

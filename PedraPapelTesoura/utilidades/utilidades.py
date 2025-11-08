from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

def computador_joga():
    escolha = choice(jogadas)
    return escolha

def quem_ganhou(escolha_computador, escolha_jogador):
    
    computador = jogadas.index(escolha_computador)
    jogador = jogadas.index(escolha_jogador)
    resultados=[
        [0,1,2],
        [2,0,1],
        [1,2,0]
        ]
    
    return resultados[jogador][computador]

if __name__ == '__main__':
    
    computador = 'tesoura'
    jogador = 'papel'
    r = quem_ganhou(computador, jogador)
    print(r)
"""
Jogo do Pedra Papel Tesoura

arquivo principal com a GUI feita em FreeSimpleGUI
https://pypi.org/project/FreeSimpleGUI/

no arquivo atual temos somente as definições da GUI do usuario
as funções que implementam o jogo estão no arquivo utilidades.py

data: 30/10/2025
autor: Joao Santanna
"""

import FreeSimpleGUI as sg
import sys
import os
from utilidades.utilidades import computador_joga, quem_ganhou


def novo_jogo(janela):
    """
    função que restaura a janela de jogo ao padrao inicial
    habilita botoes e reseta textos

    argumento: passar a variavel janela como argumento , janela aqui
    define a tela principal do jogo.

    retorno : 0 caso funcione sem erros
    """
    # habilita botoes
    janela["-PEDRA-"].update(disabled=False)
    janela["-PAPEL-"].update(disabled=False)
    janela["-TESOURA-"].update(disabled=False)
    # desaparece botao de final de jogo
    janela["-NOVO-"].update(visible=False)
    janela["-SAIR-"].update(visible=False)
    # reseta textos
    janela["-COMP-"].update("Computador:")
    janela["-JOG-"].update("Jogador:")
    janela["-PLACAR-"].update("Computador: 0 x Jogador: 0")
    janela["-FINAL-"].update("")
    return 0


# desenhar a tela

diretorio_app = os.path.dirname(os.path.abspath(__file__))
caminho_completo = os.path.join(diretorio_app, "imagem", "ilustracao3.png")
#print(caminho_completo)

desenho = [
    [sg.VPush()],
    [
        sg.Push(),
        #sg.Image(r"C:\Users\jsant\VSCodeProj\50Projetos\Free_simpleGUi\PedraPapelTesoura\imagem\ilustracao3.png"),
        sg.Image(source=caminho_completo),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Text(
            "Pedra Papel Tesoura", font=("Helvetica", 18), text_color="Yellow", pad=15
        ),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Button("Pedra", size=(8, 1), key="-PEDRA-"),
        sg.Button("Papel", size=(8, 1), key="-PAPEL-"),
        sg.Button("Tesoura", size=(8, 1), key="-TESOURA-"),
        sg.Push(),
    ],
    [sg.T("Computador:", key="-COMP-")],
    [sg.T("Jogador:", key="-JOG-")],
    [sg.Push(), sg.T(key="-SAIDA-", font=("Arial", 16)), sg.Push()],
    [sg.T("Computador: 0 x Jogador: 0", key="-PLACAR-")],
    [sg.Push(), sg.T(key="-FINAL-", text_color="Yellow"), sg.Push()],
    [
        sg.Push(),
        sg.Button("Novo jogo", size=(8, 1), key="-NOVO-", visible=False),
        sg.Button("Sair", size=(8, 1), key="-SAIR-", visible=False),
    ],
    [sg.VPush()],
]

janela = sg.Window("Jokenpô", font=("Helvetica", 14), layout=desenho, size=(500, 450))

# a função que avalia quem ganhou uma rodada retorna 0 se empate ,
# 1 - se o computador ganhou , 2 - se o jogador ganhou ,
# exatamente os indices da lista a seguir
ganhou = ["empate", "computador", "jogador"]

# controle do Placar - com 3 vitorias jogo acaba
comp = 0
jog = 0


while True:
    evento, valores = janela.read()

    if evento in (sg.WIN_CLOSED, "-SAIR-"):
        break
    if evento == "-PEDRA-":
        r = computador_joga()  # retorna a escolha do computador(pedra, papel, tesoura)

        # funcao quem ganhou recebe a escolha do computador e a escolha do jogador
        ganhador = quem_ganhou(r, "pedra")
        # funcao quem ganhou retorna 0 ,1 ou 2 para indicar o vencedor ...
        resultado = ganhou[ganhador]  # lista usada para ver quem venceu
        if ganhador == 1:
            comp += 1
        if ganhador == 2:
            jog += 1
        # atualiza interface com dados da rodada
        janela["-COMP-"].update(f"Computador:{r}")
        janela["-JOG-"].update("Jogador:pedra")
        janela["-SAIDA-"].update(f" {resultado} ganhou")
        janela["-PLACAR-"].update(f"Computador: {comp} x Jogador: {jog}")

    if evento == "-PAPEL-":
        r = computador_joga()
        ganhador = quem_ganhou(r, "papel")
        resultado = ganhou[ganhador]

        if ganhador == 1:
            comp += 1
        if ganhador == 2:
            jog += 1
        # atualiza interface com dados da rodada
        janela["-COMP-"].update(f"Computador:{r}")
        janela["-JOG-"].update("Jogador:papel")
        janela["-SAIDA-"].update(f" {resultado} ganhou")
        janela["-PLACAR-"].update(f"Computador: {comp} x Jogador: {jog}")

    if evento == "-TESOURA-":
        r = computador_joga()
        ganhador = quem_ganhou(r, "tesoura")
        resultado = ganhou[ganhador]

        if ganhador == 1:
            comp += 1
        if ganhador == 2:
            jog += 1
        # atualiza interface com dados da rodada
        janela["-COMP-"].update(f"Computador:{r}")
        janela["-JOG-"].update("Jogador:tesoura")
        janela["-SAIDA-"].update(f" {resultado} ganhou")
        janela["-PLACAR-"].update(f"Computador: {comp} x Jogador: {jog}")

    # testar se jogo acabou e colocar a possibilidade de novo jogo
    if comp == 3:
        print("teste")
        janela["-FINAL-"].update(f"GAME OVER - COMPUTADOR VENCEU")
        # desabilita os botoes
        janela["-PEDRA-"].update(disabled=True)
        janela["-PAPEL-"].update(disabled=True)
        janela["-TESOURA-"].update(disabled=True)
        janela["-NOVO-"].update(visible=True)
        janela["-SAIR-"].update(visible=True)
    if jog == 3:
        janela["-FINAL-"].update(f"GAME OVER - VOCE VENCEU")
        # desabilita os botoes
        janela["-PEDRA-"].update(disabled=True)
        janela["-PAPEL-"].update(disabled=True)
        janela["-TESOURA-"].update(disabled=True)
        janela["-NOVO-"].update(visible=True)
        janela["-SAIR-"].update(visible=True)

    if evento == "-NOVO-":
        # reseta janela
        novo_jogo(janela)
        # zera placar
        comp = 0
        jog = 0

janela.close()
sys.exit()

# TODO:
# - Melhorar interface ( justificando textos)
# - criar o jogo melhor de 3
# - criar um menu ( novo jogo, sair)
# - colocar a area de texto dentro de um container com linha , fica mais estiloso
# - docstring da interface

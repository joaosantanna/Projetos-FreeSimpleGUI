'''
descrição geral do aplicativo

arquivo principal com a GUI feita em FreeSimpleGUI
https://pypi.org/project/FreeSimpleGUI/

data: 04/11/2025
autor: Joao Santanna
'''

import  FreeSimpleGUI as sg
import sys

desenho = []


janela = sg.Window('nome do aplicativo',layout = desenho)

while True:
    
    eventos, valores = janela.read()
    
    if eventos == sg.WIN_CLOSED:
        break
    
janela.close()
sys.exit()
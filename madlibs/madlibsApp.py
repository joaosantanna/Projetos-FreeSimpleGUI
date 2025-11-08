import FreeSimpleGUI as sg
from madlibs_base import madlibs, listas_default
import io

"""
Aplicativo madlibs = forma frases malucas com as
entradas do usuario

data: 23/10/2025

entradas : as escolhas de personagens , adjetivos e verbos para montagem da frase

saidas: uma frase montada ao acaso usando as entradas

autor: Joao Santanna
"""

sg.theme("LightBlue6")

listas_padrao = listas_default()
personagens = listas_padrao["personagens"]
adjetivos = listas_padrao["adjetivos"]
verbos = listas_padrao["verbos"]

sg.theme('Material2')

layout = [
    [
        sg.Push(),
        sg.Text("Madlibs - Frases aleatorias para alegra seu dia", font=("arial", 18)),
        sg.Push(),
    ],
    [
        sg.Text("Personagens"),
    ],
    [
        sg.Push(),
        sg.Combo(
            personagens, key="personagem1", size=(12, 10), default_value=personagens[0]
        ),
        sg.Combo(
            personagens, key="personagem2", size=(12, 10), default_value=personagens[0]
        ),
        sg.Combo(
            personagens, key="personagem3", size=(12, 10), default_value=personagens[0]
        ),
        sg.Combo(
            personagens, key="personagem4", size=(12, 10), default_value=personagens[0]
        ),
        sg.Push(),
    ],
    [
        sg.Text("Adjetivos"),
    ],
    [
        sg.Push(),
        sg.Combo(adjetivos, key="adjetivo1", size=(12, 10), default_value=adjetivos[0]),
        sg.Combo(adjetivos, key="adjetivo2", size=(12, 10), default_value=adjetivos[0]),
        sg.Combo(adjetivos, key="adjetivo3", size=(12, 10), default_value=adjetivos[0]),
        sg.Combo(adjetivos, key="adjetivo4", size=(12, 10), default_value=adjetivos[0]),
        sg.Push(),
    ],
    [
        sg.Text("Verbos"),
    ],
    [
        sg.Push(),
        sg.Combo(verbos, key="verbo1", size=(12, 10), default_value=verbos[0]),
        sg.Combo(verbos, key="verbo2", size=(12, 10), default_value=verbos[0]),
        sg.Combo(verbos, key="verbo3", size=(12, 10), default_value=verbos[0]),
        sg.Combo(verbos, key="verbo4", size=(12, 10), default_value=verbos[0]),
        sg.Push(),
    ],
    [
        sg.Push(),
        sg.Multiline(default_text=" :-)", size=(60, 8), key="-OUT-"),
        sg.Push(),
    ],
    [sg.Button("Formar Frase"), sg.Button("Aleatorizar!!!")],
]


janela = sg.Window("Mad Libs app", layout=layout, font=("arial", 12))

while True:

    botao, valor = janela.read()
    print(botao)

    if botao == sg.WIN_CLOSED:
        break
    elif botao == "Formar Frase":
        personagens = [
            valor["personagem1"],
            valor["personagem2"],
            valor["personagem3"],
            valor["personagem4"],
        ]
        adjetivos = [
            valor["adjetivo1"],
            valor["adjetivo2"],
            valor["adjetivo3"],
            valor["adjetivo4"],
        ]
        verbos = [
            valor["verbo1"],
            valor["verbo2"],
            valor["verbo3"],
            valor["verbo4"],
        ]

        frase = madlibs(personagens, adjetivos, verbos)
        janela["-OUT-"].Update(frase)
    elif botao == "Aleatorizar!!!":
        frase = madlibs()
        janela["-OUT-"].Update(frase)

janela.close()

# TODO:
# - mudar os combo box para uma serie e checkbox com os nomes do lado , acho que
# vai ficar mais intuitivo
# - verificar os comentarios e gerar os docs
# - tratar aquele bug dos elementos que são retirados da lista e que gera aquele crash
# - verificar como colocar as imagens no app - isso nao funciona nessa versao da biblioteca?
# - tentar alternativamente colocar um filebutton para pegar o caminho do arquivo e passar como argumento

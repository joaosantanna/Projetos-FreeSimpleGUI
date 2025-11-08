"""
Calculador de IMC - Indice de massa corporal ,
baseado na formula imc = peso/altura^2

arquivo principal com a GUI feita em FreeSimpleGUI
https://pypi.org/project/FreeSimpleGUI/

data: 04/11/2025
autor: Joao Santanna
"""
import sys
import FreeSimpleGUI as sg

sg.theme('Material2')

desenho = [
    [sg.VPush()],
    [
        sg.Image(
            r"C:\Users\jsant\VSCodeProj\50Projetos\Free_simpleGUi\calculadora_IMC\balanca2.png",
        )
    ],
    [sg.Text("Peso:"), sg.Input(key="-PESO-", size=(10, 1))],
    [sg.Text("Altura:"), sg.Input(key="-ALTURA-", size=(10, 1))],
    [sg.Button("Calcular")],
    [sg.Text(key="-SAIDA-")],
    [sg.VPush()],
]


janela = sg.Window(
    "Calculadora IMC",
    layout=desenho,
    font="Helvetica 14",
    size=(400, 300),
    element_justification="c",
)

while True:

    eventos, valores = janela.read()

    if eventos == sg.WIN_CLOSED:
        break
    if eventos == "Calcular":
        peso = float(janela["-PESO-"].get())
        altura = float(janela["-ALTURA-"].get())
        imc = peso / altura**2
        MENSAGEM = ""
        if imc < 20:
            MENSAGEM = "Abaixo do peso ideal"
        elif imc >= 20 and imc < 25:
            MENSAGEM = "Peso ideal"
        else:
            MENSAGEM = "Sobre peso"
        janela["-SAIDA-"].update(f"IMC = {imc:.2f} - {MENSAGEM}")

janela.close()
sys.exit()

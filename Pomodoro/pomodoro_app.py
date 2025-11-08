"""
Pomodoro - projeto para criar um timer para usar com
a metodologia pomodoro de produtividade

arquivo principal com a GUI feita em FreeSimpleGUI
https://pypi.org/project/FreeSimpleGUI/

no arquivo atual temos somente as definições da GUI do usuario
as funções que implementam o jogo estão no arquivo utilidades.py

data: 01/11/2025
autor: Joao Santanna
"""

import FreeSimpleGUI as sg

# --- Definição do Layout da Janela ---
sg.theme("Material2")

layout = [
    [
        sg.Image(
            r"C:\Users\jsant\VSCodeProj\50Projetos\Free_simpleGUi\Pomodoro\tomate4.png",
            size=(100, 100),
        )
    ],
    [sg.Text("Defina o tempo:", font="Elephant 14")],
    [
        sg.Text("Minutos:"),
        sg.Spin(
            [i for i in range(60)],
            initial_value=5,
            key="-MINUTES-",
            size=(3, 1),
            font=("Arial 12"),
            background_color="#f46037",
        ),
        sg.Text("Segundos:"),
        sg.Spin(
            [i for i in range(60)],
            initial_value=0,
            key="-SECONDS-",
            size=(3, 1),
            font=("Arial 12"),
            background_color="#f46037",
        ),
    ],
    [sg.Text("00:00", key="-TIMER-", font="Elephant 50", justification="center")],
    [
        sg.Button(
            "Iniciar",
            key="-START_STOP-",
            size=(10, 2),
            font=("Arial 12"),
            button_color=("white", "#f46037"),
        )
    ],
]

# --- Criação da Janela ---
window = sg.Window("My Pomodoro", layout, element_justification="c")

# --- Variáveis de Controle do Timer ---
running = False
remaining_seconds = 0

# --- Loop de Eventos ---
while True:
    # O 'timeout' faz com que a janela seja lida a cada 1000ms(1 segundo), permitindo a atualização do timer
    event, values = window.read(timeout=1000)

    # Se a janela for fechada, o loop termina
    if event == sg.WIN_CLOSED:
        break

    # --- Lógica do Botão Iniciar/Parar ---
    if event == "-START_STOP-":
        if not running:
            # Pega os valores dos Spinbox
            minutes = int(values["-MINUTES-"])
            seconds = int(values["-SECONDS-"])

            # Calcula o total de segundos para o timer terminar.
            remaining_seconds = minutes * 60 + seconds

            # Só começa se o tempo for maior que zero
            if remaining_seconds > 0:
                running = True
                window["-START_STOP-"].update("Parar")  # Muda o texto do botão
        else:
            # Para o timer
            running = False
            window["-START_STOP-"].update("Iniciar")  # Muda o texto do botão

    # --- Lógica de Atualização do Timer (ocorre a cada 1000ms - 1 segundo) ---
    if running:
        # Diminui o tempo restante
        remaining_seconds -= 1

        # Se o tempo acabar
        if remaining_seconds <= 0:
            running = False
            window["-START_STOP-"].update("Iniciar")
            window["-TIMER-"].update("00:00")
            sg.popup_auto_close(
                "Pomodoro Esgotado!",
                auto_close_duration=15,
                title="Fim do pomodoro!",
                button_color=("white", "#f46037"),
            )
        else: # se nao é pq o timer ainda está rodando
            # Formata o tempo restante em MM:SS
            mins, secs = divmod(remaining_seconds, 60)
            time_string = f"{mins:02d}:{secs:02d}"  # formata minutos com duas casas decimais e zero d ( decimal - inteiro)
            # formata segundos do mesmo jeito

            # Atualiza o texto na tela
            window["-TIMER-"].update(time_string)

# --- Fecha a Janela ao sair do loop ---
window.close()

# ------------------------------- #
# Importações Bibliotécas Aux.
import os
import time
import PySimpleGUI as sg
from datetime import date
# ------------------------------- #

sg.theme('Reddit')

data = date.today()

layout = [
    [sg.Text('Programar Desligamento [Lab Santxsz]')],
    [sg.Text('')],
    [sg.Text('Definir Tempo')],
    [sg.Input(key='tempo')],
    [sg.Checkbox('Minutos', key='min'), sg.Checkbox('Horas', key='horas'), sg.Checkbox('Dias', key='dias')],
    [],
    [],
    [sg.Button('Programar Desligamento'), sg.Button('Adiar Desligamento')],
]

# Janela
janela = sg.Window('Programar Desligamento', layout)

while True:
    eventos, valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Programar Desligamento':
        sg.popup_notify('Programação Feita - Sucesso!')

        if not valores['tempo']:
            sg.popup_error('Defina um Tempo')
    
        if valores['min']:
            tempo = int(valores['tempo'])
            calculo = tempo * 60
            print(calculo)

        elif valores['horas']:
            tempo = int(valores['tempo'])
            calculo = tempo * 3600
            print(calculo)

        elif valores['dias']:
            tempo = int(valores['tempo'])
            calculo = tempo * 86400
            print(calculo)

        os.system("shutdown /s /t {}".format(calculo))

    if eventos == 'Adiar Desligamento':
        sg.popup_notify('Desligamento Adiado - Sucesso!')
        os.system("shutdown /a")
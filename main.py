import PySimpleGUI as sg
import pandas as pd
from datetime import date

sg.theme('DarkPurple1')

today = date.today()
EXCEL_FILE = r'C:\Users\hauta\Desktop\raid\Data.xlsx'
df = pd.read_excel(EXCEL_FILE)

pelaajat = ['asd','asd124','dfhdhf','tööt']
rankit = ['Silver I','Silver II', 'Silver III','Silver IV','Silver V','Gold I','Gold II','Gold III','Gold IV','Gold V','Platina']

alku = [
    [sg.Button('Uusi pelaaja'),sg.Button('CB')]
]

uusiDataPointti = [
    [sg.Text('Tähän muhlun data:')],
    [sg.Text('Nimi', size=(15,1)), sg.InputText(key='Nimi')],
    [sg.Text('Player power', size=(15,1)), sg.InputText(key='Player Power', size=(10))],
    [sg.Text('Clan XP', size=(15,1)), sg.InputText(key='Clan XP', size=(10))],
    [sg.Text('Arena rankki', size=(15,1)), sg.Combo(rankit, key='Arena rankki')],
    [sg.Text('Pvm', size=(15,1)), sg.InputText(today.strftime('%d/%m/%Y'),key='Pvm',disabled=True, size=(10))],

    [sg.Submit(),sg.Button('Takasin')]

]

CB = [
    [sg.Text('Tähän muhlun CB data')],
    [sg.Text('Nimi', size=(15,1)), sg.InputText(key='Nimi')],
    [sg.Text('Taso', size=(15,1)),
        sg.Checkbox('Brutal', key='Brutal'),
        sg.Checkbox('NM', key='NM'),
        sg.Checkbox('UNM', key='UNM')
    ],
    [sg.Text('Pvm', size=(15,1)), sg.InputText(today.strftime('%d/%m/%Y'),key='Pvm',disabled=True, size=(10))],

    [sg.Submit(),sg.Button('Takasin')]
]

def clear_input():
    for key in values:
        window[key]('')
    return None

layout = [
    [sg.Column(alku, key='-COL1-'), sg.Column(uusiDataPointti, visible=False, key='-COL2-'), sg.Column(CB, visible=False,key='-COL3-')]
]

window = sg.Window('Mäyräkoirien virrallinen datamasiina', layout)

layout = 1

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Uusi pelaaja':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 2
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'CB':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 3
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()

    if event == 'Takasin':
        window[f'-COL{layout}-'].update(visible=False)
        layout = 1
        window[f'-COL{layout}-'].update(visible=True)

    if event == 'Tyhjää':
        clear_input()

window.close()
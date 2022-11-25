import PySimpleGUI as sg
import pandas as pd
from datetime import date

sg.theme('DarkPurple1')

today = date.today()
EXCEL_FILE = r'C:\Users\hauta\Desktop\raid\Data.xlsx'
df = pd.read_excel(EXCEL_FILE)

pelaajat = ['asd','asd124','dfhdhf','tööt']
rankit = ['Silver I','Silver II', 'Silver III','Silver IV','Silver V','Gold I','Gold II','Gold III','Gold IV','Gold V','Platina']

def alkuIkkuna():  
    alku = [
        [sg.Button('Uusi pelaaja'),sg.Button('CB')]
    ]
    return sg.Window('Aloitus ikkuna', alku, finalize=True)

def uusiDataPointtiIkkuna():
    uusiDataPointti = [
        [sg.Text('Tähän muhlun data:')],
        [sg.Text('Nimi', size=(15,1)), sg.InputText(key='Nimi')],
        [sg.Text('Player power', size=(15,1)), sg.InputText(key='Player Power', size=(10))],
        [sg.Text('Clan XP', size=(15,1)), sg.InputText(key='Clan XP', size=(10))],
        [sg.Text('Arena rankki', size=(15,1)), sg.Combo(rankit, key='Arena rankki')],
        [sg.Text('Pvm', size=(15,1)), sg.InputText(today.strftime('%d/%m/%Y'),key='Pvm',disabled=True, size=(10))],
        [sg.Submit(),sg.Button('Takasin')]
    ]
    return sg.Window('Uusi datapointti', uusiDataPointti, finalize=True)

def CBIkkuna():
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
    return sg.Window('CB', CB, finalize=True)

def clear_input(window, values):
    for key in values:
        window[key]('')
    return None

alku, UDP, CB = alkuIkkuna(), None, None

while True:
    event1, values1 = alku.read()

    if event1 == sg.WIN_CLOSED or event1 == 'Exit':
        break

    if event1 == 'Uusi pelaaja':
        UDP = uusiDataPointtiIkkuna()
        while True:
            event2, values2 = UDP.read()

            if event2 == 'Tyhjää':
                clear_input(UDP,values2)
            
            if event2 == 'Takaisin':
                UDP.close()
                UDP = None
                break


    if event1 == 'CB':
        CB = CBIkkuna()
        while True:
            event3, values3 = CB.read()

            if event3 == 'Tyhjää':
                clear_input(CB,values3)
            
            if event3 == 'Takaisin':
                CB.close()
                CB = None
                break

alku.close()
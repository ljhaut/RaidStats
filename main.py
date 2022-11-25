import PySimpleGUI as sg
import pandas as pd
from datetime import date


sg.theme('DarkPurple1')

today = date.today()

EXCEL_FILE = r'C:\Users\hauta\Desktop\raid\Data.xlsx'

pelaajat = []
for x in pd.read_excel(EXCEL_FILE, sheet_name='Klaani').Nimi:
    pelaajat.append(x)

Pvms = []
for x in pd.read_excel(EXCEL_FILE, sheet_name='Klaani').Pvm:
    Pvms.append(x)

rankit = ['Silver I','Silver II', 'Silver III','Silver IV','Silver V','Gold I','Gold II','Gold III','Gold IV','Gold V','Platina']


def alkuIkkuna():  
    alku = [
        [sg.Button('Uusi pelaaja'),sg.Button('CB'),sg.Button('Pelaajat')]
    ]
    return sg.Window('Aloitus ikkuna', alku, finalize=True, resizable=True)

def uusiDataPointtiIkkuna():
    uusiDataPointti = [
        [sg.Text('Tähän muhlun data:')],
        [sg.Text('Nimi', size=(15,1)), sg.InputText(key='Nimi')],
        [sg.Text('Player power', size=(15,1)), sg.InputText(key='Player Power', size=(10))],
        [sg.Text('Clan XP', size=(15,1)), sg.InputText(key='Clan XP', size=(10))],
        [sg.Text('Arena rankki', size=(15,1)), sg.Combo(rankit, key='Arena rankki')],
        [sg.Text('Pvm', size=(15,1)), sg.InputText(today.strftime('%d/%m/%Y'),key='Pvm',disabled=True, size=(10))],
        [sg.Submit(),sg.Button('Tyhjää')]
    ]
    return sg.Window('Uusi datapointti', uusiDataPointti, finalize=True)

def CBIkkuna():
    CB = [
        [sg.Text('Tähän muhlun CB data')],
        [sg.Text('Nimi', size=(15,1)), sg.Combo(pelaajat, key='Nimi')],
        [sg.Text('Taso', size=(15,1)),
            sg.Checkbox('Brutal', key='Brutal'),
            sg.Checkbox('NM', key='NM'),
            sg.Checkbox('UNM', key='UNM')
        ],
        [sg.Text('Pvm', size=(15,1)), sg.InputText(today.strftime('%d/%m/%Y'),key='Pvm',disabled=True, size=(10))],
        [sg.Submit(),sg.Button('Tyhjää')]
    ]
    return sg.Window('CB', CB, finalize=True)

def PelaajatIkkuna():
    Pelaajat = [
        [sg.Text('Valitse mäyris ja mitä tutkaillaan')],
        [sg.Text('Nimi',size=(15,1)), sg.Combo(pelaajat, key='Nimi')]
    ]
    return sg.Window('Pelaajat', Pelaajat, finalize=True)

def clear_input(window, values):
    for key in values:
        if(key =='Pvm'):
            continue
        window[key]('')
    return None

alku, UDP, CB, Pelaajat = alkuIkkuna(), None, None, None

while True:
    event1, values1 = alku.read()

    if event1 == sg.WIN_CLOSED or event1 == 'Exit':
        break

    if event1 == 'Uusi pelaaja':
        UDP = uusiDataPointtiIkkuna()
        while True:
            
            event2, values2 = UDP.read()

            if event2 == sg.WIN_CLOSED or event2 == 'Exit':
                break

            if event2 == 'Tyhjää':
                clear_input(UDP,values2)
            
            if event2 == 'Submit':
                df = pd.read_excel(EXCEL_FILE, sheet_name='Klaani')
                print (df)
                df = df.append(values2, ignore_index=True)
                with pd.ExcelWriter(EXCEL_FILE, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, sheet_name='Klaani', index=False)
                clear_input(UDP, values2)


            
        UDP.close()


    if event1 == 'CB':
        CB = CBIkkuna()
        while True:
            
            event3, values3 = CB.read()

            if event3 == sg.WIN_CLOSED or event3 == 'Exit':
                break

            if event3 == 'Tyhjää':
                clear_input(CB,values3)
            
            if event3 == 'Submit':
                df = pd.read_excel(EXCEL_FILE, sheet_name='CB')
                df = df.append(values3, ignore_index=True)
                with pd.ExcelWriter(EXCEL_FILE, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, sheet_name='CB', index=False)
                clear_input(CB,values3)

        CB.close()

    if event1 == 'Pelaajat':
        Pelaajat = PelaajatIkkuna()
        while True:

            event4, values4 = Pelaajat.read()

            if event4 == sg.WIN_CLOSED or event4 == 'Exit':
                break
        
        Pelaajat.close()
        
alku.close()
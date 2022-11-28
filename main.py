import PySimpleGUI as sg
import pandas as pd
import json
from datetime import date

sg.theme('DarkPurple1')

today = date.today()

JSON_FILE = 'Data.json'

pelaajat = []
with open(JSON_FILE) as json_file:
    for x in json.load(json_file)['Klaani']:
        if pelaajat.__contains__(x['Nimi']):
            continue
        pelaajat.append(x['Nimi'])
    json_file.close()

pvms = []
with open(JSON_FILE) as json_file:
    for x in json.load(json_file)['Klaani']:
        if pvms.__contains__(x['Pvm']):
            continue
        pvms.append(x['Pvm'])
    json_file.close()

print(pelaajat, pvms)

rankit = ['Silver I','Silver II', 'Silver III','Silver IV','Silver V','Gold I','Gold II','Gold III','Gold IV','Gold V','Platina']


def alkuIkkuna():  
    alku = [
        [sg.Button('Uusi pelaaja'),sg.Button('CB'),sg.Button('Pelaajat')]
    ]
    return sg.Window('Mäyristen juhladatasovellus', alku, finalize=True, resizable=True,margins=(65,10))

def uusiDataPointtiIkkuna():
    uusiDataPointti = [
        [sg.Text('Tähän muhlun data:')],
        [sg.Text('Nimi', size=(15,1)), sg.InputText(key='Nimi')],
        [sg.Text('Player power', size=(15,1)), sg.InputText(key='Player power', size=(10))],
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
        [sg.Text('Valitse mäyris, mitä tutkaillaan ja millä aikavälillä')],
        [sg.Text('Nimi',size=(15,1)), sg.Combo(pelaajat, key='Nimi')],
        [sg.Text('1. Pvm', size=(15,1)), sg.Combo(pvms, key='pvm1')],
        [sg.Text('2. Pvm', size=(15,1)), sg.Combo(pvms, key='pvm2')],
        [sg.Text('Tutkailun kohde', size=(15,1)), sg.Combo(['Player power','Clan XP'], key='kohde')],
        [sg.Submit()]
    ]
    return sg.Window('Pelaajat', Pelaajat, finalize=True)

def clear_input(window, values):
    for key in values:
        if(key =='Pvm'):
            continue
        window[key]('')
    return None

def write_json(data, file=JSON_FILE):
    with open (file, 'w') as f:
        json.dump(data, f, indent=4)
    f.close()


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
                with open(JSON_FILE) as json_file:
                    data = json.load(json_file)
                    temp = data['Klaani']
                    temp.append(values2)
                json_file.close()

                write_json(data)
                
                clear_input(UDP,values2)

            
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
                with open(JSON_FILE) as json_file:
                    data = json.load(json_file)
                    temp = data['CB']
                    temp.append(values3)
                json_file.close()

                write_json(data)
                
                clear_input(CB,values3)

        CB.close()

    if event1 == 'Pelaajat':
        Pelaajat = PelaajatIkkuna()
        while True:

            event4, values4 = Pelaajat.read()

            if event4 == sg.WIN_CLOSED or event4 == 'Exit':
                break

            if event4 == 'Tyhjää':
                clear_input(Pelaajat,values4)
            
            if event4 == 'Submit':
                if values4['pvm1']<values4['pvm2']:
                    pvm1 = values4['pvm1']
                    pvm2 = values4['pvm2']
                else:
                    pvm1 = values4['pvm2']
                    pvm2 = values4['pvm1']

                match values4['kohde']:
                    case 'Player power':
                        with open(JSON_FILE) as f:
                            for x in json.load(f)['Klaani']:
                                if x['Pvm'] == pvm1:
                                    data1 = x
                                if x['Pvm'] == pvm2:
                                    data2 = x
                            f.close()
                        print(data1,data2)
                        sg.popup('Player power muutos: ', int(data2['Player power'])-int(data1['Player ower']))
                        
                    case 'Clan XP':
                        with open(JSON_FILE) as f:
                            for x in json.load(f)['Klaani']:
                                if x['Pvm'] == pvm1:
                                    data1 = x
                                if x['Pvm'] == pvm2:
                                    data2 = x
                            f.close()
                        sg.popup('Clan XP muutos: ', int(data2['Clan XP'])-int(data1['Clan XP']))

        Pelaajat.close()
        
alku.close()
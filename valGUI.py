import PySimpleGUI as sg

'''
def the_factor(base=6):
	estWeight=int(input("Enter the estimated weight: "))
	raw_num =(estWeight*base)/167
	print(base*round(raw_num/base))

the_factor() '''


layout = [
    [sg.Text('Estimated Weight', size=(20,1)), sg.InputText(key='Estimated Weight')], 
    [sg.Button(button_text='Calculate!'),sg.Exit()],[sg.Text('Valuation:'), sg.Text("", size=(0, 1), key='Valuation')]
]

window = sg.Window('CSR Job Aide', layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Calculate!':
        for value in values:
            if 'Estimated Weight' in values:
                weight = int((values.get('Estimated Weight')))
                raw_num = weight*6/167
                valuation = 6*round(raw_num/6)
                #print (valuation)
                window['Valuation'].update(value=f"${valuation}.00")
window.close()
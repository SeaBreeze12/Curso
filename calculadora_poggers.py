import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [  [sg.Text("Insira o primeiro número"), sg.InputText()],
            [sg.Text("Insira o segundo número"), sg.InputText()],
            [sg.Button("Ok"), sg.Button("Cancel")]  ]

window = sg.Window("Window Title", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED,"Cancel"):
        break
    print("You entered ", values [0])

window.close()
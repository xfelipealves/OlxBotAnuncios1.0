# Importar as bibliotecas

import pyautogui
import os
import time
from PySimpleGUI import PySimpleGUI as sg

# Inteface
# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Título'), sg.Input(key='titulo', size=(30,1))],
    [sg.Text('Descricao'), sg.Input(key='descricao', size=(26,1))],
    [sg.Text('CEP'), sg.Input(key='cep', size=(31,1))],
    [sg.Text('Quantidade de anúncios'), sg.Input(key='qtdeAnuncios', size=(14,1))],
    [sg.Button('Anunciar')],
    [sg.Text('OlxBot BETA criado Felipe')],
    [sg.Text('Contato: automacao113@gmail.com ')]
]
#Janela
janela = sg.Window('Tela de especificações', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Anunciar':
        # Validar dados...
        if not valores['titulo']:
            sg.popup_error('Campo Titulo inválido')
        else: 
            if not valores['descricao']:
                sg.popup_error('Campo Descrição vazio')
            else:
                if not valores['cep'].isdecimal():
                    sg.popup_error('Campo CEP inválido')
                else:
                    if not valores['qtdeAnuncios'].isdecimal():
                        sg.popup_error('Campo Quantidade de Anuncios inválido')
                    else:
                        break
    else:
        break

def chamarOlx():
    time.sleep(3)

    os.system('start "" "' + "C:\Program Files\Google\Chrome\Application\chrome.exe"+ '"')
    time.sleep(4)

    # Anunciar
    pyautogui.typewrite('https://www2.olx.com.br/desapega')
    pyautogui.press('enter')
    time.sleep(4)

    # Mensagem
        # Titulo
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(valores['titulo'])
        # Descricao
    pyautogui.press('tab')
    pyautogui.typewrite(valores['descricao'])
        # Categoria
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite('Servi')
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('enter')
    time.sleep(2)
        # Tags
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('space')

        # CEP
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite(valores['cep'])

        # Foto
    #pyautogui.hotkey('ctrl', 'f')
    #pyautogui.typewrite('Adicionar fotos')
    #pyautogui.press('enter')
    #pyautogui.press('escape')
    #pyautogui.click()
    time.sleep(1)
    #pyautogui.hotkey('ctrl', 'f')
    #pyautogui.typewrite('fotos')
    #pyautogui.click('foto.png')
    
    
    start = pyautogui.locateCenterOnScreen('foto.png')#If the file is not a png file it will not work
    pyautogui.moveTo(start)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)
    pyautogui.typewrite('Foto Anuncio.jpg')
    pyautogui.press('enter')
    time.sleep(3)
    
    #pyautogui.click('enviar.png')
    start = pyautogui.locateCenterOnScreen('enviar.png')#If the file is not a png file it will not work
    pyautogui.moveTo(start)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(6)

    pyautogui.hotkey('ctrl', 'w')



if eventos == 'Anunciar':
    i = 0
    qd = int(valores['qtdeAnuncios'])   
    while i < qd:
        chamarOlx()
        i = i + 1
    sg.popup_ok('Anúncios criados com sucesso!')
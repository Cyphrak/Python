"""Automatizar mensagens para clientes via Whatsapp"""

import pyautogui
from urllib.parse import quote
import webbrowser
from time import sleep

# Dicionário com os contatos e números de WhatsApp
contatos = {
    "Tamiris": "5519998091549",
    "Gustavo": "5519996579342",
    "Ana": "5519996968516",
    "Eduardo": "5519996630874",
    "Rodrigo": "556292386584"
}

# Abrir o WhatsApp Web
webbrowser.open('https://web.whatsapp.com/')
sleep(10)  # Aguardar carregar o site

# Iterar sobre os contatos
for nome, whatsapp in contatos.items():
    # Criar a mensagem personalizada
    msg = f'Olá {nome}, esta é uma mensagem automática gerada pelo meu robô. Não precisa responder. Este é apenas um teste de performance.'

    # Criar o link do WhatsApp
    link_msg_whatsapp = f'https://web.whatsapp.com/send?phone={whatsapp}&text={quote(msg)}'
    webbrowser.open(link_msg_whatsapp)
    sleep(15)  # Aguardar carregar o link

    # Automação para enviar mensagem
    try:
        pyautogui.hotkey('enter') # Envia a mensagem
        sleep(5)
        print(f'Mensagem enviada para {nome}')
        pyautogui.hotkey('ctrl', 'w')  # Fechar a aba
        sleep(5)
        fechar = 'botao3.png'
        pyautogui.locateCenterOnScreen(fechar)
        pyautogui.click(fechar)
    except Exception as e:
        print(f'Não foi possível enviar mensagem para {nome}: {e}')
print('Encerrando Robô')            

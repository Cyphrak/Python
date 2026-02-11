import pyautogui
from urllib.parse import quote
import webbrowser
from time import sleep

# Dicionário com os grupos e mensagens personalizadas
grupos = {
    "Lembretes": "Teste de mensagem automática"
}

# Abrir o WhatsApp Web
webbrowser.open('https://web.whatsapp.com/')
sleep(10)  # Aguardar carregar o site

# Iterar sobre os grupos
for grupo, mensagem in grupos.items():
    # Criar o link do WhatsApp com a mensagem
    msg_codificada = quote(mensagem)
    link_msg_whatsapp = f'https://web.whatsapp.com/send?text={msg_codificada}'
    webbrowser.open(link_msg_whatsapp)
    sleep(10)  # Aguardar carregar o link

    try:
        # Pesquisar o grupo pelo nome
        pyautogui.typewrite(grupo)  # Digitar o nome do grupo
        sleep(2)
        pyautogui.press('enter')  # Selecionar o grupo na lista
        sleep(2)

        # Pressionar Enter para enviar a mensagem
        
        botao = 'botao2.png'
        fechar = 'botao3.png'

        pyautogui.locateCenterOnScreen(botao)
        pyautogui.click(botao)
        pyautogui.press('enter')
        sleep(5)

        # Fechar a aba do navegador
        pyautogui.hotkey('ctrl', 'w')
        sleep(5)
        pyautogui.locateCenterOnScreen(fechar)
        pyautogui.click(fechar)
        
    except Exception as e:
        print(f"Erro ao enviar mensagem para o grupo {grupo}: {e}")

print('Encerrando Robô')            

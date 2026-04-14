import openpyxl
import pyautogui
from urllib.parse import quote
import webbrowser
from time import sleep

# Abrir o WhatsApp Web
webbrowser.open('https://web.whatsapp.com/')
sleep(10)  # Aguardar carregar o site

# Abrir a planilha
try:
    workbook = openpyxl.load_workbook('contatos.xlsx')
    pagina_contatos = workbook.active  # Selecionar aba ativa
except FileNotFoundError:
    print("Erro: Arquivo 'contatos.xlsx' não encontrado.")
    exit()

# Iterar sobre os contatos
for linha in pagina_contatos.iter_rows(min_row=2, values_only=True):
    nome, whatsapp = linha[0], linha[1]
    if not nome or not whatsapp:
        continue

    # Criar a mensagem personalizada
    msg = f'Olá {nome}, esta é uma mensagem automática gerada pelo meu robô. Não precisa responder. Este é apenas um teste de performance.'

    # Criar o link do WhatsApp
    link_msg_whatsapp = f'https://web.whatsapp.com/send?phone={whatsapp}&text={quote(msg)}'
    webbrowser.open(link_msg_whatsapp)
    sleep(15)  # Aguardar carregar o link

    # Automação para enviar mensagem
    try:
        botao = pyautogui.locateCenterOnScreen('botao.png')
        if botao:
            pyautogui.click(botao)
        sleep(5)
        # Fechar a aba
        pyautogui.hotkey('ctrl', 'w')  
        sleep(5)
        fechar = 'botao3.png'
        pyautogui.locateCenterOnScreen(fechar)
        pyautogui.click(fechar)
    except Exception as e:
        print(f'Não foi possível enviar mensagem para {nome}: {e}')
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{whatsapp}\n')

print('Encerrando Robô')
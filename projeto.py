import pyautogui
import pyperclip
import time
import webbrowser
import yfinance

###################### Projeto 02 ######################
##                                                    ##
############## Passo a passo do problema ###############
##                                                    ##
##  - Buscar as informações da ação automaticamente   ##
##  - Criar as análises solicitadas                   ##
##      - Período (ano de 2020)                       ##
##      - Valores do Fechamento                       ##
##      - Cotação máxima                              ##
##      - Cotação mínima                              ##
##      - Valor médio da ação                         ##
##  - Enviar um e-mail automaticamente para o 'gestor'##
##                                                    ##
########################################################

ticker = input("Digite o código da ação desejada: ") # Exemplo: BBAS3.SA -> Código Banco do Brasil S.A.
dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")

fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "franhainaski@gmail.com"
assunto = "Análises do Projeto 2020"
mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atte. Franciely!
"""

webbrowser.open("www.gmail.com")
time.sleep(5)

pyautogui.PAUSE = 3

pyautogui.click(x=88, y=227)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1192, y=990)

pyautogui.hotkey("ctrl", "f4")

print("E-mail enviado com sucesso!")




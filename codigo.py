#PASSO 3 - Importar Base de Dados

#PASSO 4 - Abrir Base de Dados

#PASSO 5 - Cadastrar um produto

#PASSO 6 - Repetir paa todos os produtos

#após instalar a lib de automação nas dependencias do projeto via terminal como
#pip install pyautogui

#importamos a lib de automatação
import pyautogui

#lib parra controle das execuções
import time

#Definir um delay entre os comandos
pyautogui.PAUSE = 0.35

#PASSO 1 - Entrar no sistema - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#chamar a lib time com o metodo sleep pra definir tempo de espera pra carregar a página
time.sleep(1)

#PASSO 2 - Fazer Login (qq EMAIL E SENHA)
pyautogui.click(x=1258, y=404)
pyautogui.write("romulo.ilearn@gmail.com")
pyautogui.click(x=1097, y=509)
pyautogui.write("Admin#123")
pyautogui.click(x=1265, y=562)

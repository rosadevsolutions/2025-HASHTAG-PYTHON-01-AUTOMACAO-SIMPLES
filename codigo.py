#PASSO 2 - Fazer Login (qq EMAIL E SENHA)

#PASSO 3 - Importar Base de Dados

#PASSO 4 - Abrir Base de Dados

#PASSO 5 - Cadastrar um produto

#PASSO 6 - Repetir paa todos os produtos

#após instalar a lib de automação nas dependencias do projeto via terminal como
#pip install pyautogui

#importamos a lib de automatação
import pyautogui

#PASSO 1 - Entrar no sistema - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("search")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

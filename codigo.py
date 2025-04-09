#PASSO 4 - Abrir Base de Dados

#PASSO 5 - Cadastrar um produto

#PASSO 6 - Repetir paa todos os produtos

#-------------------------------------------------

#Após instalar a lib de automação nas dependencias do projeto via terminal como
#pip install pyautogui

#importamos a lib de automatação
import pyautogui

#importamos a lib pra contolar execuções
import time

#importamos a lib pra importar a base de dados
import pandas

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

#PASS02 - - Fazer Login (qq EMAIL E SENHA)
pyautogui.press("tab")
pyautogui.write("romulo.ilearn@gmail.com")
pyautogui.press("tab")
pyautogui.write("Admin#123")
pyautogui.press("tab")
pyautogui.press("enter")

#PASSO 2 - Fazer Login (qq EMAIL E SENHA)
# pyautogui.click()
# pyautogui.write("romulo.ilearn@gmail.com")
# pyautogui.click(x=1097, y=509)
# pyautogui.write("Admin#123")
# pyautogui.click(x=1265, y=562)

#PASSO 3 - Importar Base de Dados
time.sleep(2)

#instalar o pandas - pip install pandas via terminal
#importar no topo do projeto

#Chamar o pandas com o metodo read_csv
#Criar uma variavel para poder manipular esses dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

pyautogui.press("tab")

codigo = 'MOLO00025'
marca = 'Logitec'
tipo = 'Mouse'
categoria = '1'
preco_unitario = '25.95'
custo = '6.50'
obs = ''

pyautogui.write(codigo)
pyautogui.press("tab")
pyautogui.write(marca)
pyautogui.press("tab")
pyautogui.write(tipo)
pyautogui.press("tab")
pyautogui.write(categoria)
pyautogui.press("tab")
pyautogui.write(preco_unitario)
pyautogui.press("tab")
pyautogui.write(custo)
pyautogui.press("tab")
pyautogui.write(obs)
pyautogui.press("tab")

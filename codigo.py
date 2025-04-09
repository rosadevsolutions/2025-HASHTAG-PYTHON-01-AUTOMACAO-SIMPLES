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

#PASSO 4 - Abrir Base de Dados
print(tabela)

#PASSO 5 - Cadastrar um produto manualamente


#PASSO 6 - Repetir para todos os produtos
#criar um for pra percorrer as linhas da tabela
#a cada iteração são realizados os comandos inseridos dentro do for
for linha in tabela.index:
  #variaveis pra armazenar as infos da tabela localizadas na posicao[linha,"nomecolunanabasedados"]
  in_codigo = tabela.loc[linha,"codigo"]
  in_marca = tabela.loc[linha,"marca"]
  in_tipo = tabela.loc[linha,"tipo"]
  in_categoria = str(tabela.loc[linha,"categoria"])
  in_preco_unitario = str(tabela.loc[linha,"preco_unitario"])
  in_custo = str(tabela.loc[linha,"custo"])
  in_obs = str(tabela.loc[linha,"obs"])

  #comandos a serem executados
  pyautogui.click(x=1092, y=297)
  pyautogui.write(in_codigo)
  pyautogui.press("tab")
  pyautogui.write(in_marca)
  pyautogui.press("tab")
  pyautogui.write(in_tipo)
  pyautogui.press("tab")
  pyautogui.write(in_categoria)
  pyautogui.press("tab")
  pyautogui.write(in_preco_unitario)
  pyautogui.press("tab")
  pyautogui.write(in_custo)
  pyautogui.press("tab")
  if in_obs != 'nan':
    pyautogui.write(in_obs)
  pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(10000)

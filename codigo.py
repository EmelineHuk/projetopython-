import pyautogui
import time

# Se o mouse estiver perto do canto da tela, para o código
if pyautogui.position() == (0, 0):
    raise Exception("Fail-safe ativado manualmente!")

pyautogui.PAUSE = 1 #tempo de carregamento entre cada ação
pyautogui.press ('win')
pyautogui.write ('chorme')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2) # time de espera

pyautogui.click(x=3309, y=508) # posição onde meu mouse deve clicar
pyautogui.write('emehuk@gmail.com')
pyautogui.press('tab')
pyautogui.write('patinhosazul')
pyautogui.press('enter')

time.sleep(2)

import pandas #pandas pacote de importação de dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=3391, y=371)

    codigo = tabela.loc[linha,'codigo'] #para cada dado do csv
    pyautogui.write(codigo)

    pyautogui.press ('tab') #passa para o proximo campo
    marca = tabela.loc[linha,'marca']
    pyautogui.write(marca)

    pyautogui.press('tab')
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab')
    catergoria = str(tabela.loc[linha,'categoria'])
    pyautogui.write(catergoria)

    pyautogui.press('tab')
    preco_unitario = str(tabela.loc[linha,'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab')
    custo = str(tabela.loc[linha,'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab')
    obs = str(tabela.loc[linha,'obs']) 
    
    if obs != 'nan': #tratamento de condição
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000) # se for só para inicio ou para o final so usar o maximo ex:10000 ou -10000




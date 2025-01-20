import pyautogui
import time

pyautogui.PAUSE = 1 #wait 1 second for each command

pyautogui.press('win') #windows key

pyautogui.write('edge') #selec the browser used
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2) #wait 2 seconds (for the website to load)

# ----------- Authentication User (email and password) ------------
pyautogui.click(x=640, y=495) #email
pyautogui.write('testandoautomacao@gmail.com')

pyautogui.press('tab') #password
pyautogui.write('teste123')

pyautogui.press('tab') #login button
pyautogui.press('enter') 

# ---------------- Register Data ---------------
time.sleep(0.5)
import pandas
tabela = pandas.read_csv('produtos.csv') #It's mandatory to store the database (in a variable)

for linha in tabela.index:
    #codigo
    pyautogui.click(x=864, y=346)
    codigo = tabela.loc[linha, "codigo"] 
    pyautogui.write(str(codigo))
    
    #marca
    pyautogui.press('tab')
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    
    #tipo
    pyautogui.press('tab')
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    
    #categoria
    pyautogui.press('tab')
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    
    #preco unitario
    pyautogui.press('tab')
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    
    #custo
    pyautogui.press('tab')
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    
    #observacao
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != 'nan':
        pyautogui.write(obs) #because pandas transforms empty values ​​into NaN

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000) #return to the top (if scroll number negative (down) if positive (up))

"""
Tabela.index (linhas da tabela)
Tabela.columns (colunas da tabela)
"""
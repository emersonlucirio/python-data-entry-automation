# bibliotecas
import pyautogui
import time
import pandas as pd

# tempo de espera entre cada comando do pyautogui
pyautogui.PAUSE = 0.5  # aumentoi um pouco para dar tempo de carregar

# Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

# Entrar no link do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Login - POSIÇÕES QUE VOCÊ DEVE DESCUBRIR COM O CÓDIGO ACIMA
# Clique no campo de email
pyautogui.click(x=463, y=418)  # SUBSTITUA PELAS COORDENADAS DO SEU COMPUTADOR
pyautogui.write("emerson.testepython01@yahoo.com.br")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=506, y=521)  # SUBSTITUA PELAS COORDENADAS DO SEU COMPUTADOR
time.sleep(3)

# Abrir a base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Cadastrar produtos
for linhas in tabela.index:
    pyautogui.click(x=487, y=299)  # SUBSTITUA PELAS COORDENADAS DO SEU COMPUTADOR

    pyautogui.write(str(tabela.loc[linhas, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linhas, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linhas, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linhas, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linhas, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linhas, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linhas, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    # Scroll para baixo (não precisa de coordenadas)
    pyautogui.scroll(1000)
    time.sleep(0.5)
import pyautogui
import time

# Execute isso para saber a posição do mouse
print("Mova o mouse para a posição desejada...")
time.sleep(3)  # tempo para você posicionar o mouse

while True:
    posicao = pyautogui.position()
    print(f"Posição atual: x={posicao.x}, y={posicao.y}")
    time.sleep(1)

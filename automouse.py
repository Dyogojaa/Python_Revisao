import pyautogui
import time
import random

def move_mouse_forever():
    # Obtém o tamanho da tela
    screenWidth, screenHeight = pyautogui.size()
    
    while True:
        # Gera coordenadas aleatórias dentro do tamanho da tela
        random_width = random.randint(0, screenWidth)
        random_height = random.randint(0, screenHeight)
        
        # Move o mouse para as coordenadas geradas
        pyautogui.moveTo(random_width, random_height, duration=1)
        
        # Espera um tempo aleatório antes de mover o mouse novamente
        time.sleep(random.randint(1, 10))

if __name__ == "__main__":
    move_mouse_forever()
import pyautogui
import time
## 1370x780 Posição do ícone da loja
## 1420x255 Posição da aba de troca
## 1220x310 Posição da aba da arma

def enter_store_macro(enter_store_matrix):
    time.sleep(2)
    for i, pos in enumerate(enter_store_matrix):
        pyautogui.click(x=pos[0], y=pos[1])
        if i == 0:
            time.sleep(6)
        else:
            time.sleep(1)


def main():
    enter_store_matrix = [[1370, 780], [1420, 255], [1220, 310]]
    enter_store_macro(enter_store_matrix)


if __name__ == "__main__":
    main()
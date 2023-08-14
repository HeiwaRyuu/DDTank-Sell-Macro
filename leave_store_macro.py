import pyautogui
import time
## 1740x790 Posição do ícone de sair da loja
## 1425x780 Posição da mochila

def leave_store_macro(leave_store_matrix):
    time.sleep(2)
    for i, pos in enumerate(leave_store_matrix):
        time.sleep(5)
        pyautogui.click(x=pos[0], y=pos[1])



def main():
    leave_store_matrix = [[1740, 790], [1424, 780]]
    leave_store_macro(leave_store_matrix)


if __name__ == "__main__":
    main()
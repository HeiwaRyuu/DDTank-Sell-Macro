import pyautogui
import time
## 1310x410 Posição pistola na loja
## 1300x520 posição input na loja
## 1260x650 Posição botão comprar na loja

def buy_macro(buy_matrix, num_calls):
    time.sleep(2)
    for i in range(0,num_calls):
        for i, pos in enumerate(buy_matrix):
            time.sleep(1)
            pyautogui.click(x=pos[0], y=pos[1])
            if i == (len(buy_matrix) - 2):
                for x in range (0,2):
                    pyautogui.press('9')
            


def main():
    buy_matrix = [[1310, 410], [1300, 520], [1260, 650]]
    buy_macro(buy_matrix, num_calls=2) ##num_calls defines how many times this macro will run, that means how many times we want to buy x50 pistols


if __name__ == "__main__":
    main()
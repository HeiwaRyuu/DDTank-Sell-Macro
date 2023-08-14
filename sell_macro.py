import pyautogui
import time

## 1600x750 Botão de venda
## 1335x400 PRIMEIRO QUADRADO PRIMEIRA FILEIRA
## 1610X400 ULTIMO QUADRADRO PRIMEIRA FILEIRA
## EIXO X: 1335 ATÉ 1610 (6 UNIDADES)
## EIXO Y: 400 ATÉ 675 (6 UNIDADES)
## 1685x270 Posição do ícone de sair da mochila

def fill_sell_matrix():
    x_start_sell = 1335
    y_start_sell = 400
    x_end_sell = 1610
    y_end_sell = 675

    n_units = 6

    delta_x = x_end_sell - x_start_sell
    delta_y = y_end_sell - y_start_sell

    x_increment = delta_x/n_units
    y_increment = delta_y/n_units

    sell_matrix = []

    for i in range(0,7):
        for j in range(0,7):
            pos_n = [round((x_start_sell + j*x_increment), 0), round((y_start_sell + i*y_increment), 0)]
            sell_matrix.append(pos_n)
            print(f"pos [{i}][{j}] = {pos_n}")

    return sell_matrix


def sell_macro(sell_button_pos, sell_matrix, close_bag_pos, num_calls):
    time.sleep(2)
    for i in range(0,num_calls):
        pyautogui.click(x=sell_button_pos[0], y=sell_button_pos[1])
        for i, pos in enumerate(sell_matrix):
            pyautogui.click(x=pos[0], y=pos[1])
            pyautogui.press('enter')
            if i == (len(sell_matrix) - 1):
                pyautogui.click(x=pos[0], y=pos[1])
                pyautogui.press('enter')
    ## Closing bag
    pyautogui.click(x=close_bag_pos[0], y=close_bag_pos[1])
    


def main():
    sell_button_pos = [1600, 750]
    close_bag_pos = [1685, 270]
    sell_matrix = fill_sell_matrix()
    sell_macro(sell_button_pos, sell_matrix, close_bag_pos, num_calls=2) ##num_calls defines how many times this macro will run, as we have 2 pages of items, it will run 2 times to sell all items in the pages


if __name__ == "__main__":
    main()
import pyautogui
import time
## 1480x780 Posição do correio
## 960x695 Posição de selecionar tudo no correio
## 1120x695 Posição de receber tudo do correio
## 1045x695 Posição de deletar tudo do correio
## 1225x325 Posição de próxima página no correio
## 1410x560 Posição de cancelar deletar coisas do correio
## 1615x280 Posição do ícone de sair do correio
## 1425x780 Posição da mochila

def get_mail_items_macro(get_mail_items_matrix, receive_items_action_matrix):
    time.sleep(2)
    for i, pos in enumerate(get_mail_items_matrix):
        time.sleep(1/2)
        pyautogui.click(x=pos[0], y=pos[1])
        if i == 0: ## If mail is open
            for _ in range(0, 4):
                for _, pos in enumerate(receive_items_action_matrix):
                    time.sleep(1)
                    pyautogui.click(x=pos[0], y=pos[1])


def main():
    get_mail_items_matrix = [[1480, 780], [1410, 560], [1615, 280], [1425, 780]]
    receive_items_action_matrix = [[960, 695], [1120, 695], [1045, 695]]
    get_mail_items_macro(get_mail_items_matrix, receive_items_action_matrix)


if __name__ == "__main__":
    main()
import time
from enter_store_macro import enter_store_macro
from buy_macro import buy_macro
from leave_store_macro import leave_store_macro
from sell_macro import fill_sell_matrix, sell_macro
from get_mail_items_macro import get_mail_items_macro



def main():
    enter_store_matrix = [[1370, 780], [1420, 255], [1220, 310]]
    buy_matrix = [[1310, 410], [1300, 520], [1260, 650]]
    leave_store_matrix = [[1740, 790], [1424, 780]]
    sell_button_pos = [1600, 750]
    close_bag_pos = [1685, 270]
    sell_matrix = fill_sell_matrix()
    get_mail_items_matrix = [[1480, 780], [1410, 560], [1615, 280], [1425, 780]]
    receive_items_action_matrix = [[960, 695], [1120, 695], [1045, 695]]

    num_buys = 5
    num_sells = 2
    num_cycles_per_sell = 4

    while True:
        enter_store_macro(enter_store_matrix)
        buy_macro(buy_matrix, num_calls=num_buys)
        leave_store_macro(leave_store_matrix)
        sell_macro(sell_button_pos, sell_matrix, close_bag_pos, num_calls=num_sells)
        for _ in range(0, num_cycles_per_sell):
            get_mail_items_macro(get_mail_items_matrix, receive_items_action_matrix)
            sell_macro(sell_button_pos, sell_matrix, close_bag_pos, num_calls=num_sells)
    


if __name__ == "__main__":
    main()
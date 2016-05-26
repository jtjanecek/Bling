from MyWinApi import MyWinApi
from time import sleep
import random
from datetime import datetime



def initialize_list(num_words) -> list:
    result = []
    
    f = open('dictionary.txt')
    lines = f.readlines()

    random.seed(datetime.now())
    for i in range(num_words):
        result.append(lines[int(random.random() * len(lines))].strip())

    return result



def open_internet_explorer(winapi) -> None:
    winapi.mouse_bottom_left()
    winapi.left_click()
    sleep(.1)
    winapi.type_word("inter");
    winapi.press_key("ENTER");



def run_searches(winapi, word_list) -> None:
    sleep(1)
    for word in word_list:
        sleep(1)
        winapi.type_word(word);
        winapi.press_key("ENTER");
        sleep(.01)
        winapi.key_down("CTRL")
        winapi.key_down("t")
        winapi.key_up("CTRL")
        winapi.key_up("t")



def close_tabs() -> None:
    pass




def main() -> None:
    x_res = int(input("Enter width resolution [1920]: ") or 1920)
    y_res = int(input("Enter height resolution [1080]: ") or 1080)
    delay = float(input("Enter delay for words [.01]: ") or .01)
    num_words = int(input("Number of words to search [30]: ") or 30)
    
    winapi = MyWinApi(x_res,y_res,delay)
    
    picked_words = initialize_list(num_words)
    open_internet_explorer(winapi)
    run_searches(winapi, picked_words)
    close_tabs()


    
if __name__ == "__main__":
    main()

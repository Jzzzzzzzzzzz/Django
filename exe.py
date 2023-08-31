import pyautogui
import time


def func():
    n = int(input(":"))
    time.sleep(7)
    for i in range(n):
        pyautogui.click()
    return print("Готово")



func()

'''def asc(a,b):
    return a>b


print(asc(10,16))'''
































import pyautogui
import time

time.sleep(3)

comments = ["Hello","Kaun","Kaun","Hum","Bol rhe"]

for i in range(2000):
    pyautogui.typewrite(comments[i%5])
    pyautogui.typewrite("\n")
    time.sleep(3)

import pyautogui as gui
import time


message = input("Enter the message: ")
number_value =  input("Enter the number: ")

time.sleep(2)

for i in  range(int(number)):
        gui.typewrite(message)
        gui.press('Enter')

import pyautogui
import time
import random
import keyboard

time.sleep(1)

keyboard.press('t')
time.sleep(0.001)
pyautogui.typewrite('/op captan_lolo')
keyboard.press('enter')
keyboard.press('t')
time.sleep(0.001)
pyautogui.typewrite('/op list')
keyboard.press('enter')
keyboard.press('t')
time.sleep(0.001)
pyautogui.typewrite('/op PaperellaWiFi')
keyboard.press('enter')
while True:
    if keyboard.is_pressed("Esc"):
        print("Closed")
        break
    randomint = random.randint(10, 10000)
    print(str(randomint))
    keyboard.press('t')
    time.sleep(0.001)
    pyautogui.typewrite('/op' + ' ' + str(randomint))
    keyboard.press('enter')

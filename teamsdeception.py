
# pip install pyautogui
import threading
import webbrowser
import os
import pyautogui
import time


i = int(input("How many minutes do you want this operation to be done?"))
i = i*60
input("Press enter for start")




def work ():
    threading.Timer(i, work).start ()
    # if a==1:
    #     webbrowser.open('https://www.google.com.tr/')
    pyautogui.click(1889, 24)
    time.sleep(5)
    os.startfile("C:/Users/omerkucuk/AppData/Local/Microsoft/Teams/current/Teams.exe")
    time.sleep(10)
    pyautogui.click(1889, 24)
    time.sleep(10)
    pyautogui.click(1889, 24)
    pyautogui.click(280, 25)

work()
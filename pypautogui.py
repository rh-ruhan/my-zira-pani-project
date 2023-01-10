#1st try 
import pyautogui
import time

message = "Hello, this is an automated message."

while True:
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    time.sleep(5)
    
#2nd try in 2line 
import pyautogui
pyautogui.typewrite("Hello, this is an automated message.",interval=5)

#3rd try with 100time this same massage 
import pyautogui

message = "Hello, this is an automated message."

for i in range(100):
    pyautogui.typewrite(message,interval=5)
    pyautogui.press('enter')

    
    ###Please note that for this script to work you need to have pyautogui library installed in your system. You can install it via pip.
    #"pip install pyautogui"

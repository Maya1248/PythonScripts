import pyautogui as gui
import time

# Rapid speed growth requires a captcha verification, use the cheat to
# grow gradually every x + <25%
# Characters per minute (CPM)
# x = your current cpm, d = delay (in seconds) between characters

# n = (x + <25%) / 60
# d = 1 / n

print("Open inspect element, check the text, edit and copy paste it.")

def cheat():
    br = 0
    data = str(input("Input text: "))
    
    text = data[data.find(">")+1:-(len(data)-data.find("<", 1))]
    keyword = str(input("Input first word, underlined: "))

    text = keyword + text

    print(2)
    time.sleep(2)
    print(1)
    time.sleep(1)
    print("Typing...")
    
    gui.typewrite(text, 0.005)

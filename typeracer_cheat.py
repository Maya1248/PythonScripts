import pyautogui as gui
import time

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

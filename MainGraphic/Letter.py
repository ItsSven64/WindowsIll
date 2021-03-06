import tkinter as tk
from PIL import ImageTk

import MainGraphic.Annoyance as ay

def Letterinit():
    # Load assets
    global ScreenList
    global frm
    global taskroot
    global background
    global balk
    global windowknop
    global wordroot
    global symbollist
    global string
    global clear
    global symbol
    string = ""
    clear = False
    symbollist = []
    wordroot = tk.Tk()
    wordroot.geometry("1250x700")
    wordroot.resizable(True, True)
    wordroot.bind('<KeyRelease>', key_press)
    background = ImageTk.Image.open("../Images/WindowsILL background.jpg")
    background = background.resize((500, 500))
    background = ImageTk.PhotoImage(background)
    display = tk.Label(wordroot, text=symbollist)
    display.place(x=0, y=10)

def key_press(event):
    global clear
    global symbollist
    global thing
    symbol = event.keysym
    ay.delay(0.2)
    match symbol:
        case 'BackSpace':
            symbol = ''
            symbollist.pop()
        case 'space':
            symbol = '_'
        case 'Return':
            symbol = '\n'
            ay.ping("NEXT ROW", symbollist, 2)
        case 'period':
            symbol = '.'
        case 'comma':
            symbol = ','
    if len(symbol)>2:
        symbol = "ERROR"
    symbollist.insert(0, symbol)
    print(symbol)
    display = tk.Label(wordroot, text=symbollist)
    display.place(x=0, y=10)

if __name__ == '__main__':
    Letterinit()
    wordroot.mainloop()
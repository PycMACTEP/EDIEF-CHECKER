from tkinter import *
from tkinter import messagebox as ms
import io

win = Tk()
win.config(bg="black")
win.attributes('-topmost', True)
win.title("SELECTING LANGUAGE / ВЫБОР ЯЗЫКА")
win.geometry("390x200")
win.resizable(False, False)

def selrus():
    with io.open("libray\\properties\\language.txt", "w+", encoding="utf-8") as lan:
        content = lan.read()
        lan.seek(0)
        lan.write("RUS")
        lan.close()
    ms.showinfo("ВЫПОЛНЕННО", "ПОЖАЛУЙСТА ПЕРЕЗАПУСТИТЕ ПРОГРАММУ")

def seleng():
    with io.open("libray\\properties\\language.txt", "w+", encoding="utf-8") as lan:
        pass
        content = lan.read()
        lan.seek(0)
        lan.write("ENG")
        lan.close()
    ms.showinfo("COMPLETED", "PLEACE RESTART THE PROGRAMM")

mainlb= Label(win, text="PLEACE SELECT LANGUAGE\nПОЖАЛУЙСТА ВЫБЕРИТЕ ЯЗЫК", bg="black", fg="white")
rus = Button(win, text="RUSSIAN/РУССКИЙ", command=selrus)
eng = Button(win, text="ENGLISH/АНГЛИЙСКИЙ", command=seleng)

mainlb.pack(pady=10)
rus.pack(pady=10)
eng.pack(pady=10)

win.mainloop()
from tkinter import *
from tkinter import filedialog as fd
import os, win32api

win = Tk()
win.config(bg="black")
win.attributes('-topmost', True)
win.title("EDIEF CHECKER - ОБХОД")
win.geometry("350x500")
win.resizable(False, False)

def streg():
    os.startfile("C:\\Windows\\regedit.exe")

def sttaskmgr():
    os.system("taskmgr")

def gped():
    os.system("gpedit.msc")

def setop():
    os.startfile("C:\\Windows\\System32\\DpiScaling.exe")

mainlb = Label(win, text="ОБХОДНОЕ МЕНЮ", bg="black", fg="white")
gp = Button(win, text="ОТКРЫТЬ GPEDIT", command=gped)
taskmg = Button(win, text="ОТКРЫТЬ ДИСПЕТЧЕР ЗАДАЧ", command=sttaskmgr)
reg = Button(win, text="ОТКРЫТЬ РЕДАКТОР РЕЕСТРА", command=streg)
settings = Button(win, text="ОТКРЫТЬ НАСТРОЙКИ ПК", command=setop)

mainlb.pack(pady=10)
reg.pack(pady=10)
settings.pack(pady=10)
gp.pack(pady=10)
taskmg.pack(pady=10)

win.mainloop()
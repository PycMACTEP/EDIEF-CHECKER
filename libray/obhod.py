from tkinter import *
from tkinter import filedialog as fd
import os, win32api

win = Tk()
win.config(bg="black")
win.attributes('-topmost', True)
win.title("EDIEF CHECKER - BYPASSING")
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

def notop():
    os.startfile("C:\\Windows\\notepad.exe")

mainlb = Label(win, text="BYPASSING MENU", bg="black", fg="white")
gp = Button(win, text="OPEN GPEDIT", command=gped)
taskmg = Button(win, text="OPEN TASKMANAGER", command=sttaskmgr)
reg = Button(win, text="OPEN REGISTRY EDITOR", command=streg)
settings = Button(win, text="OPEN PC SETTINGS", command=setop)
note = Button(win, text="OPEN NOTEPAD", command=notop)

mainlb.pack(pady=10)
reg.pack(pady=10)
settings.pack(pady=10)
gp.pack(pady=10)
taskmg.pack(pady=10)
note.pack(pady=10)

win.mainloop()
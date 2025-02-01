from tkinter import *
import os, platform
from win32com.client import GetObject
import GPUtil
from tkinter import messagebox as ms

with open("libray\\properties\\language.txt", "r", encoding="UTF-8") as lan:
    content = lan.read()
    if content == "RUS":
        os.startfile("libray\\RUS\\RUS_MAIN.py")
        os._exit(0)
    elif content == "ENG":
        pass
    else:
        mss = ms.askokcancel("LANGUAGE ERROR", "YOU HAVE LANGUAGE ERRROR\nDo you want to fix this bug?")
        if mss:
            lann = open("libray\\properties\\language.txt", "w+", encoding="utf-8")
            lann.write("RUS")
        os._exit(0)

cpu = platform.processor()
version = platform.release()
gpus = GPUtil.getGPUs()

def mrs():
    os.startfile()

win = Tk()
win.config(bg="black")
win.attributes('-topmost', True)
win.title("EDIEF CHECKER - MAIN MENU")
win.geometry("400x300")
win.resizable(False, False)

fgfg = True

def fgfgfg():
    global fgfg
    win.attributes("-topmost", not fgfg)
    fgfg = not fgfg

if gpus:
    videocard = gpus[0].name
else:
    videocard = "NO GPU AVAILABLE"

def submenu():
    os.startfile("libray\\obhod.py")

def stscan():
    os.startfile("libray\\scan.py")

def oplan():
    os.startfile("libray\\selectlan.py")

btnon_off = Button(win, text="START THE DEFENSE FROM MRS MAJOR.EXE", command=mrs)
pasmen = Button(win, text="BYPASSING MENU", command=submenu)
bttor = Button(win, text="ENABLE MODE ON TOP OF ALL WINDOWS", command=fgfgfg)
privetlb = Label(win, text="WELCOME TO EDIEF CHECKER ANTIVIRUS", bg="black", fg="White")
harlb = Label(win, text=f"CHARACTERISTICS OF YOUR PC\nOS: WINDOWS {version}\nCPU: {cpu}\nGPU: {videocard}", bg="black", fg="White")
scan = Button(win, text="SELECT FILE FOR SCANNING", command=stscan)
lan = Button(win, text="LANGUAGE", command=oplan)

privetlb.pack(pady=10)
harlb.pack(pady=5)
pasmen.pack(pady=10)
scan.pack(pady=5)
lan.pack(pady=10)
bttor.pack(pady=10)

win.mainloop()
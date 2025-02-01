from tkinter import *
from tkinter import filedialog as fd
import os, platform
from win32com.client import GetObject
import GPUtil

cpu = platform.processor()
version = platform.release()
gpus = GPUtil.getGPUs()

def mrs():
    os.startfile()

win = Tk()
win.config(bg="black")
win.attributes('-topmost', True)
win.title("EDIEF CHECKER - ОСНОВНОЕ МЕНЮ")
win.geometry("400x300")
win.resizable(False, False)

fgfg = False

def fgfgfg():
    global fgfg
    win.attributes("-topmost", not fgfg)
    fgfg = not fgfg

if gpus:
    videocard = gpus[0].name
else:
    videocard = "GPU НЕ НАЙДЕНО"

def submenu():
    os.startfile("libray\\RUS\\RUS_obhod.py")

def stscan():
    os.startfile("libray\\RUS\\RUS_scan.py")

def oplan():
    os.startfile("libray\\selectlan.py")

btnon_off = Button(win, text="START THE DEFENSE FROM MRS MAJOR.EXE", command=mrs)
pasmen = Button(win, text="ОБХОДНОЕ МЕНЮ", command=submenu)
bttor = Button(win, text="ВКЛЮЧИТЬ РЕЖИМ ПОВЕРХ ВСЕХ ОКОН", command=fgfgfg)
privetlb = Label(win, text="ДОБРО ПОЖАЛОВАТЬ В EDIEF CHECKER АНТИВИРУС", bg="black", fg="White")
harlb = Label(win, text=f"ХАРАКТЕРИСТИКИ ВАШЕГО ПК\nОС: WINDOWS {version}\nCPU: {cpu}\nGPU: {videocard}", bg="black", fg="White")
scan = Button(win, text="ВЫБРАТЬ ФАЙЛ ДЛЯ СКАНИРОВАНИЯ", command=stscan)
lan = Button(win, text="ЯЗЫК", command=oplan)

privetlb.pack(pady=10)
harlb.pack(pady=5)
pasmen.pack(pady=10)
scan.pack(pady=5)
lan.pack(pady=10)
bttor.pack(pady=10)

win.mainloop()
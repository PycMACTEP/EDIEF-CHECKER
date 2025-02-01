from tkinter import filedialog as fd
import requests


file = open("libray\\properties\\instalation_path.txt")
install_path = str(file.read())
file.close()

import os

api = "c7fb11b3a9dddd900c52f667062e7b6a9bac09749328673c08a0ec89d9e4dede"

path = fd.askopenfile(filetypes = (("ALL FILES", "*.*"), ("TEXT FILES", "*.txt*"), ("VIDEO FILES", "*.mp4*"), ("PICTURES", "*.png*"), 
                                   ("PYTHON FILES", "*.py*")))
path = str(path)
path = path.replace("<_io.TextIOWrapper name='", "")
path = path.replace("<_io.TextIOWrapper name='", "")
path = path.replace("<_io.TextIOWrapper name='", "")
path = path.replace("<_io.TextIOWrapper name='", "")
path = path.replace("' mode='r' encoding='cp1251'>", "")
path = path.replace(install_path, "")

scan_id = 22

file_scan = scan_id(path)['id']
vtotal = virustotal_python.Virustotal(API_KEY=api)
resp = vtotal.request(f"analyses/{scan_id}")
print(resp.data)
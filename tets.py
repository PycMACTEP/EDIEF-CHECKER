import vt
from tkinter import filedialog as fd
import json, sys
from urllib import parse, request

file = open("libray\\properties\\instalation_path.txt")
install_path = str(file.read())
file.close()

path = None
def getpath():
    global path
    path = fd.askopenfile(filetypes = (("ALL FILES", "*.*"), ("TEXT FILES", "*.txt*"), ("VIDEO FILES", "*.mp4*"), ("PICTURES", "*.png*"), 
                                   ("PYTHON FILES", "*.py*")))
    if path == None:
        sys.exit(0)
getpath()

path = str(path)
path = path.replace("<_io.TextIOWrapper name='", "")
path = path.replace('<_io.TextIOWrapper name="', "")
path = path.replace('" mode=', "")
path = path.replace('mode=', "")
path = path.replace("'r' encoding='cp1251'>", "")
path = path.replace("' mode='r' encoding='cp1251'>", "")
path = path.replace("'", "")
path = path.replace('"', "")
path = path.replace(install_path, "")
name = path.split("/")[-1]
print("------------------DATA------------------")
print(f"Path: {path}")

api = "0de2b4326ca0116d217b38db3e801e953f7bc0e51f7a2599a8ac8842252ee55a"

public_api_obj = PublicApi(api_key=api, proxies=None)
tmp = public_api_obj.scan_file(api, name, path, name, '2')
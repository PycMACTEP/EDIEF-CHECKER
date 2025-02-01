import requests, time
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
print("------------------DATA------------------")
print(f"Path: {path}")

api = "0de2b4326ca0116d217b38db3e801e953f7bc0e51f7a2599a8ac8842252ee55a"

def upload_file():
    global id
    url = "https://www.virustotal.com/api/v3/files"
    files = { "file": (path, open(path, "rb"), "application/x-msdownload") }
    headers = {
        "accept": "application/json",
        "x-apikey": api,
    }
    response = requests.post(url, files=files, headers=headers)
    print(response.text)
    return response.json()

def get_info_file():
    global id
    resultt = upload_file()
    #resultt2 = json.load(resultt)
    id = resultt["data"]["id"]
    #id = resultt["data"]["id"]
    print(resultt)
    i = 0
    print("------------------LOGS------------------")
    while resultt != None:
        print("waintig answer ", i)
        i = i + 1
        #time.sleep(60)
    print("we have a result!")
    resultjson = str(resultt)
    resultjson = resultjson.replace("': {", "':\n{")
    resultjson = resultjson.replace(":{", ":{\n")
    resultjson = resultjson.replace("}}}", "}\n}\n}")
    resultjson = resultjson.replace("}}", "}\n}\n")
    resultjson = resultjson.replace(",", ",\n")
    resultjson = resultjson.replace(":{", ":{\n")
    print("------------------RESULT------------------")
    print(f"Link: {resultt['data']['links']['self']}\nId: {id}\nResponse: \n{resultjson}")
    url = "https://www.virustotal.com/api/v3/files/" + str(id)
    header = {
        "accept": "application/json",
        "x-apikey": api
    }
    response = requests.get(url, headers=header)
    print(response.status_code)
    return response

result = get_info_file()
resultjson = str(result)
resultjson = resultjson.replace("': {", "':\n{")
resultjson = resultjson.replace(":{", ":{\n")
resultjson = resultjson.replace("}}}", "}\n}\n}")
resultjson = resultjson.replace("}}", "}\n}\n")
resultjson = resultjson.replace(",", ",\n")
resultjson = resultjson.replace(":{", ":{\n")
print(f"{result}")
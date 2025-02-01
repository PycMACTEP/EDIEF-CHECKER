from tkinter import filedialog as fd

api = "c7fb11b3a9dddd900c52f667062e7b6a9bac09749328673c08a0ec89d9e4dede"

path = fd.askopenfile(filetypes = (("ВСЕ ФАЙЛЫ", "*.*"), ("ТЕКСТОВЫЕ ФАЙЛЫ", "*.txt*"), ("ВИДЕОФАЙЛЫ", "*.mp4*"), ("КАРТИНКИ", "*.png*"), 
                                   ("ПАЙТОН ФАЙЛЫ", "*.py*")))
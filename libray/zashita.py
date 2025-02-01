import os

log = open("libray/log/log.log", "w", encoding="utf-8")

log.write(str(os.popen("tasklist")))

tasklist = os.popen("start cmd , tasklist")

print("kfeg")
print(tasklist)
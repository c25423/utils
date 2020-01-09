import os
import glob

file_list = glob.glob("*.txt")
for file_name in file_list:
    bak_name = file_name + ".bak"
    os.system("mv " + file_name + " " + bak_name)
    os.system("iconv -f cp936 -t utf-8 "+ bak_name + " > " + file_name)
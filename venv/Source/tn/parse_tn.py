import glob
import codecs
import json
import re
import requests
import time
from bs4 import BeautifulSoup
import ntpath
import os
import shutil

# files = ["/Users/grishy/projects/Scripts/tn/25.htm"]
# files = glob.glob("C:/Users/MonAmi/Desktop/CDSS/Scripts/tn/*")

def parse_file(file):
    # file = codecs.open(path, "r", "cp1251")
    soup = BeautifulSoup(file,'html5lib')

    # del all noprint
    for div in soup.find_all(None, {'class': 'noprint'}):
        div.decompose()

    drug = soup.findAll("div", {"class": "drug__content"})[0]
    tags = drug.find_all(None, recursive=False)

    info = {}
    name = "Название"
    for tag in soup.find_all("div", class_="main__content"):
        for h1 in tag.find_all('h1'):
            name_drug=h1.text.split('(')[0]
            info[name] = [name_drug]

    name = "_before"
    for tag in tags:
        if tag.name == "h2":
            name = tag.text
            continue

        if name in info:
            info[name].append(tag.prettify())
        else:
            info[name] = [tag.prettify()]

    # to html
    for key in info:
        info[key] = ''.join(info[key])
    return info

i=0
os.chdir("C:/CDSS/venv/Scripts/Resources/MKB-10")
out='C:/Users/MonAmi/Desktop/CDSS/venv/Source/tn_all/'
for root, dirs,files in os.walk(".", topdown = True):
    for name in files:
        if(root.split('\\')[-1]=='tn'):
            file_name,file_ex= os.path.splitext(name)
            print(i,'  ',root,'\\',name, file_name.split('_')[-1])
            i=i+1
            file_path=os.path.join(root,name)
            with open(file_path, 'r',encoding='cp1251') as f:
                p = parse_file(f)
                with open(out + file_name.split('_')[-1] + ".json", 'w', encoding='utf8') as json_file:
                    json.dump(p, json_file, indent=4, ensure_ascii=False)
# for f in files:
#     fileName = ntpath.basename(f)
#     name = os.path.splitext(fileName)[0]
#     print(f)
#     p = parse_file(f)
#     with open(out + name + ".json", 'w', encoding='utf8') as json_file:
#         json.dump(p, json_file, indent=4, ensure_ascii=False)

import glob
import codecs
import json
import re
import requests
import time
from bs4 import BeautifulSoup
import ntpath
import os


# files = ["/Users/grishy/projects/Scripts/tn/25.htm"]
files = glob.glob("/Users/grishy/projects/Scripts/tn/*")

def parse_file(path):
    file = codecs.open(path, "r", "cp1251")
    soup = BeautifulSoup(file.read(), 'lxml')

    # del all noprint
    for div in soup.find_all(None, {'class': 'noprint'}):
        div.decompose()

    drug = soup.findAll("div", {"class": "drug__content"})[0]
    tags = drug.find_all(None, recursive=False)

    info = {}

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


out = "/Users/grishy/projects/CDSS/venv/Source/tn_json/"
for f in files:
    fileName = ntpath.basename(f)
    name = os.path.splitext(fileName)[0]
    print(f)
    p = parse_file(f)
    with open(out + name + ".json", 'w', encoding='utf8') as json_file:
        json.dump(p, json_file, indent=4, ensure_ascii=False)

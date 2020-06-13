import glob
import codecs
import json
import re
import requests
import time
from bs4 import BeautifulSoup
import ntpath
import os


files = glob.glob("/Users/grishy/projects/CDSS/venv/Source/tn_json/*")

stat = {}

for f in files:
    with open(f) as json_file:
        for key in json.load(json_file):
            stat[key] = stat.get(key, 0) + 1

dictlist = []
for key in stat:
    temp = [key,stat[key]]
    dictlist.append(temp)

dictlist.sort(key = lambda i: i[1], reverse=True)

for k in dictlist:
    print(k)
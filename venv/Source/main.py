import requests
import random
import time
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import json

import Source.Parsing.parse_htm_by_url as parseFileHTMByURL
import Source.Parsing.paths as paths
import Source.Parsing.getDrugsForDownloadedMKB as getDrug

def getDiseases(url):
  r = parseFileHTMByURL.parseFileHTM(url)
  if (r != None):
    pathURL = urlparse(url)
    diseaseName = urlparse(url).path.split('_')[0].split('/')[-1]
    diseasePath = os.path.join(paths.path_disease,diseaseName.path)
    print(url,diseasePath)
    with open(diseasePath, 'w', encoding="cp1251") as output_file:
      output_file.write(r.text)

def getST(all_disease):
  url = 'https://www.rlsnet.ru/mkb_tree.htm'
  getDiseases(url)

  if(all_disease):
    i=0
    while (i < 10000):
      url = 'https://www.rlsnet.ru/mkb_index_id_%d.htm' % (i)
      getDiseases(url)
      i=i+1

getST(True)
getDrug.getResources()

# import json
# import requests
# import time
# import os
#
# with open('C:/CDSS/articals.json', encoding='utf8' ) as json_file:
#     data = json.load(json_file)
#     count = 0;
#     for p in data:
#       id = p["Id"]
#       url = 'https://democenter.nitrosbase.com/clinrecalg5//API.ashx?op=GetClinrec2&id=%d&ssid=' % (id) # url для второй страницы
#       r = requests.get(url)
#       print("count:",count,"req:", id, r.status_code)
#       # print(r.text)
#       count = count+ 1
#       path = "./bolezni/"+str(id)+".json"
#       if (r.status_code == 200):
#           with open(path, 'w', encoding="utf-8") as output_file:
#             output_file.write(r.text)
#
#       time.sleep(0.4)
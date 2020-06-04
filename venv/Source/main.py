import requests
import random
import time
from bs4 import BeautifulSoup
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
import os
from urllib.parse import urlparse

def delay() -> None:
  time.sleep(random.random() * 2)
  return None

def checkIP():
  socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
  socket.socket = socks.socksocket
  ip = requests.get('http://checkip.dyndns.org').content
  soup = BeautifulSoup(ip, 'html.parser')
  print(soup.find('body').text)

# for i in range(10):
#     checkIP()
#     time.sleep(5)

i=0
while (i < 10000):
  try:
    # url = 'https://www.rlsnet.ru/mkb_tree.htm'  # url для второй страницы
    url = 'https://www.rlsnet.ru/mkb_index_id_%d.htm' % (i)  # url для второй страницы
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    r = requests.get(url, headers=headers)
    pathURL = urlparse(url)
    fdfds=urlparse(url).path.split('_')[0].split('/')[-1]
    path = "."+pathURL.path
    print(path)
    print(url, r.status_code)
    if (r.status_code == 200):
      with open(path, 'w',encoding="cp1251") as output_file:
        d = r.text
        output_file.write(d)
        i = i + 1
    elif (r.status_code == 403):
      r.status_code = "Connection refused"
      print("ZZzzzz...")
      time.sleep(10)
      checkIP()
      delay()
    else:
      i=i+1

  except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"
    print("ZZzzzz...")
    time.sleep(10)
    checkIP()
    continue


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
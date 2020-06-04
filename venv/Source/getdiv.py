# from bs4 import BeautifulSoup
# from requests import get
# url = 'http://sethgodin.typepad.com/seths_blog/2016/11/the-yeasayer.html'
# htmlString = get(url).text
# html = BeautifulSoup(htmlString, 'lxml')
# entries = html.find_all('div', {'class':'entry-body'})
# text = [e.get_text() for e in entries]
# print('{} posts were found.'.format(len(text)))
# print(text[0])
import requests
import random
import time
from bs4 import BeautifulSoup as bs
import html5lib
import shutil
import os
from urllib.parse import urlparse
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
import os
from urllib.parse import urlparse

def createFolger(newPathFiles):
    if (os.path.exists(newPathFiles) == False):
        os.mkdir(newPathFiles)

def createFiLe(pathFile,newPathFiles):
    if (os.path.exists(newPathFiles + '/' + newPathFiles.split('/')[-1]) == False):
        cmd='copy %s %s' %(pathFile,newPathFiles + '/' + newPathFiles.split('/')[-1]+'.htm')
        # os.popen(cmd)
        shutil.copy2(pathFile, newPathFiles + '/' + newPathFiles.split('/')[-1]+'.htm')

def delay() -> None:
  time.sleep(random.random() * 2)
  return None

def checkIP():
  socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
  socket.socket = socks.socksocket
  ip = requests.get('http://checkip.dyndns.org').content
  soup = bs(ip, 'html.parser')
  print(soup.find('body').text)

def parseFileHTM(url):
    while (1):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
            r = requests.get(url, headers=headers)
            if (r.status_code == 200):
                return r
            elif (r.status_code == 403):
                r.status_code = "Connection refused"
                print("ZZzzzz...")
                time.sleep(10)
                checkIP()
                delay()
            elif (r.status_code == 404):
                return None

        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"
            print("ZZzzzz...")
            time.sleep(10)
            checkIP()

def getNameOfDrug(r):
    d = r.text
    soup = bs(d, 'html5lib')
    for tag in soup.find_all("div", class_="main__content"):
        for h1 in tag.find_all('h1'):
            return h1.text.split('(')[-1].split(')')[0].replace('/','&')

def addDrug(url,pathOfMKB,id):
    r=parseFileHTM(url)
    if (r!=None):
        typeOfDrug = urlparse(url).path.split('_')[0].split('/')[-1]
        pathOfDrug=pathOfMKB+'/'+typeOfDrug
        createFolger(pathOfDrug)
        print(getNameOfDrug(r))
        with open(pathOfDrug+'/'+getNameOfDrug(r)+'_'+id+'.htm', 'w', encoding="cp1251") as output_file:
            output_file.write(r.text)


pathFiles='C:/CDSS/venv/Scripts/mkb'
_newPathFiles='C:/CDSS/venv/Scripts/Resources/MKB-10'

def fileeee(pathFile,i,newPathFiles):
    with open(pathFile, 'r', encoding='cp1251') as file:
        html = file.read()
        createFolger(newPathFiles)
        createFiLe(pathFile, newPathFiles)
        soup = bs(html, 'html5lib')
        for tag in soup.find_all("a", class_="subcatlist__link"):
            name = tag['href'][len('//'):].split("/")[-1]
            tabwrite=""
            for t in range(i):
                tabwrite=tabwrite+"\t";
            print(tabwrite,'href =', name, ' ', tag.text)
            pathFile = pathFiles + '/' + name
            fileeee(pathFile,i+1,newPathFiles+'/'+tag.text.split(" ")[0].split('*')[0])
        for tr in soup.find_all('tr'):
            tds=tr.find_all('td',class_="rest_data")
            for j in range(len(tds)):
                addDrug('https:'+tds[j].find('a')['href'],newPathFiles,tds[j].find('a')['href'].split('/')[-1].split('_')[-1])



# addDrug('https://www.rlsnet.ru/mnn_index_id_35.htm','C:/CDSS/venv/Scripts/test')
# pathFile='C:/CDSS/venv/Scripts/mnn/mnn_index_id_1034.htm'
# with open(pathFile, 'r',encoding='cp1251') as file:
#     html = file.read()
#     soup = bs(html, 'html5lib')
#     for tag in soup.find_all("div",class_="main__content"):
#         for h1 in tag.find_all('h1'):
#             print(h1.text.split('(')[-1].split(')')[0])

pathFile='C:/CDSS/venv/Scripts/mkb_tree.htm'
with open(pathFile, 'r',encoding='cp1251') as file:
    html = file.read()
    soup = bs(html, 'html5lib')
    for tag in soup.find_all("a",class_="classification__link classification__link--upper"):
        name=tag['href'][len('//'):].split("/")[-1]
        print('href =',name,' ',tag.text)
        pathFile=pathFiles+'/'+name
        fileeee(pathFile,1,_newPathFiles+'/'+tag.text.split(" ")[0].split('*')[0])

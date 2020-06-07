import requests
import random
import time
from bs4 import BeautifulSoup as bs
import os
import socks
import socket
socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket

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
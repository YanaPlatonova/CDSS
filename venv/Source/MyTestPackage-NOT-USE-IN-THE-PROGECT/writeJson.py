import json
from bs4 import BeautifulSoup as bs
import html5lib
import os
import re
# class Drug:
#     def __init__(self, id, name
#                  ,mkb,adult,child,ssid,created,schemes,
#                  textBlock,textBlockCreatedBy,textBlockCreatedAt
#                  ,status,createdBy,code,NPC_approved,publish_date,tables
#                  ,obj,
#                  ):
#         self.id = id
#         self.name = name
#         self.mkb = mkb
#         self.adult = adult
#         self.child = child
#         self.doc_key_words = obj['sections'][2]['content']
#         self.doc_terms = obj['sections'][4]['content']
#         self.doc_description = obj['sections'][5]['content']
#         self.doc_diagnostics = obj['sections'][6]['content']
#         self.doc_treatment = obj['sections'][7]['content']
#         self.doc_rehabilitation = obj['sections'][8]['content']
#         self.doc_prevention = obj['sections'][9]['content']
#         self.doc_additional = obj['sections'][10]['content']
#         self.doc_criteria = obj['sections'][11]['content']
#
#     @classmethod
#     def from_json(cls, json_string):
#         json_dict = json.loads(json_string)
#         return cls(**json_dict)

def getResource1(idDiv,soup):
    dictOfContent = dict()
    dictOfContent.setdefault('div',[]).append(idDiv)
    tag=soup.find("div", id=re.compile(idDiv))
    if tag!=None:
        for t in tag.findAllNext():
            if(t.name=='div'):
                break
            if(t.name=='span' and t.get('class')=="sokr"):
                continue
            if(t.name=='h2'):
                dictOfContent.setdefault('h2',[]).append(t.text)
            else:
                dictOfContent.setdefault('p',[]).append(t.text)
    return dictOfContent

def getResource2(soup):
    dictOfContent = dict()
    tag=soup.find_all('h3')
    for h3 in range(len(tag)):
        dictOfContent.setdefault(tag[h3].text, []).append(tag[h3].find_next('div').text)
        # if(tag.name=='h3'):
        #     print(tag.text)
        #     for t in tag.parent.find_next('div'):
        #         print(t.text)
        # if (tag.get('class')==['WordSection1']):
        #     if(tag["class"]):
        #         tag_text=tag.text
        #         dictOfContent.setdefault(tag_name, []).append(tag_text)
    return dictOfContent

def doit():
    pathFile=os.getcwd()+'/Scripts/Resources/MKB-10/A00-В99/A00-A09/A05/A05.1/tn/Sera antibotulinica typorum B purificata concentrata liquida_15755.htm.htm'
    # pathFile=os.getcwd()+'/Scripts/Resources/MKB-10/A00-В99/A00-A09/A00/A00.9/tn/Haemodes-N_4341.htm.htm'
    # pathFile=os.getcwd()+'/Scripts/Resources/MKB-10/A00-В99/A00-A09/A00/A00.9/tn/Doxycycline hydrochloride_1341.htm.htm'
    with open(pathFile, 'r',encoding='cp1251') as file:
        html = file.read()
        soup = bs(html, 'html5lib')
        print(getResource1('farmakologicheskoe-dejstvie', soup))
        print('\n')
        print(getResource1('farmakodinamika', soup))
        print('\n')
        print(getResource1('farmakokinetika', soup))
        print('\n')
        print(getResource1('farmakologicheskoe-dejstvie', soup))
        print('\n')
        print(getResource1('pokazaniya-preparata', soup))
        print('\n')
        print(getResource1('protivopokazaniya', soup))
        print('\n')
        print(getResource1('pobochnye-dejstviya', soup))
        print('\n')
        print(getResource1('mery-predostorozhnosti', soup))
        print('\n')
        print(getResource1('sposob-primeneniya-i-dozy', soup))
        print('\n')
        print(getResource1('osobye-ukazaniya', soup))
        print('\n')

        print(getResource2(soup.find("div", class_='instructiontext')))
        # dictOfContent=getResource2(soup.find("div", class_='instructiontext'))
        # for i in dictOfContent:
        #     for j in dictOfContent[i]:
        #         print (i, '  ',j)


doit()



from bs4 import BeautifulSoup as bs
import html5lib
import os
from urllib.parse import urlparse
import Source.CreateUpdateFolderFile.creating as createUpdateFolderFile
import Source.Parsing.parse_htm_by_url as parseFileHTMByURL
import Source.Parsing.paths as paths

def getNameOfDrug(request_drug):
    text_drug = request_drug.text
    soup = bs(text_drug, 'html5lib')
    for tag in soup.find_all("div", class_="main__content"):
        for h1 in tag.find_all('h1'):
            return h1.text.split('(')[-1].split(')')[0].replace('/','&')

def add_drug(url,path_disease,idDrug):
    request_drug=parseFileHTMByURL.parseFileHTM(url)
    if (request_drug!=None):
        typeOfDrug = urlparse(url).path.split('_')[0].split('/')[-1]
        pathOfDrug=os.path.join(path_disease,typeOfDrug)
        createUpdateFolderFile.createFolger(pathOfDrug)
        nameofDrug=self.getNameOfDrug(request_drug)
        print(nameofDrug)
        with open(os.path.join(pathOfDrug,nameofDrug,idDrug), 'w', encoding="cp1251") as output_file:
            output_file.write(request_drug.text)

def add_disease(path_disease,newPath_disease):
    with open(path_disease, 'r', encoding='cp1251') as file:
        soup = bs(file.read(), 'html5lib')
        createUpdateFolderFile.createFolger(newPath_disease)
        createUpdateFolderFile.createFiLe(path_disease, newPath_disease)
        for tag in soup.find_all("a", class_="subcatlist__link"):
            name = tag['href'][len('//'):].split("/")[-1]
            print('href =', name, ' ', tag.text)
            path_disease = os.path.join(paths.path_disease,name)
            name_rubric=tag.text.split(" ")[0].split('*')[0]
            self.add_disease(path_disease,os.path.join(newPath_disease,name_rubric))
        for tr in soup.find_all('tr'):
            drugs_list=tr.find_all('td',class_="rest_data")
            for j in range(len(drugs_list)):
                idDrug=drugs_list[j].find('a')['href'].split('/')[-1].split('_')[-1]
                add_drug('https:'+drugs_list[j].find('a')['href'],newPath_disease,idDrug)

def getResources():
    path_current_disease=paths.pathFile_mkb_tree
    with open(path_current_disease, 'r',encoding='cp1251') as file:
        soup = bs(file.read(), 'html5lib')
        for tag in soup.find_all("a",class_="classification__link classification__link--upper"):
            name=tag['href'][len('//'):].split("/")[-1]
            print('href =',name,' ',tag.text)
            path_current_disease=os.path.join(paths.path_disease,name)
            mkb_className=tag.text.split(" ")[0].split('*')[0]
            add_disease(path_current_disease,os.path.join(paths.newPath_disease,mkb_className))
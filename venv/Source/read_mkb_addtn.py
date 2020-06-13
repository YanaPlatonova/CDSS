import glob
import codecs
import json
import re
import requests
import time
from bs4 import BeautifulSoup

filePath = "/Users/grishy/projects/CDSS/mkb_tree_raw.json"
infoPath = "/Users/grishy/projects/CDSS/mkb.json"

info = []
with open(infoPath) as json_file:
    info = json.load(json_file)

def find_in_info(id):
    return next((item for item in info if item["id"] == id), None)

def add_info(node):
    id = int(node["id"])
    node["id"] = id
    info_mkb = find_in_info(id)
    fg = []
    mnn = []
    tn = []
    if info_mkb:
        fg = info_mkb["fg"]
        mnn = info_mkb["mnn"]
        tn = info_mkb["tn"]
    node["fg"] = fg
    node["mnn"] = mnn
    node["tn"] = tn

    return info_mkb

def add_all(list):
    for n in list:
        add_info(n)
        if "nodes" in n:
            add_all(n["nodes"])

with open(filePath) as json_file:
    data = json.load(json_file)
    add_all(data)

    with open('/Users/grishy/projects/CDSS/mkb_tree_withInfo.json', 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
# with open('/Users/grishy/projects/CDSS/mkb_tree_info.json', 'w', encoding='utf8') as json_file:
#     json.dump(result, json_file, indent=4, ensure_ascii=False)

# # Получение базового дерева
# file = codecs.open("/Users/grishy/projects/CDSS/tree.html", "r", "utf-8")
#
# def get_list(text):
#     soup = BeautifulSoup(text, 'lxml')
#     table = soup.findAll("table", {"class": "tree_fade"})
#     list = []
#     for t in table:
#         link = t.findAll("a", {"class": "classification__link"})[0]
#         end = len(t.findAll("td", {"class": "tree_empty"})) > 0
#         id = re.findall('\d+', link["href"])[0]
#         obj = {
#             "id": id,
#             "text": link.text,
#         }
#         if not end:
#             obj["nodes"] = []
#         list.append(obj)
#     return list
#
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
# }
#
# def parse(list):
#     for el in list:
#         if "nodes" not in el:
#             return
#         url = 'https://www.rlsnet.ru/mkb_gettreelevel.htm'
#         r = requests.post(url, headers=headers, data={'id': el["id"]})
#         print("req: ", el["id"], r.status_code)
#         sub_list = get_list(r.text)
#         if sub_list != 0:
#             el["nodes"] = sub_list
#         parse(sub_list)
#
#
# for el in root:
#     file_name = '/Users/grishy/projects/CDSS/tree/' + el["id"] + '.json'
#     el_root = parse([el])
#     with open(file_name, 'w', encoding='utf8') as json_file:
#         json.dump(el, json_file, indent=4, ensure_ascii=False)

    # print(30)
    # time.sleep(30)

# with open('/Users/grishy/projects/CDSS/mkb_tree.json', 'w', encoding='utf8') as json_file:
#     json.dump(root, json_file, indent=4, ensure_ascii=False)

# for num, path in enumerate(files, start=1):
#     print("Status {}/{}: {}".format(num, len(files), path))
#     file = codecs.open(path, "r", "cp1251")
#     soup = BeautifulSoup(file.read(), 'lxml')
#
#     breadcrumbs = soup.find(id="breadcrumbs")
#     breadcrumbs_path = [x.strip() for x in breadcrumbs.text.split(">")][4:]
#     id = re.findall('\d+', path)[0]
#
#     fg = []
#     mnn = []
#     tn = []
#
#     table = soup.findAll("table", {"class": "rest_nest"})
#     if len(table) != 0:
#         table = table[0]
#         # get links
#         fgEl = table.findAll("a", href = re.compile(r'.*fg_index_id_*'))
#         mnnEl = table.findAll("a", href = re.compile(r'.*mnn_index_id_*'))
#         tnEl = table.findAll("a", href = re.compile(r'.*tn_index_id_*'))
#
#         # Get href from link
#         fg = [a['href'] for a in fgEl]
#         mnn = [a['href'] for a in mnnEl]
#         tn = [a['href'] for a in tnEl]
#         # Get id from href
#         fg = [re.findall('\d+', str(a))[0] for a in fg]
#         mnn = [re.findall('\d+', str(a))[0] for a in mnn]
#         tn = [re.findall('\d+', str(a))[0] for a in tn]
#         # to int
#         fg = [int(a) for a in fg]
#         mnn = [int(a) for a in mnn]
#         tn = [int(a) for a in tn]
#
#     result_list.append({
#         "id": int(id),
#         "path": breadcrumbs_path,
#         "fg": fg,
#         "mnn": mnn,
#         "tn": tn,
#     })
#
#     node = result_tree
#     for el in breadcrumbs_path:
#         finded = next((i for i in node["nodes"] if i["text"] == el), None)
#         if not finded:
#             finded = {
#                 "id": int(id),
#                 "text": el,
#                 "nodes": [],
#             }
#             node["nodes"].append(finded)
#         node = finded
#         sorted(node["nodes"], key=lambda i: i['text'])
#
# with open('/Users/grishy/projects/CDSS/mkb.json', 'w', encoding='utf8') as json_file:
#     json.dump(result_list, json_file, indent=4, ensure_ascii=False)
#
# with open('/Users/grishy/projects/CDSS/mkb_tree.json', 'w', encoding='utf8') as json_file:
#     json.dump(result_tree, json_file, indent=4, ensure_ascii=False)

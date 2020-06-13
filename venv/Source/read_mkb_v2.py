import glob
import codecs
import json
import re
from bs4 import BeautifulSoup


# print("Status {}/{}: {}".format(num, len(files), path))

# Получение базового дерева
file = codecs.open("/Users/grishy/projects/CDSS/tree.html", "r", "utf-8")
soup = BeautifulSoup(file.read(), 'lxml')

table = soup.findAll("table", {"class": "tree_fade"})
list = []
for t in table:
    link = t.findAll("a", {"class": "classification__link"})[0]
    end = len(t.findAll("td", {"class": "tree_empty"})) > 0
    id = re.findall('\d+', link["href"])[0]
    list.append({
        "id": id,
        "text": link.text,
        "nodes": [],
        "is_end": end,
    })

print(json.dumps(list, indent=4, ensure_ascii=False))
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

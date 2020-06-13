import glob
import codecs
import json
import re
from bs4 import BeautifulSoup

files = glob.glob("/Users/grishy/projects/Scripts/mkb/*.htm")

result = []
for num, path in enumerate(files, start=1):
    print("Status {}/{}: {}".format(num, len(files), path))
    file = codecs.open(path, "r", "cp1251")
    soup = BeautifulSoup(file.read(), 'lxml')

    breadcrumbs = soup.find(id="breadcrumbs")
    breadcrumbs_path = [x.strip() for x in breadcrumbs.text.split(">")][3:]
    id = re.findall('\d+', path)[0]

    fg = []
    mnn = []
    tn = []

    table = soup.findAll("table", {"class": "rest_nest"})
    if len(table) != 0:
        table = table[0]
        # get links
        fgEl = table.findAll("a", href = re.compile(r'.*fg_index_id_*'))
        mnnEl = table.findAll("a", href = re.compile(r'.*mnn_index_id_*'))
        tnEl = table.findAll("a", href = re.compile(r'.*tn_index_id_*'))

        # Get href from link
        fg = [a['href'] for a in fgEl]
        mnn = [a['href'] for a in mnnEl]
        tn = [a['href'] for a in tnEl]
        # Get id from href
        fg = [re.findall('\d+', str(a))[0] for a in fg]
        mnn = [re.findall('\d+', str(a))[0] for a in mnn]
        tn = [re.findall('\d+', str(a))[0] for a in tn]
        # to int
        fg = [int(a) for a in fg]
        mnn = [int(a) for a in mnn]
        tn = [int(a) for a in tn]

    result.append({
        "id": int(id),
        "path": breadcrumbs_path,
        "fg": fg,
        "mnn": mnn,
        "tn": tn,
    })

with open('/Users/grishy/projects/CDSS/mkb.json', 'w', encoding='utf8') as json_file:
    json.dump(result, json_file, indent=4, ensure_ascii=False)

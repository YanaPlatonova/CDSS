from elasticsearch import Elasticsearch
import json
import glob
from datetime import datetime

es=Elasticsearch('http://localhost:9200')
filePath='./venv/Source/es/mkb.json'

tn = glob.glob("C:/Users/MonAmi/Desktop/CDSS/venv/Source/tn_all/*")

doc_path='./venv/Source/tn_all/78.json'
with open(doc_path, encoding='utf8') as json_file:
     data = json.load(json_file)
es.index(index='drug',id=78,body=data)
res=es.get(index='drug',id=78)

query_body = {
  "query": {
    "bool": {
      "must_not": {
        "match": {
          "Противопоказания": "беременностей"
        }
      },
    }
  }
}

res = es.search(index='drug', body=query_body)
print("Got %d Hits:" % res['hits']['total']['value'])
print(res)

doc={
"id_disease": [
        7973,
        7948,
        4134,
        4269,
        4252,
        4124
    ],
}

print(doc['id_disease'][2])


es.index(index='drug',id=78,body=doc)

dsa={'dict':[]}
for i in range(len(doc['id_disease'])):
    dsa['dict'].append( {"terms": { "id_disease": [doc['id_disease'][i]] }})

# dsa={
#     "terms": { "id_disease": [4124] },
#     "terms": { "id_disease": [7973] },
# }

print(dsa['dict'])

query_body={
    "query": {
        "bool": {
            "must": [
                dsa['dict'][0]
            ]
        }
    }
}
res = es.search(index='drug', body=query_body)
print("Got %d Hits:" % res['hits']['total']['value'])
print(res)
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

# data=[]
# with open(filePath, encoding='utf8') as json_file:
#     data = json.load(json_file)
#
# for s in abc:
#     with open(s, encoding='utf8') as json_file:
#         data_35 = json.load(json_file)
#     info={}
#     info["id"]=int(s.split('\\')[-1].split('.')[0])
#     #
#     print(info)
#     data_35.update(info)
#     with open(s, 'w', encoding='utf8') as json_file:
#         json.dump(data_35, json_file, indent=4, ensure_ascii=False)
#
# # with open("a", 'w', encoding='utf8') as json_file:
#     json.dump(p, json_file, indent=4, ensure_ascii=False)
#
# for section, commands in data.items():
#     print(section,'  ',commands)

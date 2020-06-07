import html
import urllib.parse

import json

import os

class Disease:
    def __init__(self, id, name
                 ,mkb,adult,child,ssid,created,schemes,
                 textBlock,textBlockCreatedBy,textBlockCreatedAt
                 ,status,createdBy,code,NPC_approved,publish_date,tables
                 ,obj,
                 ):
        self.id = id
        self.name = name
        self.mkb = mkb
        self.adult = adult
        self.child = child
        self.doc_key_words = obj['sections'][2]['content']
        self.doc_terms = obj['sections'][4]['content']
        self.doc_description = obj['sections'][5]['content']
        self.doc_diagnostics = obj['sections'][6]['content']
        self.doc_treatment = obj['sections'][7]['content']
        self.doc_rehabilitation = obj['sections'][8]['content']
        self.doc_prevention = obj['sections'][9]['content']
        self.doc_additional = obj['sections'][10]['content']
        self.doc_criteria = obj['sections'][11]['content']

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

users_list=[]
pathFile='C:/CDSS/venv/Scripts/out/6.json'
pathFiles='C:/CDSS/venv/Scripts/out'

for root, dirs, files in os.walk("C:/CDSS/venv/Scripts/out/", topdown = False):
    for name in files:
        with open(os.path.join(root, name), encoding='utf8' ) as json_file:
            user_data = json.load(json_file)
            if (user_data.get('fail')):
                print(os.path.join(root, name))
            else:
                users_list.append(Disease(**user_data))


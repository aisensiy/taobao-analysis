#-*- coding: utf8 -*-

import json
import pandas as pd

json_path = u'/Volumes/新加卷/cat_format.json'
dst_path = u'/Volumes/新加卷/cat.csv'

data = json.loads(open(json_path).read())

result = []

def get_flat_cat(prefix, data):
    if data.get('name'):
        result.append({'cid': data.get('cid'), 'desc': prefix + data.get('name')})
        prefix += data.get('name')
    if data.get('children') and len(data.get('children')):
        for item in data['children']:
            get_flat_cat(prefix, item)

get_flat_cat('', data)
print len(result)
print result[:10]

df = pd.DataFrame(result)
df.to_csv(dst_path, encoding='utf8', index=None)

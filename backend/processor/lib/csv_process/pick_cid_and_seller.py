#-*- coding: utf8 -*-

import pandas as pd
import re
import json

csv_path = u'/Volumes/新加卷/extracted_url.csv'
dst_csv_path = u'/Volumes/新加卷/cid_seller_url.csv'

df = pd.read_csv(csv_path, names=['id', 'md5', 'raw', 'json'], header=None, chunksize=10000, doublequote=False, escapechar='\\', na_values='N')
cids = []

def get_cid(x):
    taobaocidpn = re.compile(r'"cid": ?"(\d+)"')
    tmallcidpn  = re.compile(r'"categoryId": ?"(\d+)"')
    m = taobaocidpn.search(x)
    if m:
        return m.group(1)
    else:
        m = tmallcidpn.search(x)
        if m:
            return m.group(1)
    return None

def get_seller(x):
    x = dict(json.loads(x))
    return x.get('seller', None)


for idx, chunk in enumerate(df):
    print idx
    chunk = chunk[chunk['json'].notnull()]
    chunk['cid'] = chunk['json'].map(get_cid)
    chunk['seller'] = chunk['raw'].map(get_seller)
    print chunk['cid'].head()
    print chunk[chunk['cid'].isnull()].json
    cids.append(pd.DataFrame({'urlmd5': chunk['md5'], 'cid': chunk['cid'], 'seller': chunk['seller']}))

ciddf = pd.concat(cids)

ciddf.to_csv(dst_csv_path, index=None, encoding='utf8')

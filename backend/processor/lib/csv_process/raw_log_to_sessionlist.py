#-*- coding: utf8 -*-

import numpy as np
import pandas as pd
from urlparse import urlparse
import json
import hashlib

csv_path = u'/Volumes/新加卷/2013-05-03.csv'
dst_path = u'/Volumes/新加卷/2013-05-13sidlist.csv'
cid_seller_path = u'/Volumes/新加卷/cid_seller_url.csv'
path_anno = u'/Volumes/新加卷/page_annotation.json'
cat_path = u'/Volumes/新加卷/cat.csv'

def md5(source):
    m = hashlib.md5()
    m.update(source)
    return m.hexdigest()

def url_to_urlpath(url):
    obj = urlparse(url)
    if not obj or obj.netloc == '': return None
    return obj.netloc + obj.path

url_anno = json.loads(open(path_anno).read())
def url_type(urlpath):
    if urlpath in url_anno:
        return url_anno[urlpath]['class']
    else:
        return 'unknown'

cid_seller_df = pd.read_csv(cid_seller_path)
print cid_seller_df.head()
df = pd.read_csv(csv_path)

df = df[['id', 'urlmd5', 'url', 'uid', 'sessionid']]

# make tmall md5
df['urlmd5'] = df['url'].map(md5)

# add urlpath
df['urlpath'] = df['url'].map(url_to_urlpath)

# add url type
df['urltype'] = df['urlpath'].map(url_type)

# add cid
# add seller
df = df.merge(cid_seller_df, left_on='urlmd5', right_on='urlmd5', how='left')
df[df.cid.notnull()]['cid'] = df[df.cid.notnull()]['cid'].astype(int)

# add desc for cid
cats = pd.read_csv(cat_path, names=['cid', 'ciddesc'])
df = df.merge(cats, how='left')
print df.head()

# add if female cat
# female_cats = pd.read_csv(female_cat_path, header=None)
# female_cats = set(female_cats[0])
#
# def check_female(x):
#     if not x: return False
#     if x in female_cats:
#         return True
#
# df['isfemalcat'] = df['cid'].map(check_female)

df = pd.DataFrame({'url': df['url'],
                   'id': df['id'],
                   'uid': df['uid'],
                   'urlpath': df['urlpath'],
                   'sessionid': df['sessionid'],
                   'urltype': df['urltype'],
                   'seller': df['seller'],
                   'cid': df['cid'],
                   'ciddesc': df['ciddesc']})

print df.head()
print df[df.cid.notnull()].head()

grouped = df.groupby('sessionid')
sidgrp = grouped['id'].count()
valid_sidlist = list(sidgrp[sidgrp > 3].index)
df = df[df.sessionid.isin(valid_sidlist)]
print 'len after rm invalid session: %d' % len(df)
print df.head()

grouped = df.groupby('sessionid')
result = grouped.agg({'urltype': lambda x: ' '.join(x),
                      'seller': lambda x: ' '.join(map(str, x[x.notnull()])),
                      'cid': lambda x: ' '.join(map(lambda x: str(int(x)), x[x.notnull()])),
                      'ciddesc': lambda x: ' '.join(x[x.notnull()]),
                      'uid': 'max'})
print len(result)
print result[:2]

result.to_csv(dst_path, encoding='utf8')

# -*- coding: utf8 -*-

import pandas as pd

csv_path = u'/Volumes/新加卷/2013-05-13onlyitem.csv'
female_cats = '/Volumes/新加卷/female_cat.csv'
dst_path = u'/Volumes/新加卷/2013-05-13onlyitem.femail.csv'

female_cats = pd.read_csv(female_cats)
female_cats = set(female_cats.cid)

df = pd.read_csv(csv_path)
def mark_female(x):
    x = map(int, x.split(' '))
    for i in x:
        if i in female_cats:
            return True
    return False

df['female'] = df.cid.map(mark_female)

df = df[df['female'] == True]
del df['female']

print len(df)

df.to_csv(dst_path, index=None, encoding='utf8')

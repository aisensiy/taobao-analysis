#-*- coding: utf8 -*-

import pandas as pd

csv_path = u'/Volumes/新加卷/2013-05-13sidlist.csv'
dst_path = u'/Volumes/新加卷/2013-05-13onlyitem.csv'

df = pd.read_csv(csv_path)
print len(df)

df = df[df.seller.notnull()]
print len(df)

df.to_csv(dst_path, encoding='utf8', index=None)

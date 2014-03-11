#-*- coding: utf8 -*-

import pandas as pd
import numpy as np
from datetime import datetime
import time

csv_path = u'/Volumes/新加卷/uidsortedrecordwithsid.csv'
dst_csv_path = u'/Volumes/新加卷/2013-05-03.csv'

df = pd.read_csv(csv_path)
cols = ['id', 'uid', 'ip', 'url', 'site', 'domain', 'date', 'staytime', 'urlmd5', 'sessionid']
df.columns = cols
df = df[df['date'].notnull()]
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

pick_day = '2013-05-03'

sample = df['2013-05-03']

sample.to_csv(dst_csv_path, encoding='utf8')

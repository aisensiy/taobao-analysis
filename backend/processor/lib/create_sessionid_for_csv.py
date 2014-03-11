#-*- coding: utf8 -*-

import pandas as pd
import numpy as np
from datetime import datetime
import time

count = 1
last_uid = None
last_datetime = None
firstline = True

def createsid(row):
    this_datetime = time.mktime(row['date'].timetuple())
    this_uid = row['uid']

    global firstline
    global count
    global last_uid
    global last_datetime

    if firstline:
        row['sessionid'] = count
        firstline = False
    else:
        if this_uid == last_uid and this_datetime - last_datetime <= session_len:
            row['sessionid'] = count
        else:
            count += 1
            row['sessionid'] = count

    last_datetime = this_datetime
    last_uid = this_uid

    return row


csv_path = u'/Volumes/新加卷/uidsortedrecord.csv'
dst_csv_path = u'/Volumes/新加卷/uidsortedrecordwithsid.csv'
session_len = 60 * 15 # 15 min

df = pd.read_csv(csv_path, chunksize=10000)

for idx, chunk in enumerate(df):
    print 'chunk: %d' % idx
    chunk['date'] = pd.to_datetime(chunk['date'])
    chunk = chunk.apply(createsid, axis=1)
    chunk.to_csv(dst_csv_path, index=None, header=None, mode='a')

print 'total count: %d' % count

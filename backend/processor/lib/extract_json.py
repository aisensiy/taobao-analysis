# -*- coding: utf-8 -*-

from db import MySQL as DB
from constants import config
from urllib2 import urlopen
from common import url_to_json, json_to_url, str_ungzip
import json
from pyquery import PyQuery
import re
from parse_json_in_taobao import parse_json as parse_taobao_json
from parse_json_in_tmall import parse_json as parse_tmall_json

tablename = 'url_tmp'
target_tablename = 'extracted_url'

url = 'http://detail.tmall.com/item.htm?id=17551351677&spm=a1z10.1.w7001835-8709588762.16.pc6bHh'

def parse_item(content):
    result = parse_json_in_taobao(content)
    if result != '{}':
        return result
    elss:
        return parse_json_in_tmall(content)

def parse_tmall(content):
    result = parse_json_in_tmall(content)
    if result != '{}':
        return result
    elss:
        return parse_json_in_taobao(content)

rules = {
    'item.taobao.com/item.htm': {
        "json": parse_taobao
    },
    'detail.tmall.com/item.htm': {
        "json": parse_tmall
    }
}

def fetch(url):
    response = urlopen(url)
    code = response.headers.getheader('Content-Type').split('=')[-1]
    return response.read().decode(code, 'ignore')

def extract(html, meta):
    try:
        return meta['json'](html)
    except Exception, e:
        return ""

def match_pattern(url, content):
    obj = url_to_json(url)
    if not obj: return None
    for rule, value in rules.items():
        m = re.match(rule, obj['host'] + obj['path'])
        if m:
            print url
            return extract(content, value)

    return None

def extract_pages(db):
    limit = 999
    skip = 0

    while True:
        rows = db.fetchall("select id, url, content from " + tablename + " where id <= %s and id > %s", (limit + skip, skip))
        if not len(rows): break
        skip += limit

        for row in rows:
            id, url, content = row
            if not content: continue
            result = match_pattern(url, str_ungzip(content))
            if not result: continue
            print url, json.dumps(result)
            db.execute("update " + target_tablename + " set jsons=%s where url_id = %s", (json.dumps(result), id))

        db.commit()

    db.close()

def main():
    db = DB(config)
    extract_pages(db)

if __name__ == '__main__':
    main()
    # db = DB(config)
    # row = db.fetchone('select id, url, content from ' + tablename + ' limit 1 offset 1000')
    # id, url, content = row
    # print match_pattern(url, str_ungzip(content))

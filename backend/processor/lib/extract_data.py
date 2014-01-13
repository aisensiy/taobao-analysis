# -*- coding: utf-8 -*-

from db import MySQL as DB
from constants import config
from urllib2 import urlopen
from common import url_to_json, json_to_url, str_ungzip
import json
from pyquery import PyQuery
import re

tablename = 'url_tmp'

url = 'http://detail.tmall.com/item.htm?spm=a1z10.4.w8632496736.34.Zd1C3H&id=16250626349'

rules = {
    'item.taobao.com/item.htm': {
        "title": {
            "selector": [ "#detail h3" ]
        },
        "price": {
            "selector": ["em.tb-rmb-num"],
            "handler": lambda elem: elem.text().strip()
        },
        "detail": {
            "selector": [ "#attributes .attributes-list" ],
            "handler": lambda elem: dict(map(lambda x: x.strip(), li.text.replace(u'：', ':').split(":", 1)) for li in elem.find('li'))
        },
        "seller": {
            "selector": [".shop-card a.hCard.fn", '.tm-brand em'],
            'handler': lambda elem: elem.attr['title']
        },
        "jsondata": {
        }
    },
    'detail.tmall.com/item.htm': {
        "title": {
            "selector": [ ".tb-detail-hd h3" ]
        },
        "price": {
            "selector": ["#J_StrPrice .tb-rmb-num", '.J_originalPrice'],
            "handler": lambda elem: float(elem.text())
        },
        "detail": {
            "selector": [ "#attributes .attributes-list" ],
            "handler": lambda elem: dict(map(lambda x: x.strip(), li.text.replace(u'：', ':').split(":", 1)) for li in elem.find('li'))
        },
        "seller": {
            "selector": [".shop-card a.hCard.fn", '.tm-brand em']
        }
    }

}

def fetch(url):
    response = urlopen(url)
    code = response.headers.getheader('Content-Type').split('=')[-1]
    return response.read().decode(code, 'ignore')

def extract(html, meta):
    page = PyQuery(html)
    title = page('title')
    print title.text()
    result = []

    for name, entity in meta.items():
        elem = None
        for selector in entity["selector"]:
            elem = page(selector)
            if elem and elem.text():
                if len(elem) > 1: elem = PyQuery(elem[0])
                break

        print '=' * 10
        print selector
        if entity["selector"] == [ "#attributes .attributes-list" ]:
            lis = elem.find('li')
            print len(lis)
            for li in lis:
                print li.text
        else:
            print elem
        print '=' * 10

        if not elem.text(): continue

        handler = entity.get("handler", None)

        if handler:
            value = handler(elem)
        else:
            value = PyQuery(elem).text()

        result.append((name, value))

    return result

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
            db.execute("update " + tablename + " set extracted=%s where id = %s", (json.dumps(result), id))

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

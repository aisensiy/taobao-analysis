# -*- coding: utf-8 -*-

from db import MySQL as DB
from constants import config
from common import url_to_json, json_to_url
import re

rules = {
  'item.taobao.com/item.htm': {
    'params': ['id'],
    'info': u'商品详情'
  },
  '(s|s8|search).taobao.com/search': {
    'params': ['q', 'cat', 'ppath', 'bcoffset', 's'],
    'info': u'搜索'
  },
  'trade.taobao.com/trade/itemlist/list_bought_items.htm': {
    'params': [],
    'info': u'购买列表'
  },
  'wuliu.taobao.com/user/order_detail_new.htm': {
    'params': ['trade_id'] # seller_id
  },
  'login.taobao.com/member/loginByIm.do': {
    'params': ['defaulturl']
  },
  'click.simba.taobao.com/cc_im': {
    'params': ['e']
  },
  'trade.taobao.com/trade/pay_success.htm': {
    'params': ['biz_order_id']
  },
  's.click.taobao.com/t': {
    'params': ['e']
  },
  'i.taobao.com/my_taobao.htm': {
    'params': []
  },
  'trade.taobao.com/trade/detail/tradeSnap.htm': {
    'params': ['tradeID']
  },
  'trade.taobao.com/trade/itemlist/listBoughtItems.htm': {
    'params': []
  },
  'admin.uz.taobao.com/index.do': {
    'params': ['url']
  },
  'trade.taobao.com/trade/trade_success.htm': {
    'params': ['alipay_no', 'seller_id', 'biz_order_id']
  },
  'www.taobao.com/': {
    'params': []
  },
  'ju.taobao.com/tg/home.htm': {
    'params': ['itemId']
  },
  'trade.taobao.com/trade/detail/trade_item_detail.htm': {
    'params': ['bizOrderId']
  },
  'trade.taobao.com/trade/confirm_goods.htm': {
    'params': ['biz_order_id']
  },
  'favorite.taobao.com/collect_list.htm': {
    'params': []
  },
  'vip.taobao.com/vip_home.htm': {
    'params': []
  },
  'trade.taobao.com/trade/itemlist/list_sold_items.htm': {
    'params': []
  },
  'login.taobao.com/member/logout.jhtml': {
    'params': ['redirectURL']
  },
  'try.taobao.com/item.htm': {
    'params': ['id']
  },
  'mai.taobao.com/seller_admin.htm': {
    'params': []
  },
  'redirect.simba.taobao.com/rd': {
    'params': ['f']
  },
  'cart.taobao.com/my_cart.htm': {
    'params': []
  },
  'store.taobao.com/shop/view_shop.htm': {
    'params': ['user_number_id', 'shop_id']
  },
  'vip.taobao.com/tjb/user_coin_detail.htm': {
    'params': []
  },
  'trade.taobao.com/trade/detail/trade_snap.htm': {
    'params': ['tradeID']
  }
}

def match_pattern(url):
  obj = url_to_json(url)
  if not obj: return None
  for rule, value in rules.items():
    m = re.match(rule, obj['host'] + obj['path'])
    if m:
      obj['query'] = dict((k, v) for k, v in obj['query'].items() if k in value['params'])
      return json_to_url(obj)

  return None

def update_cleanurl(db):
  limit = 1000
  skip = 0

  while True:
    rows = db.fetchall("select id, url from url where id <= %s and id > %s", (limit + skip, skip))
    if not len(rows): break
    skip += limit

    for row in rows:
      id, url = row
      if not url: continue
      cleanurl = match_pattern(url)
      if not cleanurl: continue
      db.execute("update url set cleanurl=%s where id = %s", (cleanurl, id))

    db.commit()

  db.close()

def main():
  db = DB(config)
  update_cleanurl(db)

if __name__ == '__main__':
  main()

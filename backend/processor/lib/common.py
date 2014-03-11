# -*- coding: utf-8 -*-

from urlparse import urlparse, parse_qs
from urllib import urlencode
import re
import hashlib
import gzip
from StringIO import StringIO

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def str_ungzip(content):
    """
    Decode gzip and decode utf8
    """
    gzipper = gzip.GzipFile(fileobj=StringIO(content))
    data = gzipper.read()
    data = data.decode('utf-8')
    return data


def url_to_json(url):
  obj = urlparse(url)
  if obj.netloc == '': return None
  return {
    'host': obj.netloc,
    'path': obj.path,
    'query': dict((k, len(v) == 1 and v[0] or v) for k, v in parse_qs(obj.query).items())
  }

def json_to_url(obj):
  pn = re.compile(r'%[0-9a-z][0-9a-z]')
  try:
    return "http://%s%s%s" % (obj['host'], obj['path'], len(urlencode(obj['query'])) and '?' + re.sub(pn, (lambda x: x.group(0).upper()), urlencode(obj['query'])) or '')
  except Exception, e:
    print obj
    raise e

def md5(source):
  m = hashlib.md5()
  m.update(source)
  return m.hexdigest()



if __name__ == '__main__':
  url = 'http://s.taobao.com/search?promote=0&initiative_id=staobaoz_20130501&tab=all&q=%C4%D0%CD%AF%CF%C4%D7%B0%C0%F1%B7%FE&s=80'
  obj = url_to_json(url)
  print json_to_url(obj)

from nose.tools import *
import create_site_column as csc

def test_url_to_json():
  url = "http://paimai.taobao.com/pmp/auction.htm?spm=a2129.3065509.6861957.3.bsgxBK&id=35110807706"

  obj = csc.url_to_json(url)
  assert_equal('paimai.taobao.com', obj['host'])
  assert_equal('/pmp/auction.htm', obj['path'])
  assert_equal({'spm': 'a2129.3065509.6861957.3.bsgxBK', 'id': '35110807706'}, obj['query'])

def test_no_empty_params():
  """docstring for test_no_empty_params"""
  url = "http://paimai.taobao.com/pmp/auction.htm?a=&spm=a2129.3065509.6861957.3.bsgxBK&id=35110807706"
  obj = csc.url_to_json(url)

  assert obj['query'].has_key('a') == False

def test_invalid_url():
  """docstring for test_invalid_url"""
  url = 'asdfsadf'
  obj = csc.url_to_json(url)
  assert obj == None

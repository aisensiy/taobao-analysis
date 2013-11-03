from nose.tools import *
import create_cleanurl as cc
from common import url_to_json

def test_rules():
  url = 'http://item.taobao.com/item.htm?spm=a1z0k.1000775.1.47.vvrs9l&id=17906894855'
  assert_equal('http://item.taobao.com/item.htm?id=17906894855', cc.match_pattern(url))

  url = 'http://s.taobao.com/search?spm=a230r.1.7.5.i1XNiF&initiative_id=staobaoz_20130501&tab=old&q=s132242'
  assert_equal('http://s.taobao.com/search?q=s132242', cc.match_pattern(url))

  url = 'http://s8.taobao.com/search?q=%D3%EF%CE%C4%B1%D8%D0%DE2&cat=0&pid=mm_40297119_3498309_11441409&mode=23&commend=1%2C2'
  assert_equal('http://s8.taobao.com/search?q=%D3%EF%CE%C4%B1%D8%D0%DE2&cat=0', cc.match_pattern(url))

  url = 'http://s.taobao.com/search?spm=a230r.1.3.1.qaQJr4&initiative_id=tbindexz_20131010&tab=all&q=%D7%C0%D7%D3&cps=yes&promote=0&cat=50094979&from=compass&ppath=10187632%3A31867&bcoffset=1&s=40#J_relative'
  assert_equal(url_to_json('http://s.taobao.com/search?q=%D7%C0%D7%D3&cat=50094979&ppath=10187632%3A31867&bcoffset=1&s=40'), url_to_json(cc.match_pattern(url)))

  url = 'http://trade.taobao.com/trade/itemlist/list_bought_items.htm?spm=a1z02.1.0.19.5IdfS0'
  assert_equal('http://trade.taobao.com/trade/itemlist/list_bought_items.htm', cc.match_pattern(url))

  url = 'http://wuliu.taobao.com/user/order_detail_new.htm?trade_id=138282426286227&seller_id=679118663'
  assert_equal('http://wuliu.taobao.com/user/order_detail_new.htm?trade_id=138282426286227', cc.match_pattern(url))

  url = 'http://login.taobao.com/member/loginByIm.do?_input_charset=utf-8&uid=cntaobaoilh907&token=6d8176397dd250037a7fa93db4c52aca&act=SignIn&time=1367393910643&asker=AliIM&asker_version=7.20.11T&defaulturl=http%3a%2f%2fvip.etao.com%2fyouhui.htm%3fdrawCredits%26tb_lm_id%3dw_wangwang_wuzhao%26paymentId%3d334796169678719%26sign%3d065e3a8b010c1fd9e6c74d80bca5eb25&nv=Y&webpas=cntaobaoilh907748D6376-7F49-1F4C-8852-C55B4E693194'
  assert_equal('http://login.taobao.com/member/loginByIm.do?defaulturl=http%3A%2F%2Fvip.etao.com%2Fyouhui.htm%3FdrawCredits%26tb_lm_id%3Dw_wangwang_wuzhao%26paymentId%3D334796169678719%26sign%3D065e3a8b010c1fd9e6c74d80bca5eb25', cc.match_pattern(url))

  url = 'http://click.simba.taobao.com/cc_im?p=&s=426415923&k=321&e=Riy4%2FzZq4zfQWRt2KnoKxrlnITmtMjR7v8qSERl2qQlNIg2WUQimHO8wale%2FTESDQlysWwWosm0w1py50kNqOgovpr8LF40zOod1md0QxiO39pfK105P2LNkMNEkNP5IoNCPrikgiifCoPajbh2cW1mW%2F30%2FNRgd2HYl5TfryLhxrxWMYHY7R2gIt2Bw5d5brRVhA0SjzPbbmrGe0xmpO3QahFsygxzRtXhGEH%2FcLSBUj9MALYzatJJlY0NrepBF3tk4yjshC4Q%2B59GHuNqeTJxtF2VBl96%2F2HYl5TfryLhxrxWMYHY7R%2BF9zCwCx8bq'
  assert_equal('http://click.simba.taobao.com/cc_im?e=Riy4%2FzZq4zfQWRt2KnoKxrlnITmtMjR7v8qSERl2qQlNIg2WUQimHO8wale%2FTESDQlysWwWosm0w1py50kNqOgovpr8LF40zOod1md0QxiO39pfK105P2LNkMNEkNP5IoNCPrikgiifCoPajbh2cW1mW%2F30%2FNRgd2HYl5TfryLhxrxWMYHY7R2gIt2Bw5d5brRVhA0SjzPbbmrGe0xmpO3QahFsygxzRtXhGEH%2FcLSBUj9MALYzatJJlY0NrepBF3tk4yjshC4Q%2B59GHuNqeTJxtF2VBl96%2F2HYl5TfryLhxrxWMYHY7R%2BF9zCwCx8bq', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/pay_success.htm?biz_order_id=337652840237576&notify_id=RqPnCoPT3K9%252Fvwbh3I73%252BKMThU0w5OsljyQqAcVjB0lmwiFoxFoSvg60XsWeuQgph%252FvZ&notify_time=2013-05-01+18%3A05%3A46&out_trade_no=T200P337652840237576&trade_no=2013050100001000380002208349&sign=mocksigncontent&sign_type=DSA'
  assert_equal('http://trade.taobao.com/trade/pay_success.htm?biz_order_id=337652840237576', cc.match_pattern(url))

  url = 'http://s.click.taobao.com/t?e=zGU34CA7K%2BPkqB07S4%2FK0CFcRfH0GoT805sipKj1yK1OVPKIAKPZTiZKHg9nPxW7FpYfQdZW17oFQ17%2FS8N34omUA65B9moagKkTxVNEdI7CTek%3D'
  assert_equal(url, cc.match_pattern(url))

  url = 'http://i.taobao.com/my_taobao.htm?spm=0.0.0.0.uvnjIF'
  assert_equal('http://i.taobao.com/my_taobao.htm', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/detail/tradeSnap.htm?spm=a1z09.2.9.9.bJNJtU&tradeID=253528838604809'
  assert_equal('http://trade.taobao.com/trade/detail/tradeSnap.htm?tradeID=253528838604809', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/itemlist/listBoughtItems.htm?spm=a1z09.2.7.2.txnn3j&action=itemlist/QueryAction&event_submit_do_query=1&auctionStatus=SEND'
  assert_equal('http://trade.taobao.com/trade/itemlist/listBoughtItems.htm', cc.match_pattern(url))

  url = 'http://admin.uz.taobao.com/index.do?spm=a2116.2175081.0.145.6lBQll&action=site/GetCpsAction&event_submit_do_get=true&_input_charset=UTF-8&url=http%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D15341334753%26spm%3D2014.21018550.0.0&userId=1074509866&domain=http://coubei.uz.taobao.com/'
  assert_equal('http://admin.uz.taobao.com/index.do?url=http%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D15341334753%26spm%3D2014.21018550.0.0', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/trade_success.htm?alipay_no=2012052459978841&seller_id=2088702661844884&biz_order_id=137460332476413'
  assert_equal(url_to_json('http://trade.taobao.com/trade/trade_success.htm?alipay_no=2012052459978841&seller_id=2088702661844884&biz_order_id=137460332476413'), url_to_json(cc.match_pattern(url)))

  url = 'http://www.taobao.com/?spm=a1z09.2.0.10.AGpsV1'
  assert_equal('http://www.taobao.com/', cc.match_pattern(url))

  url = 'http://ju.taobao.com/tg/home.htm?spm=a220o.1000855.0.70.R5GbML&itemId=19096447721&'
  assert_equal('http://ju.taobao.com/tg/home.htm?itemId=19096447721', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/detail/trade_item_detail.htm?spm=a1z09.2.9.55.40sscv&bizOrderId=336579169123440'
  assert_equal('http://trade.taobao.com/trade/detail/trade_item_detail.htm?bizOrderId=336579169123440', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/confirm_goods.htm?spm=a1z09.2.9.14.smf8sw&biz_order_id=214581931377144'
  assert_equal('http://trade.taobao.com/trade/confirm_goods.htm?biz_order_id=214581931377144', cc.match_pattern(url))

  url = 'http://favorite.taobao.com/collect_list.htm?spm=1.1000386.0.32.tkMyza&itemtype=1'
  assert_equal('http://favorite.taobao.com/collect_list.htm', cc.match_pattern(url))

  url = 'http://vip.taobao.com/vip_home.htm?ad_id=&am_id=&cm_id=140022308277fff826e5&pm_id='
  assert_equal('http://vip.taobao.com/vip_home.htm', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/itemlist/list_sold_items.htm'
  assert_equal('http://trade.taobao.com/trade/itemlist/list_sold_items.htm', cc.match_pattern(url))

  url = 'http://login.taobao.com/member/logout.jhtml?spm=a1z09.2.0.6.SdAKUY&f=top&out=true&redirectURL=http%3A%2F%2Ftrade.taobao.com%2Ftrade%2Fitemlist%2Flist_bought_items.htm%3Fspm%3Da1z02.1.0.19.mN5auB'
  assert_equal('http://login.taobao.com/member/logout.jhtml?redirectURL=http%3A%2F%2Ftrade.taobao.com%2Ftrade%2Fitemlist%2Flist_bought_items.htm%3Fspm%3Da1z02.1.0.19.mN5auB', cc.match_pattern(url))

  url = 'http://try.taobao.com/item.htm?spm=a1z0i.1000798.1000585.7.4uLt98&id=5658364'
  assert_equal('http://try.taobao.com/item.htm?id=5658364', cc.match_pattern(url))

  url = 'http://mai.taobao.com/seller_admin.htm?spm=a1z09.3.0.30.TSNeLl'
  assert_equal('http://mai.taobao.com/seller_admin.htm', cc.match_pattern(url))

  url = 'http://redirect.simba.taobao.com/rd?&k=dd56fa41e1011fe7&b=386_101370_4_0_1011704711&f=http%3A%2F%2Ftao.etao.com%2Fsearch%3F_input_charset%3Dutf-8%26catid%3D1622%26refpid%3Dmm_13087935_2078460_8372209%26keyword%3D%25E5%25A5%25B3%25E8%25A3%25A4%2B%25E9%2595%25BF%25E8%25A3%25A4%26refpos%3D386_101370_4%2Cn%2Ca&p=mm_13087935_2078460_8372209&pvid=1_1367406244_4402317_525869706&w=unionpost&c=un'
  assert_equal('http://redirect.simba.taobao.com/rd?f=http%3A%2F%2Ftao.etao.com%2Fsearch%3F_input_charset%3Dutf-8%26catid%3D1622%26refpid%3Dmm_13087935_2078460_8372209%26keyword%3D%25E5%25A5%25B3%25E8%25A3%25A4%2B%25E9%2595%25BF%25E8%25A3%25A4%26refpos%3D386_101370_4%2Cn%2Ca', cc.match_pattern(url))

  url = 'http://cart.taobao.com/my_cart.htm?spm=2013.1.0.274.EKO0S9&ct=7986f5d70a86f4cff04997f63b2dd34a'
  assert_equal('http://cart.taobao.com/my_cart.htm', cc.match_pattern(url))

  url = 'http://store.taobao.com/shop/view_shop.htm?spm=a230r.1.14.6.ZK0mcH&user_number_id=345894189'
  assert_equal('http://store.taobao.com/shop/view_shop.htm?user_number_id=345894189', cc.match_pattern(url))

  url = 'http://vip.taobao.com/tjb/user_coin_detail.htm?spm=0.0.0.0.Eq7VY2'
  assert_equal('http://vip.taobao.com/tjb/user_coin_detail.htm', cc.match_pattern(url))

  url = 'http://trade.taobao.com/trade/detail/trade_snap.htm?spm=a1z09.1.11.8.IlGaYi&tradeID=214856970204471'
  assert_equal('http://trade.taobao.com/trade/detail/trade_snap.htm?tradeID=214856970204471', cc.match_pattern(url))

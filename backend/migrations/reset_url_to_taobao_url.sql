update url left join taobao on taobao.url_md5 = url.url_md5 set url.url = taobao.url where url.url != taobao.url;

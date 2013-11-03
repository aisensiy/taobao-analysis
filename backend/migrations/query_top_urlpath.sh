topurlpaths=`mysql --host=162.105.11.227 --user=spider --password=spider11 spide -e 'select urlpath from urlpath_count_for_taobao limit 100\G'`
echo $topurlpaths

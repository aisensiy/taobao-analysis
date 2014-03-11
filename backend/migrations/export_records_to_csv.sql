SELECT id, uid, ip, url, site, domain, date, staytime, url_md5, sessionid
FROM taobao
INTO OUTFILE '/Volumes/新加卷/record.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

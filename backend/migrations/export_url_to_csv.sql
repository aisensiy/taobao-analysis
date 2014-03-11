SELECT id, url, cleanurl, urlpath, url_md5, title, description
FROM url
INTO OUTFILE '/tmp/url.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

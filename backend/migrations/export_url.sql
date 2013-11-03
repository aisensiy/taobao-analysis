SELECT id, url, cleanurl, urlpath, url_md5, title FROM url INTO OUTFILE './url.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n';

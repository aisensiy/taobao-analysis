SELECT url_id, url_md5, extracted
FROM extracted_url
INTO OUTFILE '/tmp/extracted_url.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n';

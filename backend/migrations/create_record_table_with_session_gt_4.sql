-- drop table if exists records;
-- create table records (
--   id int(11) primary key auto_increment,
--   uid varchar(25),
--   ip char(16),
--   url text,
--   site varchar(255),
--   domain varchar(255),
--   referurl text,
--   date datetime,
--   staytime int(11),
--   url_kw text,
--   refer_kw text,
--   url_md5 char(32),
--   sessionid int(11)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- insert into records (id, uid, ip, url, site, domain, referurl, date, staytime, url_kw, refer_kw, url_md5, sessionid)
--   select id, uid, ip, url, site, domain, referurl, date, staytime, url_kw, refer_kw, url_md5, sessionid
--     from taobao where sessionid IN (select sessionid from taobao group by sessionid having count(id) > 4) order by id;
select id, uid, ip, url, site, domain, referurl, date, staytime, url_kw, refer_kw, url_md5, sessionid
  from taobao where sessionid IN (select sessionid from taobao group by sessionid having count(id) > 4) order by id
  INTO OUTFILE '/tmp/records.csv' FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

create TABLE IF NOT EXISTS site_count_for_taobao (site varchar(100), url_count int) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
insert into site_count_for_taobao (site, url_count) select newsite, count(url) as url_count from taobao group by newsite order by url_count desc;

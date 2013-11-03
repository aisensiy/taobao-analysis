create TABLE IF NOT EXISTS newsite_count_for_taobao_table (urlpath varchar(100), url_count int) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
insert into urlpath_count_for_taobao (urlpath, url_count) select urlpath, count(url) as url_count from url group by urlpath order by url_count desc;

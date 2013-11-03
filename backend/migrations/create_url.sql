create table IF NOT EXISTS url(
  id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  url text NOT NULL,
  cleanurl text,
  urlpath text,
  url_md5 char(32),
  title text
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci


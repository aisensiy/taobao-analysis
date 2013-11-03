drop table if exists users_have_records;
create table users_have_records (
  id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  uid text,
  age tinyint,
  gender tinyint,
  city int,
  income_pre int,
  income_fml int,
  education int,
  job int,
  industry int,
  birth text
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into users_have_records (uid, age, gender, city, income_pre, income_fml, education, job, industry, birth) select uid, age, gender, city, income_pre, income_fml, education, job, industry, birth from users where uid in (select distinct uid from taobao);

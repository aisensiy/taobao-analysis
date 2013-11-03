drop table if exists joined_users_have_records;
create table joined_users_have_records (
  id int(11) not null primary key AUTO_INCREMENT,
  uid varchar(30),
  gender tinyint,
  age varchar(30),
  industry varchar(127),
  job varchar(127),
  education varchar(127),
  city varchar(127),
  province varchar(127),
  tier varchar(15),
  income_pre int(11),
  income_fml int(11),
  birth varchar(10)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

insert into joined_users_have_records (uid, gender, age, industry, job, education, city, province, tier, income_pre, income_fml, birth)
select u.uid, u.gender, ages.age_s, ind.industry_s, job.job_s, ed.education_s, re.city_s, re.province_s, re.tier_s, u.income_pre, u.income_fml, u.birth
  from users_have_records as u
  left join industry as ind on u.industry = ind.industry
  left join job on job.job = u.job
  left join education as ed on ed.education = u.education
  left join region as re on re.city = u.city
  left join ages on ages.age = u.age;

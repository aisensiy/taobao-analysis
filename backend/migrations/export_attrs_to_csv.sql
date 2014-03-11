SELECT age, age_s
FROM ages
INTO OUTFILE '/tmp/age.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT education, education_s
FROM education
INTO OUTFILE '/tmp/education.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT industry, industry_s
FROM industry
INTO OUTFILE '/tmp/industry.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT job, job_s
FROM job
INTO OUTFILE '/tmp/job.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT id, city, city_s, province, province_s, region, region_s, tier, tier_s
FROM region
INTO OUTFILE '/tmp/region.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

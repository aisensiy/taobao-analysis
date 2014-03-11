SELECT id, uid, gender, age, city, income_pre, income_fml, education, job, industry, birth
FROM users
INTO OUTFILE '/tmp/user.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

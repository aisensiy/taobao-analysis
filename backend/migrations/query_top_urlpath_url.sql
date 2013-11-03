SELECT `url`.`id` , `url`.`urlpath`
FROM `url` WHERE 3 > ( SELECT count(*) FROM `url` AS `url1` WHERE `url`.`urlpath` = `url1`.`urlpath` AND `url`.`id` > `url1`.`id` )
ORDER BY `url`.`id` DESC
LIMIT 10

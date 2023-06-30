---city_rank_df
SELECT city_name
FROM city_rank_df
WHERE city_name LIKE '%(%' OR city_name LIKE '%)%' OR city_name LIKE '%,%'

--clean the name to one name
UPDATE city_rank_df 
SET city_name = CASE
    WHEN city_name LIKE '%,%' THEN REGEXP_REPLACE(city_name, ',.*$', '')
    WHEN city_name LIKE '%(%' THEN REGEXP_REPLACE(city_name, '\\s*\\(.*?\\)$', '')
    ELSE city_name
END
WHERE city_name LIKE '%,%' OR city_name LIKE '%(%'

--second attempt

UPDATE city_rank_df
SET city_name = CASE
    WHEN city_name LIKE '%,%' THEN REGEXP_REPLACE(city_name, ',.*$', '')
    WHEN city_name LIKE '%(%' THEN REGEXP_REPLACE(REGEXP_REPLACE(city_name, '\\s*\\(.*?\\)$', ''), '\\s*\\(.*\\)', '')
    ELSE city_name
END
WHERE city_name LIKE '%,%' OR city_name LIKE '%(%'

--drop whitespaces and all after it
UPDATE city_rank_df
SET city_name = TRIM(REGEXP_REPLACE(city_name, '\\s*\\(.*?\\)', ''))
WHERE city_name LIKE '%(%'

--next try, and now it works!
UPDATE city_rank_df
SET city_name = CASE
    WHEN POSITION('(' IN city_name) > 0 THEN SUBSTRING(city_name, 1, POSITION('(' ^--IN city_name) - 1)
    ELSE city_name
END
WHERE city_name LIKE '%(%'

--check
SELECT *
FROM city_rank_clean


-- add columns iso3 and id
CREATE TABLE city_rank_clean AS (
  SELECT city_rank_df.*, ccc.iso3, ccc.id
  FROM city_rank_df
  JOIN country_city_code ccc ON city_rank_df.city_name = ccc.city AND city_rank_df.country = ccc.country
);

-- airbnb cleanen
SELECT *
FROM airbnb_prices_clean

--

CREATE TABLE airbnb_prices_clean AS (
  SELECT airbnb_prices_all.*, ccc.id
  FROM airbnb_prices_all
  JOIN country_city_code ccc ON airbnb_prices_all.city = ccc.city);

 
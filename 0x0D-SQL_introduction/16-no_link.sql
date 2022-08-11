-- list all records when name value is not null
SELECT score,name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;

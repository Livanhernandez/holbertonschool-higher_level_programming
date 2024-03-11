-- script that lists all records of second_table in your MySQL server.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
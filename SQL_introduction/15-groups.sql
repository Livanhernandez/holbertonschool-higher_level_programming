-- script that lists the number of records with the same score in the second_table in your My SQL server.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
-- display records above a specific score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

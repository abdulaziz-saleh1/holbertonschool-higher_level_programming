-- script to list records with null name
SELECT name, score
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;

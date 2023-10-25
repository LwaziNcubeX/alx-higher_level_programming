-- A cript that displays the max temperature of each state
SELECT state, MAX(value) AS max_temp
FROM cities
GROUP BY state
ORDER BY state ASC;

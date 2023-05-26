-- script displays the top 3 cities temperature during July and August ordered by temperature(DESC)
WITH July_August(
    SELECT * FROM temperatures WHERE month BETWEEN 7 AND 8
    )SELECT city, AVG(value) AS avg_temp FROM July_August GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
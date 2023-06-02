SELECT count(name), region FROM country
GROUP BY Region
ORDER BY count(name) DESC
SELECT name, Population FROM city
WHERE CountryCode = 'mex' AND
population > 500000
ORDER BY Population DESC
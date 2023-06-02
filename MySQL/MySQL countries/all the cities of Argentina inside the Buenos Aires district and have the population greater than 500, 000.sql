SELECT country.name, city.name, district, city.Population FROM city
JOIN country ON country.code = city.countrycode
WHERE District = 'Buenos Aires'
AND city.Population > 500000
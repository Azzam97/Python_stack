SELECT country.name, count(country.name)
FROM country
JOIN city ON city.CountryCode = Country.Code
GROUP BY country.name
ORDER BY count(country.name) DESC;
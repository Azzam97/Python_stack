SELECT country.name, language, Percentage FROM countrylanguage
JOIN country ON countrylanguage.CountryCode = country.code
WHERE Percentage > 89
ORDER BY Percentage DESC
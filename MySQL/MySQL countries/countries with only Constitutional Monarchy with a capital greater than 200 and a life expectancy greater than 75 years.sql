SELECT name, GovernmentForm, Capital, LifeExpectancy FROM country
WHERE GovernmentForm = 'Constitutional Monarchy'
AND Capital > 200
AND LifeExpectancy > 75
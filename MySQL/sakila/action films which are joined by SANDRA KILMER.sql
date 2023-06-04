SELECT title, description, release_year, rating, special_features, category.name,
 first_name, last_name
 FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
WHERE first_name = 'Sandra'
AND last_name = 'Kilmer'
AND category.name = 'Action'
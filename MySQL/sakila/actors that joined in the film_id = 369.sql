SELECT film.film_id, title, actor.actor_id, first_name  FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film.film_id = 369
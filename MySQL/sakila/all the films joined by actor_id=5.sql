SELECT actor.actor_id, actor.first_name, film.title, film.description, film.release_year FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id = 5
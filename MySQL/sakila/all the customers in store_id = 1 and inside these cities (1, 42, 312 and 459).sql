SELECT store_id, city_id, first_name, last_name, email, address FROM customer
JOIN address ON address.address_id = customer.address_id
where store_id = 1
and (city_id = 1 or city_id = 42 or city_id = 312 or city_id = 459)

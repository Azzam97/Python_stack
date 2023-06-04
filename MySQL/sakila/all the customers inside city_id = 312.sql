select city.city_id,city.city, first_name, last_name, email, address from  customer
join address on address.address_id = customer.address_id
join city on city.city_id = address.city_id
where city.city_id = 312
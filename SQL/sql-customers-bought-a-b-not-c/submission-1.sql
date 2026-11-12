-- Write your query below
SELECT customer_id, customer_name
FROM customers
Where customer_id IN
(SELECT customer_id from orders where product_name='A')
and customer_id IN
(SELECT customer_id from orders where product_name='B')
and customer_id NOT IN
(SELECT customer_id from orders where product_name ='C')
order by customer_name;
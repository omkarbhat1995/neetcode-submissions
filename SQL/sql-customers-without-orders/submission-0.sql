-- Write your query below
/*SELECT c.name 
FROM customers c
left join orders o on c.id = o.customer_id
where o.customer_id IS NULL;
*/
SELECT c.name
FROM customers c
WHERE c.id NOT IN (SELECT o.customer_id FROM orders o);
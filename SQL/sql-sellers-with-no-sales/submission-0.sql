-- Write your query below
SELECT seller_name
FROM seller 
WHERE seller_id NOT IN (
    SELECT seller_id from orders where sale_date>='2020-01-01' and sale_date<='2020-12-31'
)
order by seller_name;
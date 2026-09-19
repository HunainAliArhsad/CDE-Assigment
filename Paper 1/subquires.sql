SELECT 
    p1.product_id,
    p1.product_name,
    p1.category_id,
    p1.list_price
FROM production.products p1
WHERE p1.list_price > (
    SELECT AVG(p2.list_price)
    FROM production.products p2
    WHERE p2.category_id = p1.category_id
);
######################################################
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    COUNT(o.order_id) AS total_orders
FROM sales.customers c
INNER JOIN sales.orders o 
    ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, 
    c.first_name, 
    c.last_name
HAVING COUNT(o.order_id) > (
    SELECT COUNT(order_id) * 1.0 / COUNT(DISTINCT customer_id)
    FROM sales.orders
);
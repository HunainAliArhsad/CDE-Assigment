Exercise 5.1
SELECT 
    p1.product_id,
    p1.product_name,
    p1.brand_id,
    p1.list_price
FROM production.products p1
WHERE p1.list_price > (
    SELECT AVG(p2.list_price)
    FROM production.products p2
    WHERE p2.brand_id = p1.brand_id
);
##########################################
Exercise 5.2
SELECT 
    o.order_id,
    o.customer_id,
    o.order_date,
    o.order_status
FROM sales.orders o
WHERE o.customer_id IN (
    SELECT c.customer_id
    FROM sales.customers c
    WHERE c.state IN ('NY', 'CA')
);
##########################################
Exercise 5.3
SELECT customer_id 
FROM sales.customers
WHERE customer_id NOT IN (
    SELECT customer_id 
    FROM sales.orders 
    WHERE customer_id IS NOT NULL
);
##########################################
Exercise 5.4

SELECT 
    AVG(dt.total_items_per_order * 1.0) AS avg_items_per_order
FROM (
    SELECT 
        order_id,
        SUM(quantity) AS total_items_per_order
    FROM sales.order_items
    GROUP BY order_id
) AS dt;
##########################################
Exercise 5.5

SELECT c.customer_id, c.first_name, c.last_name
FROM sales.customers c
WHERE c.customer_id IN (
    SELECT o.customer_id
    FROM sales.orders o
);

##########################################
Exercise 5.6
SELECT 
    c.customer_id,
    c.first_name,
    recent_orders.order_id,
    recent_orders.order_date
FROM sales.customers c
CROSS APPLY (
    SELECT TOP (3) 
        o.order_id,
        o.order_date
    FROM sales.orders o
    WHERE o.customer_id = c.customer_id
    ORDER BY o.order_date DESC, o.order_id DESC
) AS recent_orders;
##########################################
Exercise 5.7
SELECT product_name, list_price
FROM production.products
WHERE list_price > ALL (
    SELECT p.list_price
    FROM production.products p
    INNER JOIN production.categories c ON p.category_id = c.category_id
    WHERE c.category_name = 'Mountain Bikes'
);

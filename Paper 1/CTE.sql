WITH customer_spend AS (
    SELECT 
        c.customer_id,
        c.first_name || ' ' || c.last_name AS customer_name,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_spend
    FROM sales.customers c
    INNER JOIN sales.orders o 
        ON c.customer_id = o.customer_id
    INNER JOIN sales.order_items oi 
        ON o.order_id = oi.order_id
    GROUP BY 
        c.customer_id, 
        c.first_name, 
        c.last_name
),
spend_categorized AS (
    SELECT 
        customer_id,
        customer_name,
        total_spend,
        DENSE_RANK() OVER (ORDER BY total_spend DESC) AS spend_rank,
        CASE 
            WHEN total_spend > (SELECT AVG(total_spend) FROM customer_spend) THEN 'High'
            ELSE 'Regular'
        END AS customer_label
    FROM customer_spend
)
SELECT 
    customer_id,
    customer_name,
    total_spend,
    spend_rank,
    customer_label
FROM spend_categorized
WHERE spend_rank <= 10
ORDER BY spend_rank;




#################################################################################

WITH product_sales AS (
    SELECT 
        p.category_id,
        p.product_id,
        p.product_name,
        SUM(oi.quantity) AS total_quantity_sold,
        ROW_NUMBER() OVER (
            PARTITION BY p.category_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rank_in_category
    FROM production.products p
    INNER JOIN sales.order_items oi 
        ON p.product_id = oi.product_id
    GROUP BY 
        p.category_id, 
        p.product_id, 
        p.product_name
),
stock_total AS (
    SELECT 
        product_id,
        SUM(quantity) AS total_stock_available
    FROM production.stocks
    GROUP BY product_id
)
SELECT 
    cat.category_name,
    ps.product_name AS best_selling_product,
    ps.total_quantity_sold,
    COALESCE(st.total_stock_available, 0) AS total_stock_available
FROM product_sales ps
INNER JOIN production.categories cat 
    ON ps.category_id = cat.category_id
LEFT JOIN stock_total st 
    ON ps.product_id = st.product_id
WHERE ps.rank_in_category = 1
ORDER BY cat.category_name;
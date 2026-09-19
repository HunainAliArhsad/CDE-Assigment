Group BY:

SELECT 
    st.store_name,
    SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_revenue
FROM sales.stores st
INNER JOIN sales.orders o 
    ON st.store_id = o.store_id
INNER JOIN sales.order_items oi 
    ON o.order_id = oi.order_id
GROUP BY 
    st.store_id, 
    st.store_name
ORDER BY 
    total_revenue DESC;
    ###########################################################################

    SELECT 
    b.brand_name,
    COUNT(p.product_id) AS total_products,
    AVG(p.list_price) AS avg_list_price,
    MAX(p.list_price) AS max_list_price
FROM production.brands b
INNER JOIN production.products p 
    ON b.brand_id = p.brand_id
GROUP BY 
    b.brand_id, 
    b.brand_name
HAVING 
    COUNT(p.product_id) > 5;
    ############################################################################
    SELECT 
    MONTH(o.order_date) AS order_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_revenue
FROM sales.orders o
INNER JOIN sales.order_items oi 
    ON o.order_id = oi.order_id
WHERE 
    YEAR(o.order_date) = 2017
GROUP BY 
    MONTH(o.order_date)
ORDER BY 
    order_month ASC;
    #############################################
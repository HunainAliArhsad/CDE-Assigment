-- Task 1: Sales Detail Dataset
SELECT 
    o.order_id,
    o.order_date,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    s.store_name,
    CONCAT(st.first_name, ' ', st.last_name) AS staff_name,
    p.product_name,
    cat.category_name,
    b.brand_name,
    oi.quantity,
    oi.list_price,
    oi.discount,
    oi.quantity * oi.list_price * (1 - oi.discount) AS net_line_revenue
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN sales.customers c ON o.customer_id = c.customer_id
JOIN sales.stores s ON o.store_id = s.store_id
JOIN sales.staffs st ON o.staff_id = st.staff_id
JOIN production.products p ON oi.product_id = p.product_id
JOIN production.categories cat ON p.category_id = cat.category_id
JOIN production.brands b ON p.brand_id = b.brand_id
WHERE o.order_status = 4
ORDER BY o.order_date DESC;


-- Task 2: Store Performance Summary
SELECT
    s.store_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.quantity) AS total_units_sold,
    SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_net_revenue,
    SUM(oi.quantity * oi.list_price * (1 - oi.discount)) 
        / COUNT(DISTINCT o.order_id) AS average_order_value
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN sales.stores s ON o.store_id = s.store_id
WHERE o.order_status = 4
GROUP BY s.store_name
ORDER BY total_net_revenue DESC;


-- Task 3: High-Value Customers
WITH customer_totals AS (
    SELECT
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        COUNT(DISTINCT o.order_id) AS completed_order_count,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_spending
    FROM sales.customers c
    JOIN sales.orders o ON c.customer_id = o.customer_id
    JOIN sales.order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 4
    GROUP BY c.customer_id, c.first_name, c.last_name
)
SELECT
    customer_id,
    customer_name,
    completed_order_count,
    total_spending
FROM customer_totals
WHERE total_spending > (SELECT AVG(total_spending) FROM customer_totals)
ORDER BY total_spending DESC;


-- Task 4: Inventory Risk Report
SELECT
    p.product_name,
    s.store_name,
    stk.quantity,
    cat.category_name,
    b.brand_name
FROM production.stocks stk
JOIN production.products p ON stk.product_id = p.product_id
JOIN production.categories cat ON p.category_id = cat.category_id
JOIN production.brands b ON p.brand_id = b.brand_id
JOIN sales.stores s ON stk.store_id = s.store_id
WHERE stk.quantity < 5
ORDER BY stk.quantity ASC;


-- Task 5: Top 3 Products Within Each Category
WITH product_sales AS (
    SELECT
        cat.category_name,
        p.product_name,
        SUM(oi.quantity) AS total_units_sold,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_net_revenue
    FROM sales.order_items oi
    JOIN sales.orders o ON oi.order_id = o.order_id
    JOIN production.products p ON oi.product_id = p.product_id
    JOIN production.categories cat ON p.category_id = cat.category_id
    WHERE o.order_status = 4
    GROUP BY cat.category_name, p.product_name
),
ranked_products AS (
    SELECT
        category_name,
        product_name,
        total_units_sold,
        total_net_revenue,
        RANK() OVER (PARTITION BY category_name ORDER BY total_net_revenue DESC) AS category_position
    FROM product_sales
)
SELECT *
FROM ranked_products
WHERE category_position <= 3
ORDER BY category_name, category_position;


-- Task 6: Monthly Sales Trend
WITH monthly_sales AS (
    SELECT
        YEAR(o.order_date) AS sales_year,
        MONTH(o.order_date) AS sales_month,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_net_revenue
    FROM sales.orders o
    JOIN sales.order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 4
    GROUP BY YEAR(o.order_date), MONTH(o.order_date)
)
SELECT
    sales_year,
    sales_month,
    total_net_revenue,
    LAG(total_net_revenue) OVER (ORDER BY sales_year, sales_month) AS previous_month_revenue,
    total_net_revenue - LAG(total_net_revenue) OVER (ORDER BY sales_year, sales_month) AS revenue_change
FROM monthly_sales
ORDER BY sales_year, sales_month;


-- Task 7: Reusable Reporting View
CREATE VIEW sales.vw_customer_sales_summary AS
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(DISTINCT o.order_id) AS total_completed_orders,
    IFNULL(SUM(oi.quantity), 0) AS total_units_purchased,
    IFNULL(SUM(oi.quantity * oi.list_price * (1 - oi.discount)), 0) AS total_net_revenue,
    MAX(o.order_date) AS most_recent_order_date
FROM sales.customers c
LEFT JOIN sales.orders o 
    ON c.customer_id = o.customer_id AND o.order_status = 4
LEFT JOIN sales.order_items oi 
    ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.first_name, c.last_name;


-- Task 8: Safe Data Modification
START TRANSACTION;

UPDATE sales.customers
SET phone = '(999) 555-0101'
WHERE customer_id = 1;

SELECT customer_id, first_name, last_name, phone
FROM sales.customers
WHERE customer_id = 1;

ROLLBACK;


-- Task 9: Store Sales Procedure
DELIMITER //

CREATE PROCEDURE sales.usp_store_sales_report(
    IN in_store_id INT,
    IN in_start_date DATE,
    IN in_end_date DATE
)
BEGIN
    IF in_start_date > in_end_date THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Start date cannot be later than the end date.';
    ELSE
        SELECT
            p.product_name,
            SUM(oi.quantity) AS total_units_sold,
            SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_net_revenue
        FROM sales.orders o
        JOIN sales.order_items oi ON o.order_id = oi.order_id
        JOIN production.products p ON oi.product_id = p.product_id
        WHERE o.order_status = 4
            AND o.store_id = in_store_id
            AND o.order_date BETWEEN in_start_date AND in_end_date
        GROUP BY p.product_name
        ORDER BY total_net_revenue DESC;
    END IF;
END //

DELIMITER ;

-- Call example:
-- CALL sales.usp_store_sales_report(1, '2018-01-01', '2018-12-31');


-- Task 10: Management Insight Query
SELECT
    b.brand_name,
    COUNT(DISTINCT o.customer_id) AS distinct_customers,
    SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_net_revenue
FROM sales.orders o
JOIN sales.order_items oi ON o.order_id = oi.order_id
JOIN production.products p ON oi.product_id = p.product_id
JOIN production.brands b ON p.brand_id = b.brand_id
WHERE o.order_status = 4
GROUP BY b.brand_name
ORDER BY total_net_revenue DESC;

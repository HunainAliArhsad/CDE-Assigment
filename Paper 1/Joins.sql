Joins

SELECT 
    o.order_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    st.store_name,
    sf.first_name || ' ' || sf.last_name AS staff_name
FROM sales.orders o
INNER JOIN sales.customers c 
    ON o.customer_id = c.customer_id
INNER JOIN sales.stores st 
    ON o.store_id = st.store_id
INNER JOIN sales.staffs sf 
    ON o.staff_id = sf.staff_id;
  ############################################################################
  SELECT 
    p.product_id,
    p.product_name,
    b.brand_name,
    cat.category_name
FROM production.products p
LEFT JOIN production.brands b 
    ON p.brand_id = b.brand_id
LEFT JOIN production.categories cat 
    ON p.category_id = cat.category_id;
    ####################################################################
    SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    c.city,
    c.email
FROM sales.customers c
LEFT JOIN sales.orders o 
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

###########################################################################


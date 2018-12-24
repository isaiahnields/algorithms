SELECT salesperson.name FROM salesperson
WHERE salesperson.sales_id NOT IN 
    (SELECT DISTINCT o.sales_id 
    FROM company c 
    INNER JOIN orders o ON o.com_id = c.com_id 
    WHERE c.name = "RED");

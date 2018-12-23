SELECT *, 
    CASE 
        WHEN ((x + y > z) AND (z + x > y) AND (y + z > x)) = 1 THEN 'Yes' 
        ELSE 'No'
    END AS triangle 
FROM triangle;

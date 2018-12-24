SELECT DISTINCT a.seat_id 
FROM cinema a, cinema b 
WHERE a.free AND b.free AND ABS(a.seat_id - b.seat_id) = 1
ORDER BY a.seat_id ASC;

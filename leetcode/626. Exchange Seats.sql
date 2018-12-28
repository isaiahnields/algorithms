SELECT
    CASE
        WHEN id % 2 = 0 THEN id - 1
        WHEN max_id = id THEN id
        ELSE id + 1
    END AS id,
    student
FROM
    seat,
    (SELECT COUNT(*) AS max_id FROM seat) AS c
ORDER BY id ASC;

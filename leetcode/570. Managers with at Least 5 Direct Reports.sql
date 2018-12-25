SELECT Name FROM Employee
INNER JOIN
    (SELECT ManagerId
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) > 4) AS T
ON Employee.Id = T.ManagerId;

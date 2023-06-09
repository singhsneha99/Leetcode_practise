# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE t1
FROM Person t1
JOIN (
    SELECT MIN(id) AS min_id, email
    FROM Person
    GROUP BY email
    HAVING COUNT(*) > 1
) t2 ON t1.email = t2.email
WHERE t1.id > t2.min_id;


-- Problem: Recyclable and Low Fat Products
-- Find the IDs of products that are both low fat and recyclable.

-- Solution:
# Write your MySQL query statement below
SELECT product_id
FROM Products
WHERE low_fats='Y' AND recyclable='Y'

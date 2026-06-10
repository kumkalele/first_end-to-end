-- ANALYSIS, FINDING KPIs

SELECT * FROM cafe_sales;

-- Total revenue
SELECT CONCAT(SUM(total_spent), ' $') AS Total_Revenue
FROM cafe_sales;

-- Best selling products
SELECT 
	item,
	SUM(total_spent) AS Total_Revenue
FROM cafe_sales
GROUP BY item
ORDER BY Total_Revenue DESC;

-- Each item's price
SELECT 
	DISTINCT(item), 
	price_per_unit
FROM cafe_sales
WHERE item != 'UNKNOWN'
ORDER BY price_per_unit DESC;

-- Location choice
SELECT 
	location, 
	COUNT(*) AS Number_Of_Transactions, 
	CAST(ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS DECIMAL(5,2)) AS Location_Percentage
FROM cafe_sales
WHERE location != 'UNKNOWN'
GROUP BY location;

-- Most profitable months
SELECT
	-- EXTRACT(MONTH FROM transaction_date) AS Month,
	MONTH(transaction_date) AS Month,
	SUM(total_spent) AS Total_Revenue
FROM cafe_sales
GROUP BY MONTH(transaction_date)
ORDER BY MONTH(transaction_date);

-- Most profitable quaters
SELECT 
	DATEPART(QUARTER, transaction_date) AS Quarter,
	SUM(total_spent) AS Total_Revenue
FROM cafe_sales
GROUP BY DATEPART(QUARTER, transaction_date)
ORDER BY DATEPART(QUARTER, transaction_date);

-- Average Order Value
SELECT
	CAST(ROUND(AVG(total_spent), 2) AS DECIMAL(5,2)) AS Average_Value
FROM cafe_sales
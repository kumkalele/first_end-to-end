-- MODELING

INSERT INTO cafe_sales
	SELECT 
		Transaction_ID,
		Item,
		TRY_CAST(Quantity AS FLOAT),
		TRY_CAST(Price_Per_Unit AS FLOAT),
		TRY_CAST(Total_Spent AS FLOAT),
		Payment_Method,
		Location,
		Transaction_Date
	FROM clean_cafe_sales;

SELECT * FROM cafe_sales;

SELECT TABLE_SCHEMA, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'cafe_sales';
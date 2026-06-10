-- STAGING

SELECT * FROM clean_cafe_sales

SELECT TABLE_SCHEMA, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS

CREATE TABLE cafe_sales (
	transaction_id NVARCHAR(50),
	item NVARCHAR(100),
	quantity FLOAT,
	price_per_unit FLOAT,
	total_spent FLOAT,
	payment_method NVARCHAR(50),
	location NVARCHAR(50),
	transaction_date DATE
	);
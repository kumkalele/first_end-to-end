# first_end-to-end

Cafe Sales Analysis
Project Overview

This project analyzes coffee shop sales data using Python, SQL Server, and Power BI.

The main objective was to build a complete analytical workflow starting from raw CSV data, through data cleaning and validation, to business analysis and dashboard creation.

The project demonstrates practical skills in:

Data cleaning and preprocessing
SQL data transformation
Data quality validation
Exploratory business analysis
Dashboard development in Power BI
Documentation and version control using Git/GitHub


Tech Stack:
Python - pandas, numpy, os
Microsoft SQL Server, SQL Server Management Studio (SSMS)
Power BI
GitHub

Project Structure
cafe-analysis/
│
├── python/
│   └── cafe_code.py
├── sql/
│   ├── Cafe_Staging.sql
│   ├── Cafe_Modeling.sql
│   └── Cafe_Analysis.sql
├── powerbi/
│   ├── Dashboard.pbix
│   └── Dashboard.jpg
├── docs/
│   └── issues_solutions.md
└── README.md

Project Workflow:
Raw CSV
    ↓
Python Data Cleaning
    ↓
SQL Server Import
    ↓
Data Validation & Transformation
    ↓
Business Analysis Queries
    ↓
Power BI Dashboard


Data Cleaning and Preparation:
The dataset required multiple cleaning and validation steps before analysis:

Standardized column names
Replaced whitespaces in column names with underscores
Handled missing values with proper calculations
Corrected invalid categorical values
Fixed import-related datatype issues
Reconstructed product names where possible using transaction prices
Replaced unresolved values with "Unknown"

The analysis focuses on answering the following questions:

Which products generate the highest revenue?
Which products are sold most frequently?
What is the revenue distribution by quarter?
What is the payment method distribution?
What is the average transaction value?
Which products contribute most to total sales?


The Power BI dashboard provides:

Total Revenue KPI
Total Transactions KPI
Average Transaction Value
Revenue by Product
Revenue Trends by Month
Best selling products

Interactive slicer allows filtering by time period.

Challenges and Solutions

A detailed description of all technical issues encountered during the project can be found in:

docs/issues_and_solutions.md

The document includes:

SQL Server import problems
Data quality issues
Handling invalid values
Item reconstruction logic
Column naming standardization
Lessons Learned

Throughout this project I gained practical experience in:

Designing an end-to-end analytics workflow
Data cleaning using Python and Pandas
Working with SQL Server import limitations
Building staging and transformation processes
Using SQL window functions
Creating business-oriented SQL queries
Designing interactive dashboards in Power BI
Documenting analytical projects for GitHub portfolios
Maintaining reproducible and well-structured project repositories

Created as a portfolio project to demonstrate practical skills in:
Data Analytics
SQL
Python
Business Intelligence
Data Cleaning and Validation
 

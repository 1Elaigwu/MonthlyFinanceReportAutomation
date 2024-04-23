# SQL Queries Documentation

This document provides details about the SQL queries used in the Monthly Financial Reporting project to clean and process financial data.

## Data Cleaning Queries

### Update Units Sold Column

```sql
UPDATE [dbo].[financial_data]
SET [Units Sold] = REPLACE([Units Sold], '$', '')
WHERE [Units Sold] LIKE '%$%';
```
### Update Gross Sales Column
```sql
UPDATE [dbo].[financial_data]
SET [Gross Sales] = REPLACE([Gross Sales], '$', '')
WHERE [Gross Sales] LIKE '%$%';
```

### Update Discounts Column
```sql
UPDATE [dbo].[financial_data]
SET [Discounts] = REPLACE([Discounts], '$', '')
WHERE [Discounts] LIKE '%$%';
```

### Update Sales Column
```sql
UPDATE [dbo].[financial_data]
SET [Sales] = REPLACE([Sales], '$', '')
WHERE [Sales] LIKE '%$%';
```

### Update COGS Column
```sql
UPDATE [dbo].[financial_data]
SET [COGS] = REPLACE([COGS], '$', '')
WHERE [COGS] LIKE '%$%';
```

### Update Profit Column
```sql
UPDATE [dbo].[financial_data]
SET [Profit] = REPLACE([Profit], '$', '')
WHERE [Profit] LIKE '%$%';

UPDATE [dbo].[financial_data]
SET [Profit] = REPLACE([Profit], '-', '')
WHERE [Profit] LIKE '%-%';

UPDATE [dbo].[financial_data]
SET [Profit] = REPLACE(REPLACE([Profit], '(', ''), ')', '')
WHERE [Profit] LIKE '%(%' OR [Profit] LIKE '%)%';

UPDATE [dbo].[financial_data]
SET [Profit] = REPLACE([Profit], ',', '')
WHERE [Profit] LIKE '%,%';

UPDATE [dbo].[financial_data]
SET [Profit] = COALESCE(TRY_CAST(REPLACE([Profit], ',', '') AS DECIMAL(18, 2)), 0.00);
```

## Data Type Conversion Queries

### Convert Units Sold Column to Decimal
```sql
ALTER TABLE [dbo].[financial_data]
ALTER COLUMN [Units Sold] DECIMAL(18, 2);
```

### Convert Gross Sales Column to Decimal
```sql
ALTER TABLE [dbo].[financial_data]
ALTER COLUMN [Gross Sales] DECIMAL(18, 2);
```

### Convert COGS Column to Decimal
```sql
ALTER TABLE [dbo].[financial_data]
ALTER COLUMN [COGS] DECIMAL(18, 2);
```

### Convert Discounts Column to Decimal
```sql
ALTER TABLE [dbo].[financial_data]
ALTER COLUMN [Discounts] DECIMAL(18, 2);
```

### Convert Sales Column to Decimal
```sql
ALTER TABLE [dbo].[financial_data]
ALTER COLUMN [Sales] DECIMAL(18, 2);
```

## Stored Procedure
### Monthly Financial Reporting Stored Procedure

```sql
CREATE PROCEDURE MonthlyFinancialReporting
AS
BEGIN
    SET NOCOUNT ON;

    -- Create a temporary table to store sample data
    CREATE TABLE #FinancialData (
        Segment VARCHAR(50),
        Country VARCHAR(50),
        Product VARCHAR(50),
        [Discount Band] VARCHAR(50),
        [Units Sold] INT,
        [Manufacturing Price] DECIMAL(18, 2),
        [Sale Price] DECIMAL(18, 2),
        [Gross Sales] DECIMAL(18, 2),
        Discounts DECIMAL(18, 2),
        Sales DECIMAL(18, 2),
        COGS DECIMAL(18, 2),
        Profit DECIMAL(18, 2),
        [Date] DATE,
        [Month Number] INT,
        [Month Name] VARCHAR(20),
        [Year] INT
    );

    -- Insert sample data into the temporary table
    INSERT INTO #FinancialData (Segment, Country, Product, [Discount Band], [Units Sold], [Manufacturing Price], [Sale Price], [Gross Sales], Discounts, Sales, COGS, Profit, [Date], [Month Number], [Month Name], [Year])
    VALUES
        ('Segment A', 'Country A', 'Product 1', 'Band A', 100, 10.00, 15.00, 1500.00, 100.00, 1400.00, 800.00, 600.00, '2024-04-15', 4, 'April', 2024),
        ('Segment B', 'Country B', 'Product 2', 'Band B', 150, 12.00, 18.00, 2700.00, 200.00, 2500.00, 1200.00, 1300.00, '2024-04-20', 4, 'April', 2024),
        ('Segment A', 'Country C', 'Product 3', 'Band C', 200, 8.00, 12.00, 2400.00, 150.00, 2250.00, 1500.00, 750.00, '2024-04-25', 4, 'April', 2024);

    -- Generate summary for the current month
    SELECT 
        [Month Name],
        [Year],
        SUM([Units Sold]) AS TotalUnitsSold,
        SUM([Gross Sales]) AS TotalGrossSales,
        SUM(Discounts) AS TotalDiscounts,
        SUM(Sales) AS TotalSales,
        SUM(COGS) AS TotalCOGS,
        SUM(Profit) AS TotalProfit
    FROM 
        #FinancialData
    WHERE
        [Month Number] = MONTH(GETDATE())
        AND [Year] = YEAR(GETDATE())
    GROUP BY 
        [Month Name], [Year];

    -- Clean up temporary table
    DROP TABLE #FinancialData;
END
GO
```

## View
### Financial Summary View
```sql
-- Create a parameterized view to generate financial summaries for specific months and years
CREATE VIEW FinancialSummaryView
AS
    SELECT 
        [Month Name],
        [Year],
        SUM([Units Sold]) AS TotalUnitsSold,
        SUM([Gross Sales]) AS TotalGrossSales,
        SUM([Discounts]) AS TotalDiscounts,
        SUM([Sales]) AS TotalSales,
        SUM([COGS]) AS TotalCOGS,
        SUM([Profit]) AS TotalProfit
    FROM [dbo].[financial_data]
    GROUP BY 
        [Month Name], [Year];
```
These SQL queries define the operations for data cleaning, data type conversion, stored procedure creation (MonthlyFinancialReporting), and view creation (FinancialSummaryView) within 
the Monthly Financial Reporting project.

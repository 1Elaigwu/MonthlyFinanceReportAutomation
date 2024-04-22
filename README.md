# Monthly Financial Reporting Project

## Overview

The Monthly Financial Reporting project aims to process financial data stored in a SQL Server database (`financial_data`) and generate monthly financial summaries and reports. This documentation provides insights into the project's objectives, data sources, database schema, features, and usage instructions.

## Data Source

The project uses a SQL Server database named `financial_data`, which contains detailed financial information such as sales, costs, and profits. The data is stored in tables with specific columns representing various aspects of financial transactions.

## Database Schema
- **Source:** Kaggle (https://www.kaggle.com/datasets/atharvaarya25/financials)
### Table: `financial_data`

- `Segment` (VARCHAR): Describes the market segment of the product.
- `Country` (VARCHAR): Indicates the country where the sales occurred.
- `Product` (VARCHAR): Specifies the product name.
- `Discount Band` (VARCHAR): Categorizes the discount level.
- `Units Sold` (INT): Number of units sold.
- `Manufacturing Price` (DECIMAL): Cost price of manufacturing.
- `Sale Price` (DECIMAL): Selling price of the product.
- `Gross Sales` (DECIMAL): Total sales amount before discounts.
- `Discounts` (DECIMAL): Amount of discounts applied.
- `Sales` (DECIMAL): Net sales amount after discounts.
- `COGS` (DECIMAL): Cost of goods sold.
- `Profit` (DECIMAL): Profit earned from the transaction.
- `Date` (DATE): Date of the transaction.
- `Month Number` (INT): Month represented as a number (e.g., 1 for January).
- `Month Name` (VARCHAR): Month name (e.g., January, February).
- `Year` (INT): Year of the transaction.

## Features

### Data Cleaning

- Remove special characters like '$', '()' and '-' from numeric columns (`Units Sold`, `Gross Sales`, `Discounts`, `Sales`, `COGS`, `Profit`, `Sale Price`).
- Normalize data by converting columns from VARCHAR to DECIMAL after cleaning.
- Handle NULL or empty values appropriately during data cleaning.

### Monthly Reporting

- Create a stored procedure `MonthlyFinancialReporting` to generate monthly financial summaries.
- Utilize a temporary table (`#FinancialData`) to process and aggregate financial data for reporting purposes.

### View Creation

- Develop a parameterized view `FinancialSummaryView` for flexible financial data analysis by month and year.

## Usage

### Monthly Financial Reporting

1. Execute the `MonthlyFinancialReporting` stored procedure to generate monthly financial summaries:

    ```sql
    EXEC MonthlyFinancialReporting;
    ```

### Financial Data Analysis

1. Query the `FinancialSummaryView` to analyze financial summaries by specific months and years:

    ```sql
    -- Query financial summary for a specific month and year
    SELECT *
    FROM FinancialSummaryView
    WHERE [Month Name] = 'June' AND [Year] = 2014;
    ```
## Technologies Used

The following technologies and tools are utilized in this project:
- SQL
- SQL Server Management Studio (SSMS) or equivalent

## Contributing

Contributions to enhance existing scripts or add new functionalities are welcome. Fork the repository, make your changes, and submit a pull request.

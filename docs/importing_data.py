import sqlalchemy
import pandas as pd
import os

# Define SQL Server connection parameters
server_name = ''  # Replace 'your_server_name' with your SQL Server hostname
database_name = 'FinancialReport'
driver = 'ODBC Driver 17 for SQL Server'
trusted_connection = 'yes'

# Specify the path to your CSV file
csv_file_path = r"C:\Users\
# Create the connection string
connection_string = f'mssql+pyodbc://{server_name}/{database_name}?trusted_connection={trusted_connection}&driver={driver}'

# Create the SQL Alchemy engine
engine = sqlalchemy.create_engine(connection_string)

# Specify the desired table name for the SQL Server table
table_name = 'financial_data'

# Read CSV file into pandas DataFrame
df = pd.read_csv(csv_file_path)

# Write DataFrame to SQL Server table
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

print(f"CSV file '{csv_file_path}' imported successfully into table '{table_name}' in SQL Server.")

# Dispose of the database engine connection
engine.dispose()

print("CSV file imported into SQL Server.")

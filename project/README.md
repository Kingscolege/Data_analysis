# End-to-End ETL & Data Analysis Pipeline

## Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load)
pipeline using an e-commerce dataset.

The project demonstrates data cleaning with Python and Pandas,
loading structured data into MySQL, validating data quality,
performing SQL analysis, and visualizing results using Matplotlib.

## Technologies Used

- Python
- Pandas
- MySQL
- SQLAlchemy
- PyMySQL
- Matplotlib
- Jupyter Notebook

## Dataset

The project uses two CSV files:

- customer_details.csv
- basket_details.csv

Dataset source:
https://www.kaggle.com/datasets/berkayalan/ecommerce-sales-dataset

## Project Workflow

### 1. Extract

Loaded the customer and basket CSV files into Pandas DataFrames.

### 2. Transform

Cleaned and prepared the data by examining data types, handling
implausible customer ages, standardizing categorical values,
and converting basket dates to datetime format.

The original raw files were preserved.

### 3. Load

Loaded the cleaned customer and basket datasets into MySQL tables:

- customer_details
- basket_details

### 4. Data Validation

Compared CSV and database row counts.

Results:

- Customer records: 20,000
- Basket records: 15,000

Verified that the missing-age counts matched between the cleaned
customer CSV and the MySQL table.

Checked missing values in important customer and basket fields.

### 5. Data Analysis

Performed SQL analysis to identify the top 10 products by total
recorded basket quantity.

Analyzed daily basket activity to examine changes in recorded
quantity over time.

### 6. Visualization

Created visualizations using Matplotlib:

- Daily Basket Quantity
- Top 10 Products by Total Quantity

## Key Findings

Product 43524799 had the highest total recorded quantity among
the top 10 products in the analysis.

The daily basket activity chart provides a view of how recorded
basket quantities vary over time.

These results describe the available dataset and do not establish
product revenue or profit.

## Project Structure

- data/raw/: Original source files
- data/processed/: Cleaned CSV files and saved charts
- notebooks/: Data cleaning notebook
- sqlconnection.ipynb: MySQL loading, validation, and analysis

## Future Improvements

- Perform more comprehensive data validation.
- Investigate unmatched customer IDs between the two datasets.
- Compare all relevant CSV values with the corresponding MySQL data.
- Expand the SQL analysis.
- Build an interactive dashboard.

## Conclusion

This project demonstrates the main stages of an ETL pipeline,
from extracting and cleaning raw data to loading it into MySQL,
validating data quality, and performing exploratory analysis.
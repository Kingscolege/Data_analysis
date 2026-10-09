import pandas as pd

basket_df = pd.read_csv("basket_details.csv")
print("="*50)
print("Basket Data")
print("="*50)
customer_df = pd.read_csv("customer_details.csv")
print("="*50)
print("Customer Data")
print("="*50)

print(basket_df.head())
print("="*50)
print(customer_df.head())
print("="*50)
print(basket_df.shape)
print("="*50)
print(customer_df.shape)
print("="*50)
print(basket_df.columns)
print("="*50)

print(customer_df.columns)
print("="*50)

print(basket_df.dtypes)
print("="*50)

print(customer_df.dtypes)
print("="*50)

print(basket_df.describe())
print("="*50)

print(customer_df.describe())
print("="*50)



print(basket_df.isnull().sum())
print("="*50)

print(customer_df.isnull().sum())
print("="*50)


print("Basket duplicates", basket_df.duplicated().sum())
print("="*50)

print("Customer duplicates", customer_df.duplicated().sum())
print("="*50)


print("Total basket records:", len(basket_df))
print("="*50)
print("Unique customers:", basket_df["customer_id"].nunique())
print("="*50)
print("Unique products:", basket_df["product_id"].nunique())
print("="*50)
print("Total basket count:", basket_df["basket_count"].sum())
print("="*50)
top_products = (
    basket_df.groupby("product_id")["basket_count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)
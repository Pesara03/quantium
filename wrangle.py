import pandas as pd

# Load CSV files
df_0 = pd.read_csv("daily_sales_data_0.csv")
df_1 = pd.read_csv("daily_sales_data_1.csv")
df_2 = pd.read_csv("daily_sales_data_2.csv")

# Combine dataframes into one big dataframe
df = pd.concat([df_0, df_1, df_2])

# Filter rows where product is "pink morsel"
df = df[df['product'] == 'pink morsel']

# Combine quantity and price into sales
df['sales'] = df['quantity'] * df['price']

# Select required fields
selected_df = df[['sales', 'date', 'region']]

# Save to output file
selected_df.to_csv("formatted_output.csv", index=False)

import pandas as pd

# List of CSV files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Empty list to store processed data
all_data = []

# Read and process each file
for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]

    # Remove $ sign and convert price to float
    df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

    # Calculate sales
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    all_data.append(df)

# Combine all files
final_df = pd.concat(all_data)

# Save output
final_df.to_csv("formatted_sales_data.csv", index=False)

print("File created successfully!")
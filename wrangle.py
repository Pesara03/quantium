import csv

# Initialize an empty list to store the combined data
combined_data = []

# Function to convert price to numeric type
def convert_price(price_str):
    # Remove '$' sign and convert to float
    return float(price_str.replace('$', ''))

# Function to filter rows and calculate sales
def process_row(row):
    # Check if the product is "pink morsel"
    if row[0] == 'pink morsel':
        # Convert price to numeric type
        price = convert_price(row[1])
        # Calculate sales
        sales = int(row[2]) * price
        # Append sales, date, and region to combined_data
        combined_data.append([sales, row[3], row[4]])

# Read and append data from daily_sales_data_0.csv
with open("daily_sales_data_0.csv", newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        process_row(row)

# Read and append data from daily_sales_data_1.csv
with open("daily_sales_data_1.csv", newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        process_row(row)

# Read and append data from daily_sales_data_2.csv
with open("daily_sales_data_2.csv", newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        process_row(row)

# Save combined data to a new CSV file
with open("formatted_output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sales", "Date", "Region"])  # Write header
    writer.writerows(combined_data)
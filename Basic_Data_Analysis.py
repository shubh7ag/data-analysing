
import pandas as pd

# Step 1: Load the CSV File
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("CSV file loaded successfully!")
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

# Step 2: Display Basic Information
def display_info(data):
    print("\n--- Dataset Information ---")
    print(data.info())

# Step 3: Display Summary Statistics
def display_statistics(data):
    print("\n--- Summary Statistics ---")
    print(data.describe())

# Step 4: Display First Few Rows
def display_head(data, num_rows=5):
    print(f"\n--- First {num_rows} Rows ---")
    print(data.head(num_rows))

# Step 5: Check for Missing Values
def check_missing_values(data):
    print("\n--- Missing Values ---")
    print(data.isnull().sum())

# Step 6: Display Column Names
def display_columns(data):
    print("\n--- Column Names ---")
    print(data.columns)

# Step 7: Example Analysis - Grouping and Aggregation
def group_and_aggregate(data, group_by_column, agg_column):
    print(f"\n--- Grouping by '{group_by_column}' and Aggregating '{agg_column}' ---")
    grouped_data = data.groupby(group_by_column)[agg_column].mean()
    print(grouped_data)

# Main Program
if __name__ == "__main__":
    # Provide the path to your CSV file
    file_path = input("Enter the path to your CSV file: ")
    
    data = load_csv(file_path)
    if data is not None:
        # Perform basic data analysis
        display_info(data)
        display_statistics(data)
        display_head(data)
        check_missing_values(data)
        display_columns(data)
        
        # Optional: Perform grouping and aggregation
        group_column = input("\nEnter a column to group by (or press Enter to skip): ")
        agg_column = input("Enter a column to aggregate (or press Enter to skip): ")
        if group_column and agg_column:
            group_and_aggregate(data, group_column, agg_column)

import pandas as pd
from tabulate import tabulate

# Replace 'your_file.csv' with the actual CSV file path
file_path = 'c:\Data\data2.csv'

# Replace 'index_column_name' with the name of the column you want to set as the index
index_column_name = 'ID'

# Read the CSV file into a pandas DataFrame and set the specified column as the index
df = pd.read_csv(file_path, index_col=index_column_name)

num_rows, num_columns = df.shape

# Convert the DataFrame to a tabular format with left-aligned columns
table = tabulate(df, headers='keys', tablefmt='pipe', colalign=("left",))

metadata = f"File Metadata: Rows={num_rows}, Columns={num_columns}\n"

# Print the tabulated table
print(metadata)
print(table)
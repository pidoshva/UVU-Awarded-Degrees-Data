"""
This program reads data (Degrees Awarded by Type) provided by Business Intelligence & Research Services at UVU.

Use to avoid spreadsheets. 

by Vadim Pidoshva
"""

import pandas as pd
from tabulate import tabulate
import chardet

def detect_encoding(file_path):
    """Detect the encoding of a CSV file."""
    with open(file_path, 'rb') as f:
        raw_data = f.read(10000)
        result = chardet.detect(raw_data)
        return result['encoding']

def load_data(file_path):
    """Load CSV data into a pandas DataFrame with duplicate column handling."""
    encoding = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")

    try:
        df = pd.read_csv(file_path, encoding=encoding, delimiter='\t')  # Handling tab-separated values
        df.columns = ['COLLEGE', 'DEPARTMENT', 'MAJOR_DESC', 'grad_yr', 
                      'pDegreeLevelType', 'Number_Percentage', 'COLLEGE_2', 
                      'DEPARTMENT_2', 'Number_of_Records']
        return df
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None

def filter_data(df, major, year, degree_type):
    """Filter data based on user input."""
    filtered_df = df[
        (df['MAJOR_DESC'].str.contains(major, case=False, na=False)) &
        (df['grad_yr'].astype(str) == year) &
        (df['pDegreeLevelType'].str.contains(degree_type, case=False, na=False))
    ]
    return filtered_df

def display_data(df):
    """Display data in a formatted table."""
    if df.empty:
        print("\nNo matching records found.\n")
    else:
        print("\nFiltered Data:\n")
        print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))

def main():
    file_path = input("Enter the path to the CSV file: ").strip()
    df = load_data(file_path)

    if df is None:
        return

    print("\nPlease provide the following details to filter the data:")
    
    major = input("Enter the major: ").strip()
    year = input("Enter the graduation year: ").strip()
    degree_type = input("Enter the degree type (Master, Bachelor, Associate, Certificate/Diplomas): ").strip()

    filtered_df = filter_data(df, major, year, degree_type)
    display_data(filtered_df)

if __name__ == "__main__":
    main()

# UVU Awarded Degrees Data Finder

## Overview
This program reads a CSV file containing data about various majors, graduation years, and degree levels at UVU. The user can input a major, graduation year, and degree type, and the program will display the relevant information in a structured and visually appealing format.  

Created for `https://www.uvu.edu/birs//performance-indicators/academic-programs/degrees_awarded_by_type.html#graduates`.  However, might be rellocated.  

**Note**: Database updates every year. Last update 2024. Make sure to download updated CSV file when provided.  

## Features
- Detects the encoding of the CSV file to prevent reading errors.
- Handles tab-separated CSV files.
- Filters data based on user input.
- Displays results in an easy-to-read table format.
- Shows both the number of students and percentage values.

## Prerequisites
Ensure you have Python 3 installed along with the following dependencies:

```bash
pip install pandas tabulate chardet
```

## How to Use

1. Clone or download the repository.
2. Prepare your CSV file with the expected columns:
   - `COLLEGE`
   - `DEPARTMENT`
   - `MAJOR_DESC`
   - `grad_yr`
   - `pDegreeLevelType`
   - `Number / Percentage`
   - `COLLEGE`
   - `DEPARTMENT`
   - `Number of Records`
3. Run the script with:

```bash
python3 find.py
```

4. Enter the path to the CSV file when prompted.
5. Provide the required details:
   - Major name
   - Graduation year
   - Degree type (Master, Bachelor, Associate, Certificate/Diplomas)

6. View the displayed results.

## Example Output

```console
Enter the path to the CSV file: major_graph_data.csv
Please provide the following details to filter the data:
Enter the major: Computer Science
Enter the graduation year: 2024
Enter the degree type (Master, Bachelor, Associate, Certificate/Diplomas): Bachelor


Filtered Data:

╒═══════════╤══════════════╤══════════════════╤═══════════╤════════════════════╤═════════════════════╤═════════════╤════════════════╤═════════════════════╕
│ COLLEGE   │ DEPARTMENT   │ MAJOR_DESC       │   grad_yr │ pDegreeLevelType   │   Number_Percentage │ COLLEGE_2   │ DEPARTMENT_2   │   Number_of_Records │
╞═══════════╪══════════════╪══════════════════╪═══════════╪════════════════════╪═════════════════════╪═════════════╪════════════════╪═════════════════════╡
│ EN        │ CSE          │ Computer Science │      2024 │ Bachelor Degrees   │                  97 │ EN          │ CSE            │                  97 │
╘═══════════╧══════════════╧══════════════════╧═══════════╧════════════════════╧═════════════════════╧═════════════╧════════════════╧═════════════════════╛
```

## Code Structure

- `find.py`: Main script to run the program.
- `requirements.txt`: Dependencies list.

## Handling Duplicate Columns

Since the CSV file contains duplicate column names (`COLLEGE`, `DEPARTMENT`), the script renames them to:

- `COLLEGE_2`
- `DEPARTMENT_2`

## Error Handling

- Handles encoding issues.
- Displays an error message if no matching records are found.

## Author
Vadim Pidoshva



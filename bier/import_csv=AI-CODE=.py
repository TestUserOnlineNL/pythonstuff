import csv

# CSV file path
csv_file = "/home/pi/GitHub/pythonstuff/bier/test.csv"

# Get maximum data width per column
def get_max_data_width(csv_file):
    """Calculates the maximum data width for each column in a CSV file.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        list: A list containing the maximum widths for each column.
    """

    max_widths = [0] * 3
    try:
        with open(csv_file, "r", encoding="UTF8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                for i, cell in enumerate(row):
                    max_widths[i] = max(max_widths[i], len(cell))
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
        return None
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
        return None
    return max_widths

# Fill up row data with padding
def fill_row_data(row, max_widths):
    """Fills up row data with padding to ensure consistent column widths.

    Args:
        row (list): The row data to be filled.
        max_widths (list): A list containing the maximum widths for each column.

    Returns:
        list: The filled row data.
    """

    return [cell.ljust(max_widths[i]) for i, cell in enumerate(row)]

# Print rows with fixed column widths
def print_rows_with_fixed_width(csv_file):
    """Prints rows from a CSV file with fixed column widths.

    Args:
        csv_file (str): The path to the CSV file.
    """

    max_widths = get_max_data_width(csv_file)
    if max_widths is None:
        return
    with open(csv_file, "r", encoding="UTF8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            filled_row = fill_row_data(row, max_widths)
            print(" ".join(filled_row))

# Start
print_rows_with_fixed_width(csv_file)
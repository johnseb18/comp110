"""Dictionary related utility functions."""

__author__ = "730612873"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings 
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()
    
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row_oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Returning only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        if rows > len(table):
            return table
        a_list: list[str] = []
        n: int = 0
        while n < rows:
            a_list.append(table[column][n])
            n += 1
        result[column] = a_list
    return result


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Creating a new column-based table with only specific subset of original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    return result


def concat(input_1: dict[str, list[str]], input_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creating a new column-based table with two tables combined."""
    result: dict[str, list[str]] = {}
    for column in input_1:
        result[column] = input_1[column]
    for column in input_2:
        if column in result:
            result[column] += input_2[column]
        else:
            result[column] = input_2[column]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Creating a dictionary where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for n in values:
        if n in result:
            result[n] += 1
        else:
            result[n] = 1
    return result
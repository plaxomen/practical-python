# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str, select=None, types=None, has_headers=True, delimiter=","
) -> dict:
    """A function that takes a csv filename as input and returns a
    list of dictionaries representing each row of data."""
    if select and not has_headers:
        raise RuntimeError(
            f"'select' column headers provided ({select}) for file containing no headers."
        )

    with open(filename, "rt") as f:
        rows = csv.reader(f, delimiter=delimiter)

        # If file has headers then handle for headers and possible select columns.
        if has_headers:
            # Read file headers.
            header = next(rows)

            # If select columns provided, find the indices of the columns names from existing headers.
            if select:
                indices = [header.index(colname) for colname in select]
                header = select
            else:
                indices = []

        records = []
        for rowno, row in enumerate(rows, start=1):
            try:
                if not row:  # Skip empty rows.
                    continue

                # Filter the row if specific columns were selected
                if has_headers and indices:
                    row = [row[index] for index in indices]

                # Apply type conversions of specific types were provided
                if types:
                    row = [func(value) for func, value in zip(types, row)]

                # Build dictionay if headers supplied or tuples if missing headers
                if has_headers:
                    record = dict(zip(header, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                print(f"Error processing row {rowno}: {row}")
                print(f"\tError Message: {e}")
    return records

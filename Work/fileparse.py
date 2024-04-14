# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str, select=None, types=None) -> dict:
    """A function that takes a csv filename as input and returns a
    list of dictionaries representing each row of data."""
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        # Read file headers.
        header = next(rows)

        # If select columns provided, find the indices of the columns names from existing headers.
        if select:
            indices = [header.index(colname) for colname in select]
            header = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip empty rows.
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Apply type conversions of specific types were provided
            if types:
                row = [func(value) for func, value in zip(types, row)]

            # Build Dictionary
            record = dict(zip(header, row))
            records.append(record)
    return records

# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename: str) -> dict:
    """A function that takes a csv filename as input and returns a
    list of dictionaries representing each row of data."""
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        # Read the file headers.
        header = next(rows)
        records = []
        for row in rows:
            if not row:  # Skip empty rows.
                continue
            record = dict(zip(header, row))
            records.append(record)
    return records

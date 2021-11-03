"""Utility functions."""

__author__ = "730393060"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of the csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(data_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """List of rows turned into dictionary of columns."""
    data_cols: dict[str, list[str]] = {}
    first_row: dict[str, str] = data_rows[0]
    for column in first_row:
        data_cols[column] = column_values(data_rows, column)
    return data_cols


def head(column_based: dict[str, list[str]], rows_included: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first row of data."""
    final: dict[str, list[str]] = {}
    for column in column_based:
        if rows_included >= len(column_based[column]):
            return column_based
        else:
            new: list[str] = []
            point = column_based[column]
            i: int = 0
            while i < rows_included:
                new.append(point[i])
                i += 1
            final[column] = new
    return final


def select(column_based: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a subset of original columns."""
    returned: dict[str, list[str]] = {}
    for n in names:
        returned[n] = column_based[n]
    return returned


def concat(column_one: dict[str, list[str]], column_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """New dictionary from two combined column-based tables."""
    ending: dict[str, list[str]] = {}
    for column in column_one:
        ending[column] = column_one[column]
    for column in ending:
        if column in ending:
            column_one[column] + column_two[column]
        else:
            ending[column] = column_two[column]
    return ending


def count(frequencies: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for key in frequencies:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result
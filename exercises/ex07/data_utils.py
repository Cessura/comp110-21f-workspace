"""Utility functions."""

__author__ = "730330727"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
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


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(dic: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Shows the first parts of a dictionary."""
    result: dict[str, list[str]] = {}
    k: int = 0
    
    if N > len(dic):
        N = len(dic)

    for i in dic:
        workhorse: list[str] = []
        while k < N:
            workhorse.append(dic[i][k])
            k = k + 1
        result[i] = workhorse
        workhorse = []
        k = 0
    
    return result


def select(dic: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Picks certain columns to leave a dictionary for."""
    result: dict[str, list[str]] = {}
    k: int = 0
    while k < len(names):
        result[names[k]] = dic[names[k]]
        k = k + 1
    
    return result


def concat(dic_1: dict[str, list[str]], dic_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Stick together two dicitonaries."""
    result: dict[str, list[str]] = {}
    for k in dic_1:
        result[k] = dic_1[k]
    for k in dic_2: 
        if k in result:
            result[k] = result[k] + dic_2[k]
        else:
            result[k] = dic_2[k]

    return result


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a thing occurs in the list."""
    workhorse: dict[str, int] = {}
    comparator: str = str("")
    i = 0

    if len(a) < 1:
        raise IndexError

    while i < len(a):
        workhorse[a[i]] = 0
        i += 1

    i = 0

    while i < len(a):
        for key in workhorse: 
            comparator = key
            if a[i] == comparator:
                workhorse[a[i]] += 1
        i = i + 1 

    return workhorse

from prettytable import PrettyTable

from field import columns, rows


def generate_table(field: list[list[int]]):
    table = PrettyTable()
    table.field_names = columns
    for key, val in enumerate(rows):
        table.add_row([val, *field[key]])

    return table
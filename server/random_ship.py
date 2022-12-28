from random import randint


def random_ship() -> tuple:
    ship_size = randint(2, 4)
    one_column_or_one_row = randint(0, 1)

    # Если 0 - один столбец
    if one_column_or_one_row == 0:
        ship_column = randint(0, 9)
        ship_rows_start = randint(0, 9)
        
        if ship_rows_start - ship_size >= -1:
            ship_rows = []
            for i in range(ship_size):
                ship_rows.append(ship_rows_start - i)
        elif ship_rows_start - ship_size < -1:
            ship_rows = []
            for i in range(ship_size):
                ship_rows.append(ship_rows_start + i)
        
        return one_column_or_one_row, ship_column, ship_rows
        
    # Если 1 - одна строка
    elif one_column_or_one_row == 1:
        ship_row = randint(0, 9)
        ship_columns_start = randint(0, 9)

        if ship_columns_start - ship_size >= -1:
            ship_columns = []
            for i in range(ship_size):
                ship_columns.append(ship_columns_start - i)
        elif ship_columns_start - ship_size < -1:
            ship_columns = []
            for i in range(ship_size):
                ship_columns.append(ship_columns_start + i)

        return one_column_or_one_row, ship_row, ship_columns

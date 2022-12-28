from copy import deepcopy


def spawn_ships(field: list[list[int]], ship) -> list[list[int]]:
    f = deepcopy(field)
    print(ship)

    try:
        if ship[0] == 0:
            for val in ship[2]:
                f[val][ship[1]] = 1
        elif ship[0] == 1:
            for val in ship[2]:
                f[ship[1]][val] = 1

        return f

    except Exception as e:
        print(f'ERROR IN spawn_ships(): {e}')
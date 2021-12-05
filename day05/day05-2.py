def main() -> None:
    with open('input.txt') as file:
        lines = file.read().splitlines()

    crossed_vents = {}

    for line in lines:
        coord1, coord2 = transform_line(line)
        if coord1[0] == coord2[0]:
            mark_vertical(coord1, coord2, crossed_vents)
        elif coord1[1] == coord2[1]:
            mark_horizontal(coord1, coord2, crossed_vents)
        else:
            mark_diagonal(coord1, coord2, crossed_vents)
    overlapped_points = len(crossed_vents) - list(crossed_vents.values()).count(1)
    print(overlapped_points)


def mark_horizontal(coord1: tuple, coord2: tuple, crossed_vents: dict) -> None:
    start = min(coord1[0], coord2[0])
    end = max(coord1[0], coord2[0])
    for x in range(start, end + 1):
        coord = (x, coord1[1])
        mark(crossed_vents, coord)


def mark_vertical(coord1: tuple, coord2: tuple, crossed_vents: dict) -> None:
    start = min(coord1[1], coord2[1])
    end = max(coord1[1], coord2[1])
    for y in range(start, end + 1):
        coord = (coord1[0], y)
        mark(crossed_vents, coord)


def mark_diagonal(coord1: tuple, coord2: tuple, crossed_vents: dict) -> None:
    if coord2[0] < coord1[0]:
        coord_left = coord2
        coord_right = coord1
    else:
        coord_left = coord1
        coord_right = coord2
    if coord_left[1] > coord_right[1]:
        for i in range( coord_left[1] - coord_right[1] + 1):
            coord = (coord_left[0] + i, coord_left[1] - i)
            mark(crossed_vents, coord)
    else:
        for i in range( coord_right[1] - coord_left[1] + 1):
            coord = (coord_left[0] + i, coord_left[1] + i)
            mark(crossed_vents, coord)


def mark(crossed_vents: dict, coord: tuple) -> None:
    if coord not in crossed_vents:
        crossed_vents[coord] = 1
    else:
        crossed_vents[coord] += 1


def transform_line(line: str) -> list:
    split_line = line.split(' -> ')
    return_val = []
    for part in split_line:
        numbers = part.split(',')
        return_val.append((int(numbers[0]), int(numbers[1])))
    return return_val


if __name__ == '__main__':
    main()

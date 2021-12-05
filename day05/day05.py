def main() -> None:
    with open('input.txt') as file:
        lines = file.read().splitlines()

    crossed_vents = {}

    for line in lines:
        coord1, coord2 = transform_line(line)
        if coord1[0] == coord2[0]:
            start = min(coord1[1], coord2[1])
            end = max(coord1[1], coord2[1])
            for y in range(start, end+1):
                coord = (coord1[0], y)
                mark(crossed_vents, coord)
        elif coord1[1] == coord2[1]:
            start = min(coord1[0], coord2[0])
            end = max(coord1[0], coord2[0])
            for x in range(start, end + 1):
                coord = (x, coord1[1])
                mark(crossed_vents, coord)

    overlapped_points = len(crossed_vents) - list(crossed_vents.values()).count(1)
    print(overlapped_points)


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

def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()
    octopusses = []
    for line in input_data:
        octopusses.append([int(x) for x in line])

    print(octopusses)
    step = 0

    while True:
        step += 1
        raise_by_one(octopusses)
        handle_gt_nines(octopusses)
        if count_zeroes(octopusses) == len(octopusses)*len(octopusses[0]):
            break
    print(step)


def raise_by_one(octopusses: list) -> None:
    for i in range(len(octopusses)):
        for j in range(len(octopusses[i])):
            octopusses[i][j] += 1


def count_zeroes(octopusses):
    zeroes = 0
    for line in octopusses:
        zeroes += line.count(0)
    return zeroes


def handle_gt_nines(octopusses: list) -> None:
    contains_gt_nines = True
    while contains_gt_nines:
        added_gt_nine = False
        for x in range(len(octopusses[0])):
            for y in range(len(octopusses)):
                if octopusses[y][x] > 9:
                    octopusses[y][x] = 0
                    if raise_adjacent(octopusses, x, y):
                        added_gt_nine = True
        contains_gt_nines = added_gt_nine


def raise_adjacent(grid: list, x: int, y: int) -> bool:
    added_gt_nine = False
    for i in range(x - 1, x + 2):
        if i < 0 or i >= len(grid[0]):
            continue
        for j in range(y - 1, y + 2):
            if j < 0 or j >= len(grid):
                continue
            if i == x and j == y:
                continue
            if grid[j][i] != 0:
                grid[j][i] += 1
                if grid[j][i] > 9:
                    added_gt_nine = True
    return added_gt_nine


if __name__ == '__main__':
    main()
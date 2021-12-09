def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()

    grid = []
    for line in input_data:
        grid.append([int(x) for x in line])

    risk_levels = 0
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            if is_lowest_cardinal(grid, x, y):
                risk_levels += grid[y][x] + 1
    print(risk_levels)


def is_lowest_cardinal(grid: list, x: int, y: int) -> bool:
    if x != 0 and grid[y][x - 1] <= grid[y][x]:
        return False
    if x < len(grid[0]) - 1 and grid[y][x + 1] <= grid[y][x]:
        return False
    if y != 0 and grid[y - 1][x] <= grid[y][x]:
        return False
    if y < len(grid) - 1 and grid[y + 1][x] <= grid[y][x]:
        return False
    return True


if __name__ == '__main__':
    main()

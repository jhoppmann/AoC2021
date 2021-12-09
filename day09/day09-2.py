def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()

    grid = []
    for line in input_data:
        grid.append([int(x) for x in line])

    low_points = []
    for x in range(0, len(grid[0])):
        for y in range(0, len(grid)):
            if is_lowest_cardinal(grid, x, y):
                low_points.append((x, y))

    basin_sizes = []
    already_counted = []
    for x, y in low_points:
        basin_sizes.append(get_basin_size(grid, x, y, already_counted))
    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


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


def get_basin_size(grid, x, y, already_counted):
    if (x, y) in already_counted:
        return 0
    already_counted.append((x, y))
    basin_size = 0
    if x != 0 and grid[y][x - 1] > grid[y][x] and grid[y][x - 1] != 9:
        basin_size += get_basin_size(grid, x - 1, y, already_counted)
    if x < len(grid[0]) - 1 and grid[y][x + 1] > grid[y][x] and grid[y][x + 1] != 9:
        basin_size += get_basin_size(grid, x + 1, y, already_counted)
    if y != 0 and grid[y - 1][x] > grid[y][x] and grid[y - 1][x] != 9:
        basin_size += get_basin_size(grid, x, y - 1, already_counted)
    if y < len(grid) - 1 and grid[y + 1][x] > grid[y][x] and grid[y + 1][x] != 9:
        basin_size += get_basin_size(grid, x, y + 1, already_counted)
    return basin_size + 1


if __name__ == '__main__':
    main()

import timeit
from queue import PriorityQueue


def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()

    grid = []
    for i in range(5):
        for line in input_data:
            ints = []
            for j in range(5):
                for x in line:
                    val = (int(x) + i + j)
                    if val > 9:
                        val -= 9
                    ints.append(val)
            grid.append(ints)

    starting_point = (0, 0)
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    target = (max_x, max_y)

    cost = dijkstra(grid, starting_point, target)

    print(cost[target])


def dijkstra(grid: list, starting_point: tuple, target: tuple) -> dict:
    start2 = timeit.default_timer()
    frontier = PriorityQueue()
    frontier.put((grid[0][0], starting_point))
    cost = {starting_point: 0}
    while frontier:
        current = frontier.get()
        if current[1] == target:
            break

        for neighbor in get_neighbors(grid, *current[1]):
            new_cost = cost[current[1]] + grid[neighbor[1]][neighbor[0]]
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                frontier.put((new_cost, neighbor))
    stop2 = timeit.default_timer()
    print('Time Dijkstra:: ', stop2 - start2)
    return cost


def get_neighbors(grid: list, x: int, y: int) -> list:
    neighbors = []
    if x != 0:
        neighbors.append((x - 1, y))
    if x < len(grid[0]) - 1:
        neighbors.append((x + 1, y))
    if y != 0:
        neighbors.append((x, y - 1))
    if y < len(grid) - 1:
        neighbors.append((x, y + 1))
    return neighbors


if __name__ == '__main__':
    start = timeit.default_timer()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)

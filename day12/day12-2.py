def main() -> None:
    with open('input.txt') as file:
        cave_connections = file.read().splitlines()
    cave_connections = [tuple(x.split('-')) for x in cave_connections]

    connections = map_connections(cave_connections)
    routes = []
    find_routes('start', connections, [], routes)
    print(len(routes))


def map_connections(cave_connections) -> dict:
    connections = {}
    for connection in cave_connections:
        if connection[0] not in connections:
            connections[connection[0]] = []
        connections[connection[0]].append(connection[1])
        if connection[1] not in connections:
            connections[connection[1]] = []
        connections[connection[1]].append(connection[0])

    return connections


def find_routes(current_cave, connections, route: list, routes: list) -> None:
    route.append(current_cave)
    if current_cave == 'end':
        routes.append(route)
        return
    for cave in connections[current_cave]:
        can_be_visited = cave.isupper() or may_be_visited(cave, route)
        if can_be_visited:
            find_routes(cave, connections, route.copy(), routes)


def may_be_visited(cave, route) -> bool:
    if cave == 'start':
        return False
    if cave in route:
        for previous_cave in route:
            if previous_cave.islower() and route.count(previous_cave) == 2:
                return False
    return True


if __name__ == '__main__':
    main()

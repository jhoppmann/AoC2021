def main() -> None:
    with open('input.txt') as file:
        crabs = [int(x) for x in file.read().split(',')]

    min_val = min(crabs)
    max_val = max(crabs)
    fuel_usage = len(crabs) * gauss_formula(max_val)
    for i in range(min_val, max_val + 1):
        fuel = 0
        for crab in crabs:
            fuel += gauss_formula(abs(crab - i))

        if fuel > fuel_usage:
            break
        fuel_usage = fuel

    print(fuel_usage)


def gauss_formula(n: int) -> float:
    return int((n * (n + 1)) / 2)


if __name__ == '__main__':
    main()

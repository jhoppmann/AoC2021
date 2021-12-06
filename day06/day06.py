def main() -> None:
    with open('input.txt') as file:
        fish_ages = file.read().splitlines()

    fish_ages = [int(x) for x in fish_ages[0].split(',')]

    for _ in range(80):
        new_fish_ages = []
        new_fish = 0
        for fish in fish_ages:
            if fish == 0:
                new_fish += 1
                new_fish_ages.append(6)
            else:
                new_fish_ages.append(fish - 1)
        new_fish_ages += new_fish * [8]
        fish_ages = new_fish_ages

    print(len(fish_ages))


if __name__ == '__main__':
    main()

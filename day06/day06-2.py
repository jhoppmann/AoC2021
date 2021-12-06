def main() -> None:
    with open('input.txt') as file:
        fish_ages = file.read().splitlines()

    fish_ages = [int(x) for x in fish_ages[0].split(',')]
    fish = {}
    for i in range(9):
        fish[i] = fish_ages.count(i)

    for i in range(256):
        new_ages = {}
        for j in range(8):
            new_ages[j] = fish[j+1]
            if j == 6:
                new_ages[6] += fish[0]
        new_ages[8] = fish[0]
        fish = new_ages

    print(sum(fish.values()))


if __name__ == '__main__':
    main()

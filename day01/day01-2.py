with open('input.txt') as file:
    depths = file.read().splitlines()

depths = [int(x) for x in depths]


def main():
    windows = []
    for i in range(0, len(depths) - 2):
        windows.append(depths[i] + depths[i + 1] + depths[i + 2])

    increases = 0
    for i in range(1, len(windows)):
        if windows[i] > windows[i - 1]:
            increases += 1
    print(increases)


if __name__ == '__main__':
    main()

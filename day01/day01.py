with open('input.txt') as file:
    depths = file.read().splitlines()

depths = [int(x) for x in depths]


def main():
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    print(increases)


if __name__ == "__main__":
    main()

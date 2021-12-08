def main() -> None:
    with open('input.txt') as file:
        lines = file.read().splitlines()

    searched_for_digits = 0
    for line in lines:
        notes, output = line.split(" | ")
        output = output.split()
        for token in output:
            if len(token) == 2 or len(token) == 3 or len(token) == 4 or len(token) == 7:
                searched_for_digits += 1

    print(searched_for_digits)


if __name__ == '__main__':
    main()

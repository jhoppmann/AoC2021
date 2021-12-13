def main() -> None:
    with open('input.txt') as file:
        input_data = file.read().splitlines()

    dots = []
    folding_instructions = []

    for line in input_data:
        if 'fold along' in line:
            substring = line[11:]
            split = substring.split('=')
            folding_instructions.append((split[0], int(split[1])))
        else:
            if line:
                split = line.split(',')
                dots.append((int(split[0]), int(split[1])))

    for instruction in folding_instructions[0:1]:  # this is a weird requirement for part 1
        if instruction[0] == 'x':
            new_dots = set()
            for dot in dots:
                if dot[0] < instruction[1]:
                    new_dots.add(dot)
                else:
                    new_dots.add((2 * instruction[1] - dot[0], dot[1]))
            dots = list(new_dots)
        else:
            new_dots = set()
            for dot in dots:
                if dot[1] < instruction[1]:
                    new_dots.add(dot)
                else:
                    new_dots.add((dot[0], 2 * instruction[1] - dot[1]))

            dots = list(new_dots)
    print(len(dots))


if __name__ == '__main__':
    main()

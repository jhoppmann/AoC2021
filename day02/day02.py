with open('input.txt') as file:
    course = file.read().splitlines()

course = [x.split(' ') for x in course]


def main():
    horizontal = 0
    depth = 0
    for entry in course:
        direction = entry[0]
        length = int(entry[1])
        if direction == 'down':
            depth += length
        elif direction == 'up':
            depth -= length
        elif direction == 'forward':
            horizontal += length

    print(horizontal * depth)


if __name__ == '__main__':
    main()
import re


def main() -> None:
    with open('input.txt') as file:
        input_data = file.read()

    ints = re.findall(r'-?\d+', input_data)
    ints = [int(x) for x in ints]
    x_range = (ints[0], ints[1])
    y_range = (ints[3], ints[2])  # larger number first
    width = abs(x_range[1] - x_range[0])
    height = abs(y_range[1] - y_range[0])

    position = (0, 0)
    highest = 0
    for x in range(0, x_range[1]):
        for y in range(-500, 500):
            position = (0, 0)
            speed = (x, y)
            highest_y = y
            while position[0] <= x_range[1] and position[1] >= y_range[1]:
                position, speed = step(position, speed)
                highest_y = max(highest_y, position[1])
                if x_range[0] <= position[0] <= x_range[1] and y_range[0] >= position[1] >= y_range[1]:
                    highest = max(highest_y, highest)
                    break
    print(highest)
    print(position)


def step(position: tuple, speed: tuple) -> tuple:
    position = (position[0] + speed[0], position[1] + speed[1])
    speed = (max(0, speed[0] - 1), speed[1] - 1)
    return position, speed


if __name__ == '__main__':
    main()

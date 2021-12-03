with open('input.txt') as file:
    readings = file.read().splitlines()


def main():
    lengths = len(readings[0])
    oxygen_list = readings.copy()
    co2_list = readings.copy()

    for i in range(lengths):
        if len(oxygen_list) > 1:
            most_common = order_by_occurence(oxygen_list, i)
            oxygen_list = keep(oxygen_list, i, most_common[0])
        if len(co2_list) > 1:
            most_common = order_by_occurence(co2_list, i)
            co2_list = keep(co2_list, i, most_common[1])

    print(int(oxygen_list[0], 2) * int(co2_list[0], 2))


def order_by_occurence(current_list: list, position: int) -> (int, int):
    int_list = [int(x[position]) for x in current_list]
    ones = int_list.count(1)
    if ones >= len(current_list) / 2:
        return 1, 0
    else:
        return 0, 1


def keep(this_list: list, position: int, character: int) -> list:
    character = str(character)
    result = [line for line in this_list if line[position] == character]
    return result


if __name__ == '__main__':
    main()
